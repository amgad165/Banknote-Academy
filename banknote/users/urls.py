from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import PasswordChangeView
app_name = 'users'

urlpatterns = [
    path('login/',views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('edit/<int:pk>/', views.UpdateUser.as_view(), name="edit"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="change_password.html"), name="password_change"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('application/',views.MyApplicationList,name='myapplication_list'),
    path('<int:pk>/remove/',views.MyApplicationDeleteView.as_view(), name='remove'),

    ]
