"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from home import views as views_home
from news import views as views_news

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views_home.home, name='home'),
    path('news/', views_news.news, name='news'),
    path('news/<int:article_id>/', views_news.article_detail, name='article_detail'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    # path('register/', views_users.register, name='register'),
    # path('login/', views_users.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
