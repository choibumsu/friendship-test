from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_home, name="quiz_home"),
    path('create/<int:pk>', views.quiz_create, name="quiz_create"),
    path('complete/<int:pk>', views.quiz_complete, name="quiz_complete"),

    path('<int:quiz_url>', views.solve_home, name="solve_home"),
    path('solve/<int:pk>', views.solve_quiz, name="solve_quiz"),
    path('result/<int:pk>', views.solve_result, name="solve_result"),
]
