from django.shortcuts import render, redirect
from .forms import SignForm, ReviewForm


def index(request):
    success = False
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = SignForm()
    else:
        form = SignForm()

    courses = [
        {
            'title': 'детям 2,5-4 года',
            'url': '/courses_2_4',
            'image': 'main/img/index/course1.png',
        },
        {
            'title': 'детям 4-6 лет',
            'url': '/courses_4_6',
            'image': 'main/img/index/course2.png',
        },
        {
            'title': 'детям 6-7 лет',
            'url': '/courses_6_7',
            'image': 'main/img/index/course3.jpg',
        },
        {
            'title': 'детям 7-9 лет',
            'url': '/courses_7_9',
            'image': 'main/img/index/course4.jpg',
        },
        {
            'title': 'детям 9-11 лет',
            'url': '/courses_9_11',
            'image': 'main/img/index/course5.jpeg',
        },
        {
            'title': 'детям 11-13 лет',
            'url': '/courses_11_13',
            'image': 'main/img/index/course6.jpeg',
        },
        {
            'title': 'детям 13-16 лет',
            'url': '/courses_13_16',
            'image': 'main/img/index/course7.jpg',
        },
    ]

    return render(request, 'main/index.html', {
        'form': form,
        'success': success,
        'courses': courses,
    })



def about(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/about.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/about.html', {
        'form': form,
        'success': False
    })

def courses_online(request):
    if request.method == 'GET':
        return render(request,'main/courses_online.html')


def courses_2_4(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_2_4.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_2_4.html', {
        'form': form,
        'success': False
    })

def courses_4_6(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_4_6.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_4_6.html', {
        'form': form,
        'success': False
    })

def courses_6_7(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_6_7.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_6_7.html', {
        'form': form,
        'success': False
    })


def courses_7_9(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_7_9.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_7_9.html', {
        'form': form,
        'success': False
    })


def courses_9_11(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_9_11.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_9_11.html', {
        'form': form,
        'success': False
    })


def courses_11_13(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_11_13.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_11_13.html', {
        'form': form,
        'success': False
    })

def courses_13_16(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_13_16.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_13_16.html', {
        'form': form,
        'success': False
    })


def about_cookies(request):
    return render(request, 'main/about_cookies.html')