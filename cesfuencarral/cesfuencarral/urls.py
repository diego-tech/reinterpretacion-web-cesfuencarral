"""cesfuencarral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),

    # Path de noticias
    path('noticias/', include('noticias.urls')),

    # Path de Contact
    path('contact/', include('contact.urls')),

    # Path de Campus
    path('campus/', include('campus.urls')),

    # Path de Pages
    path('pages/', include(pages_patterns)),

    # Path de Registration
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    # Path de profiles
    path('profiles/', include(profiles_patterns)),

    # Path de Messenger
    path('messenger/', include(messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
