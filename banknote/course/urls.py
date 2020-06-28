from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('create/', views.CourseCreate.as_view(), name="create"),

    path('create/success/',views.SuccessPage.as_view(), name="success"),
    path('course/<int:pk>/', views.CourseDetails.as_view(), name="details"),
    path('addtrainercourse/', views.add_trainer_to_course, name="add_trainer_to_course"),
    path('course/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='edit'),
    path('course/<int:pk>/remove/', views.CourseDeleteView.as_view(), name='remove'),
    path('course/<int:pk>/addquestioncourse/', views.add_question_to_course, name="add_question_to_course"),

    ]
