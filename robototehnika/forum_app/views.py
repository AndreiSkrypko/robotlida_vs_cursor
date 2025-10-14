from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import ForumPost, ForumReply
from .forms import ForumPostForm, ForumReplyForm
from main_app.forms import SignForm


def forum_list(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    reply_forms = {post.id: ForumReplyForm() for post in posts}
    
    # Обработка формы записи на курсы
    if request.method == 'POST':
        sign_form = SignForm(request.POST)
        if sign_form.is_valid():
            sign_form.save()
            messages.success(request, 'Заявка успешно отправлена! Мы с вами свяжемся в ближайшее время.')
            # Возвращаем страницу с флагом успешной отправки
            context = {
                'posts': posts,
                'reply_forms': reply_forms,
                'form': SignForm(),  # Очищаем форму
                'success': True,  # Флаг успешной отправки
                'now': timezone.now().strftime('%H:%M:%S')
            }
            return render(request, 'forum_list.html', context)
        else:
            # Если форма невалидна, показываем ошибки
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        sign_form = SignForm()
    
    context = {
        'posts': posts,
        'reply_forms': reply_forms,
        'form': sign_form,  # Форма для модального окна записи
        'success': False,  # По умолчанию не успешно
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
