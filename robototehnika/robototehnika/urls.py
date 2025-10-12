from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main_app.views import robots_txt


urlpatterns = [
                  path('admin/', admin.site.urls),  # путь при входе в панель администратора
                  path('', include('main_app.urls')),
                  # путь на главную страницу, urls сделан в главном приложении main_app
                  path('', include('forum_app.urls')),
                  path('login/', include('login_app.urls')),
                  path('robots.txt', robots_txt, name='robots_txt'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
