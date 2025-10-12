from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .forms import SignForm, ReviewForm
from .seo_data import get_seo_data, get_course_structured_data
import os
import json
from django.conf import settings


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

    # SEO данные для главной страницы
    seo_data = get_seo_data('index')
    
    return render(request, 'main/index.html', {
        'form': form,
        'success': success,
        'courses': courses,
        'seo': seo_data,
    })



def about(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            seo_data = get_seo_data('about')
            return render(request, 'main/about.html', {
                'form': SignForm(),  # очистка формы
                'success': True,  # флаг успешной отправки
                'seo': seo_data,
            })
    else:
        form = SignForm()

    seo_data = get_seo_data('about')
    return render(request, 'main/about.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
    })

def courses_online(request):
    seo_data = get_seo_data('courses_online')
    if request.method == 'GET':
        return render(request, 'main/courses_online.html', {'seo': seo_data})


def courses_2_4(request):
    seo_data = get_seo_data('courses_2_4')
    
    # Структурированные данные для курса
    course_structured_data = get_course_structured_data(
        course_name='Робототехника для детей 2,5-4 года',
        age_range='2.5-4 года',
        description='Первое знакомство с технологиями для самых маленьких. Развитие логики, моторики и творческих способностей.',
        topics=['Логика', 'Творчество', 'Моторика', 'Конструирование']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_2_4.html', {
                'form': SignForm(),  # очистка формы
                'success': True,  # флаг успешной отправки
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_2_4.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })

def courses_4_6(request):
    seo_data = get_seo_data('courses_4_6')
    
    course_structured_data = get_course_structured_data(
        course_name='Робототехника для детей 4-6 лет',
        age_range='4-6 лет',
        description='Основы конструирования и логики. LEGO Education, развитие алгоритмического мышления.',
        topics=['Конструирование', 'Алгоритмы', 'LEGO Education', 'Логика']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/courses_4_6.html', {
                'form': SignForm(),
                'success': True,
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_4_6.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })

def courses_6_7(request):
    seo_data = get_seo_data('courses_6_7')
    
    course_structured_data = get_course_structured_data(
        course_name='Программирование Scratch Jr для детей 6-7 лет',
        age_range='6-7 лет',
        description='Введение в программирование через Scratch Jr. Создание первых игр и анимаций.',
        topics=['Scratch Jr', 'Робототехника', 'Логика', 'Создание игр']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/courses_6_7.html', {
                'form': SignForm(),
                'success': True,
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_6_7.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })


def courses_7_9(request):
    seo_data = get_seo_data('courses_7_9')
    
    course_structured_data = get_course_structured_data(
        course_name='Scratch программирование для детей 7-9 лет',
        age_range='7-9 лет',
        description='Создание игр и анимации на Scratch. Робототехника WeDo. Развитие творческого мышления.',
        topics=['Scratch', 'Создание игр', 'Анимация', 'WeDo робототехника']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/courses_7_9.html', {
                'form': SignForm(),
                'success': True,
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_7_9.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })


def courses_9_11(request):
    seo_data = get_seo_data('courses_9_11')
    
    course_structured_data = get_course_structured_data(
        course_name='Python и 3D моделирование для детей 9-11 лет',
        age_range='9-11 лет',
        description='Изучение Python - настоящего языка программирования. 3D моделирование и веб-дизайн.',
        topics=['Python', '3D моделирование', 'Веб-дизайн', 'Программирование']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/courses_9_11.html', {
                'form': SignForm(),
                'success': True,
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_9_11.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })


def courses_11_13(request):
    seo_data = get_seo_data('courses_11_13')
    
    course_structured_data = get_course_structured_data(
        course_name='Unity и Python для подростков 11-13 лет',
        age_range='11-13 лет',
        description='Разработка 2D и 3D игр на Unity. Python программирование и основы искусственного интеллекта.',
        topics=['Unity', 'Python', 'Разработка игр', 'AI основы', 'Game Development']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/courses_11_13.html', {
                'form': SignForm(),
                'success': True,
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_11_13.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })

def courses_13_16(request):
    seo_data = get_seo_data('courses_13_16')
    
    course_structured_data = get_course_structured_data(
        course_name='Веб-разработка и Python Pro для подростков 13-16 лет',
        age_range='13-16 лет',
        description='Профессиональная веб-разработка: HTML, CSS, JavaScript, Python Django. Создание реальных проектов.',
        topics=['HTML', 'CSS', 'JavaScript', 'Python Django', 'Веб-разработка', 'Frontend', 'Backend']
    )
    
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/courses_13_16.html', {
                'form': SignForm(),
                'success': True,
                'seo': seo_data,
                'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_13_16.html', {
        'form': form,
        'success': False,
        'seo': seo_data,
        'course_structured_data': json.dumps(course_structured_data, ensure_ascii=False),
    })


def about_cookies(request):
    seo_data = get_seo_data('about_cookies')
    return render(request, 'main/about_cookies.html', {'seo': seo_data})


@require_GET
def robots_txt(request):
    """
    Отдает robots.txt для поисковых систем
    Оптимизирован для максимальной индексации
    """
    lines = [
        "# Robots.txt для IT Клуб Юные Инженеры",
        "# https://robotlida.by",
        "",
        "# Разрешаем индексацию всем поисковым системам",
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /login/",
        "Disallow: /forum_list/",
        "Allow: /",
        "Allow: /static/",
        "",
        "# Специальные правила для Яндекса",
        "User-agent: Yandex",
        "Disallow: /admin/",
        "Disallow: /login/",
        "Allow: /",
        "Crawl-delay: 1",
        "",
        "# Специальные правила для Google",
        "User-agent: Googlebot",
        "Disallow: /admin/",
        "Disallow: /login/",
        "Allow: /",
        "",
        "# Карта сайта",
        "Sitemap: https://robotlida.by/sitemap.xml",
        "",
        "# Хост сайта (для Яндекса)",
        "Host: https://robotlida.by",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")