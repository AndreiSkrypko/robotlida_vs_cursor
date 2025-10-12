from django.db import migrations


def set_site_domain(apps, schema_editor):
    """Устанавливает правильный домен для сайта"""
    try:
        Site = apps.get_model('sites', 'Site')
        site = Site.objects.get(id=1)
        site.domain = 'robotlida.by'
        site.name = 'Робот Лида - Робототехника для детей'
        site.save()
    except Site.DoesNotExist:
        # Если сайта нет, создаем
        Site.objects.create(
            id=1,
            domain='robotlida.by',
            name='Робот Лида - Робототехника для детей'
        )


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_review_delete_reviews_alter_course_options_and_more'),
        ('sites', '0002_alter_domain_unique'),  # Зависимость от sites
    ]

    operations = [
        migrations.RunPython(set_site_domain),
    ]

