from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # 홈 페이지 설정
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('history/', views.SearchHistoryView.as_view(), name='search_history'),
]
