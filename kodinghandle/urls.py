"""kodinghandle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = "Koding Handle | Admin"
admin.site.site_title = "Koding Handle | Admin"
admin.site.index_title = "Koding Handle | Admin"

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('api/blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/users/', include('user.urls')),
    path('api/comments/', include('comment.urls')),
    path('api/contact/', include('contact.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
