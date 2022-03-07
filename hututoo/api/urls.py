
from unicodedata import name
from .views import EventView, EventCategoryView, EventOptionView, UserRegister, VerifyOTP, LoginUser, UserProfileView, TransactionView, PredictView
from django.urls import path
# from . import views

urlpatterns = [
    path('events/', EventView.as_view()),
    path('event-category/', EventCategoryView.as_view()),
    path('event-option/', EventOptionView.as_view()),
    path('register/', UserRegister.as_view()),
    path('verify-otp/', VerifyOTP.as_view()),
    path('login/', LoginUser.as_view(), name='login'),
    path('user-profile/<str:user>/', UserProfileView.as_view()),
    path('transaction/<str:user>/', TransactionView.as_view()),
    path('predict/<str:user>/<int:event_id>/', PredictView.as_view()),
    # path('predict/', views.predict, name='predict'),
]