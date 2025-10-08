from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView



urlpatterns = [
                  path('admin/', admin.site.urls),  # путь при входе в панель администратора
                  path('', include('main_app.urls')),
                  # путь на главную страницу, urls сделан в главном приложении main_app
                  path('', include('forum_app.urls')),
                  path('login/', include('login_app.urls')),
                  path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
