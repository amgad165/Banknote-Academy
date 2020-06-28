from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [

    path('application/<int:pk>',views.application, name="application"),
    path('application/applicants',views.ApplicationList.as_view(), name="applicants_list"),
    path('<int:pk>/remove/',views.ApplicationDeleteView.as_view(), name='remove'),
    path('already/', views.AlreadyEnrolled.as_view(), name="already"),
    path('<int:pk>/detail/',views.ApplicationDetails.as_view(), name='detail'),
    path('<int:pk>/apply/', views.ApplicationApply,name="apply"),
    path('application/accepted',views.AcceptedList.as_view(), name="accepted_list"),
    path('mail',views.EmailView.as_view(), name="email_sent"),

    ]
