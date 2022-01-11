from django.urls import path
from user import views
from user.views import RegisterView, MyObtainTokenPairView, UserDetail, UserList, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('register', RegisterView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view())
]
