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
            'age': '2,5-4',
            'url': '/courses_2_4',
            'image': 'main/img/index/course1.png',
            'description': 'Первое знакомство с технологиями',
            'icon': 'bi-stars',
            'color': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'topics': ['Логика', 'Творчество', 'Моторика'],
        },
        {
            'title': 'детям 4-6 лет',
            'age': '4-6',
            'url': '/courses_4_6',
            'image': 'main/img/index/course2.png',
            'description': 'Основы конструирования и логики',
            'icon': 'bi-puzzle',
            'color': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            'topics': ['Конструирование', 'Алгоритмы', 'Игры'],
        },
        {
            'title': 'детям 6-7 лет',
            'age': '6-7',
            'url': '/courses_6_7',
            'image': 'main/img/index/course3.jpg',
            'description': 'Введение в программирование',
            'icon': 'bi-lightbulb',
            'color': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
            'topics': ['Scratch Jr', 'Робототехника', 'Логика'],
        },
        {
            'title': 'детям 7-9 лет',
            'age': '7-9',
            'url': '/courses_7_9',
            'image': 'main/img/index/course4.jpg',
            'description': 'Создание первых проектов',
            'icon': 'bi-code-square',
            'color': 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
            'topics': ['Scratch', 'Роботы', 'Анимация'],
        },
        {
            'title': 'детям 9-11 лет',
            'age': '9-11',
            'url': '/courses_9_11',
            'image': 'main/img/index/course5.jpeg',
            'description': 'Программирование и дизайн',
            'icon': 'bi-cpu',
            'color': 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
            'topics': ['Python', '3D', 'Веб-дизайн'],
        },
        {
            'title': 'детям 11-13 лет',
            'age': '11-13',
            'url': '/courses_11_13',
            'image': 'main/img/index/course6.jpeg',
            'description': 'Разработка игр и приложений',
            'icon': 'bi-controller',
            'color': 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)',
            'topics': ['Unity', 'Python', 'AI основы'],
        },
        {
            'title': 'детям 13-16 лет',
            'age': '13-16',
            'url': '/courses_13_16',
            'image': 'main/img/index/course7.jpg',
            'description': 'Профессиональное программирование',
            'icon': 'bi-laptop',
            'color': 'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)',
            'topics': ['Web Dev', 'Python Pro', 'Проекты'],
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