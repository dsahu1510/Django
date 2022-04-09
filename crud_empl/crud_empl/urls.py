"""crud_empl URL Configuration

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
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/<int:id>',views.home_emp),
    path('', views.createemp),
    path('show', views.showemp),
    path('edit/<int:id>', views.editemp),
    path('update/<int:id>', views.updateemp),
    path('delete/<int:id>', views.deleteemp),
    # path('search/<int:id>', views.search_emp),
  
]