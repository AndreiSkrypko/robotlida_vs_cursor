# 📝 Пример обновления шаблонов для использования SEO-данных

## Как обновить существующие шаблоны

Все ваши шаблоны страниц курсов нужно обновить, чтобы использовать SEO-данные из контекста.

---

## Пример для courses_2_4.html

### Было (старая версия):
```django
{% extends 'main/base.html' %}
{% load static %}

{% block title %}Курсы для детей 2-4 года{% endblock %}

{% block content %}
<!-- контент -->
{% endblock %}
```

### Стало (новая версия):
```django
{% extends 'main/base.html' %}
{% load static %}

{% block title %}{{ seo.title }}{% endblock %}
{% block meta_description %}{{ seo.meta_description }}{% endblock %}
{% block meta_keywords %}{{ seo.meta_keywords }}{% endblock %}

{% block og_title %}{{ seo.og_title }}{% endblock %}
{% block og_description %}{{ seo.og_description }}{% endblock %}

{% block canonical_url %}https://robotlida.by/courses_2_4/{% endblock %}

{% block breadcrumb_items %},
{
  "@type": "ListItem",
  "position": 2,
  "name": "{{ seo.breadcrumb_name }}",
  "item": "https://robotlida.by/courses_2_4/"
}
{% endblock %}

{% block structured_data %}
{{ block.super }}
<script type="application/ld+json">
{{ course_structured_data|safe }}
</script>
{% endblock %}

{% block content %}
<!-- контент остается без изменений -->
{% endblock %}
```

---

## Применить ко всем шаблонам курсов

### Список шаблонов для обновления:
1. `main/courses_2_4.html`
2. `main/courses_4_6.html`
3. `main/courses_6_7.html`
4. `main/courses_7_9.html`
5. `main/courses_9_11.html`
6. `main/courses_11_13.html`
7. `main/courses_13_16.html`
8. `main/courses_online.html`

### Для courses_online.html (без course_structured_data):
```django
{% extends 'main/base.html' %}
{% load static %}

{% block title %}{{ seo.title }}{% endblock %}
{% block meta_description %}{{ seo.meta_description }}{% endblock %}
{% block meta_keywords %}{{ seo.meta_keywords }}{% endblock %}

{% block og_title %}{{ seo.og_title }}{% endblock %}
{% block og_description %}{{ seo.og_description }}{% endblock %}

{% block breadcrumb_items %},
{
  "@type": "ListItem",
  "position": 2,
  "name": "{{ seo.breadcrumb_name }}",
  "item": "https://robotlida.by/courses_online/"
}
{% endblock %}

{% block content %}
<!-- контент -->
{% endblock %}
```

---

## Для index.html

```django
{% extends 'main/base.html' %}
{% load static %}

{% block title %}{{ seo.title }}{% endblock %}
{% block meta_description %}{{ seo.meta_description }}{% endblock %}
{% block meta_keywords %}{{ seo.meta_keywords }}{% endblock %}

{% block og_title %}{{ seo.og_title }}{% endblock %}
{% block og_description %}{{ seo.og_description }}{% endblock %}

{% block content %}
<!-- контент -->
{% endblock %}
```

---

## Для about.html

```django
{% extends 'main/base.html' %}
{% load static %}

{% block title %}{{ seo.title }}{% endblock %}
{% block meta_description %}{{ seo.meta_description }}{% endblock %}
{% block meta_keywords %}{{ seo.meta_keywords }}{% endblock %}

{% block og_title %}{{ seo.og_title }}{% endblock %}
{% block og_description %}{{ seo.og_description }}{% endblock %}

{% block breadcrumb_items %},
{
  "@type": "ListItem",
  "position": 2,
  "name": "{{ seo.breadcrumb_name }}",
  "item": "https://robotlida.by/about/"
}
{% endblock %}

{% block content %}
<!-- контент -->
{% endblock %}
```

---

## Проверка работы SEO

После обновления шаблонов проверьте:

### 1. Локально
```bash
python manage.py runserver
```

Откройте:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/courses_2_4/
- http://127.0.0.1:8000/about/

### 2. Проверьте HTML исходный код (Ctrl+U)
Должны быть:
- `<title>` с полным названием курса
- `<meta name="description">` с описанием
- `<meta name="keywords">` с ключевыми словами
- Open Graph теги
- JSON-LD структурированные данные

### 3. Валидация структурированных данных

После деплоя на сервер:
- https://search.google.com/test/rich-results
- https://validator.schema.org/

---

## Быстрая команда для обновления

Если нужно быстро добавить SEO блоки в начало всех шаблонов курсов:

```django
{% block title %}{{ seo.title }}{% endblock %}
{% block meta_description %}{{ seo.meta_description }}{% endblock %}
{% block meta_keywords %}{{ seo.meta_keywords }}{% endblock %}
{% block og_title %}{{ seo.og_title }}{% endblock %}
{% block og_description %}{{ seo.og_description }}{% endblock %}
{% block canonical_url %}https://robotlida.by{{ request.path }}{% endblock %}

{% block breadcrumb_items %},
{
  "@type": "ListItem",
  "position": 2,
  "name": "{{ seo.breadcrumb_name }}",
  "item": "https://robotlida.by{{ request.path }}"
}
{% endblock %}

{% block structured_data %}
{{ block.super }}
{% if course_structured_data %}
<script type="application/ld+json">
{{ course_structured_data|safe }}
</script>
{% endif %}
{% endblock %}
```

Добавьте этот блок после `{% load static %}` и перед `{% block content %}`.

---

## Важно!

После обновления шаблонов:
1. Перезапустите сервер Django
2. Очистите кэш браузера (Ctrl+Shift+Delete)
3. Проверьте все страницы
4. Убедитесь что формы продолжают работать
5. Протестируйте на разных устройствах

---

✅ После этого ваш сайт будет полностью оптимизирован для поисковых систем!

