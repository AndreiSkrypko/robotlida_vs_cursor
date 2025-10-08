from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import ForumPost, ForumReply
from .forms import ForumPostForm, ForumReplyForm


@login_required
def forum_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    reply_forms = {post.id: ForumReplyForm() for post in posts}
    context = {
        'posts': posts,
        'reply_forms': reply_forms,
        'now': timezone.now().strftime('%H:%M:%S')
    }
    return render(request, 'forum_list.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Пост успешно создан!')
            return redirect('forum_list')
    else:
        form = ForumPostForm()

    return render(request, 'create_post.html', {'form': form})


@login_required
def create_reply(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = ForumReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.author = request.user
            reply.save()
            messages.success(request, 'Ответ добавлен!')
    return redirect('forum_list')
