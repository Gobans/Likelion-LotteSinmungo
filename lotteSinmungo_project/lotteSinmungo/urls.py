"""lotteSinmungo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views
from django.conf.urls import url,include
import notifications.urls
# from app.funtion.rankReset import scheduler 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    
    path('solution/',views.solution, name = 'solution'),
    path('solutionDetail/<int:solution_detail_id>', views.solutionDetail, name = "solutionDetail"),

    path('problemList/',views.problemList, name = 'problemList'),
    path('problemDetail/<int:problem_detail_id>', views.problemDetail, name = "problemDetail"),

    path('writing/',views.writing, name = 'writing'),
    path('problemUpdate/<int:problem_detail_id>', views.problemUpdate,name='problemUpdate'),
    path('problemDelete/<int:problem_detail_id>', views.problemDelete,name='problemDelete'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('mypage/', views.mypage, name='mypage'),

    path('like/<int:problem_detail_key_id>', views.problem_like, name='problem_like'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
# scheduler.start()