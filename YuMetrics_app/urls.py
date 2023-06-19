from django.urls import path
from .views import *

urlpatterns = [
    path('metrics/', MetricAPIView.as_view()),
    path('metrics/quiz_package/', QuizPackageView.as_view()),
    
    path('mistakes/', MistakeAPIView.as_view()),
    path('mistakes/create/', MistakeCreateView.as_view()),
    path('mistakes/delete/', MistakeDeleteView.as_view()),

    path('results/create/', ResultCreateView.as_view()),
    path('results/day_top/', DayTopAPIView.as_view()),
    path('results/week_top/', WeekTopAPIView.as_view()),
    path('results/month_top/', MonthTopAPIView.as_view()),
]
