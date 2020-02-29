from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.question, name='question' ),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout' ),
    path('register/', views.register, name='register'),
    path('post_question/', views.post_question, name='post_question'),
    
    path('<slug>/', views.question_detail, name='question_detail'),
    path('answer/<slug>/', views.answer, name='answer'),


]
