from django.urls import path
from . import views

app_name = 'trainer'

urlpatterns = [
    path('create/',views.TrainerCreate.as_view(), name="create"),
    path('success/',views.SuccessPage.as_view(), name="success"),
    # path('trainer/<int:pk>/', views.TrainerDetails.as_view(), name="details"),
    path('trainer_list/',views.TrainerListView.as_view(),name='trainer_list'),
    path('trainer/<int:pk>/edit/', views.TrainerUpdateView.as_view(), name='edit'),
    path('trainer/<int:pk>/remove/', views.TrainerDeleteView.as_view(), name='remove'),
    path('trainer/<int:pk>/details',views.TrainerDetailView.as_view(),name='details'),

    ]
