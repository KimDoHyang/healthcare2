from django.urls import path
from . import apis

urlpatterns_api_members = [
    path('login/', apis.AuthTokenView.as_view()),
    path('signup/', apis.SignupView.as_view()),
    path('social/', apis.SocialAuthTokenView.as_view()),
    path('verification/', apis.PhoneNumberVerificationView.as_view()),
    path('checkID/', apis.CheckUniqueIDView.as_view()),
    path('logout/', apis.LogoutView.as_view()),
    path('profile/', apis.UserInfoView.as_view())
]

