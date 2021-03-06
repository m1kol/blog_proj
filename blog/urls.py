"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings

import categories.urls
import post.urls
import core.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include(categories.urls, namespace='categories')),
    path('posts/', include(post.urls, namespace='post')),
    path('', include(core.urls, namespace='core')),
]

# code for a django debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('debug/', include(debug_toolbar.urls)),
    ] + urlpatterns
