from .views import QuizView, RegisterUser, QuizCategoryView, QuizOptionView, VerifyOTP
from django.urls import path
from rest_framework.authtoken import views
# from . import views

urlpatterns = [
    path('', QuizView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', RegisterUser.as_view()),
    path('quiz-category/', QuizCategoryView.as_view()),
    path('quiz-option/', QuizOptionView.as_view()),
    path('verify-otp/', VerifyOTP.as_view()),
]