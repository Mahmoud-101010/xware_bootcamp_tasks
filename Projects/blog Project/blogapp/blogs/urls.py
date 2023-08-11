from django.urls import path
from blogs.views import *
from . import views

urlpatterns = [
    path('homepage/' , views.homepage , name="homepage"),

    path('login/', views.login_page, name="login"),

    path('upload_blog/', views.upload_blog, name="upload_blog"),
    
    path('signup/', views.signup , name="signup"),

    path('logout/', views.logout_page , name="logout"),

    path('show_blog/', views.show_blog , name="show_blog"),

    path('change/<int:blog_id>/', views.change, name='change'),

    path('delete/<int:blog_id>/', views.delete, name='delete'),

    path('update/<int:blog_id>/', views.update, name='update')
    
]
