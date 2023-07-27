from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/', views.StudentView.as_view()),
    path('api-url/', views.StudentView.as_view()),
    path('api/<int:pk>/', views.StudentView.as_view()),
    path('api-post/', views.StudentView.as_view()),
    path('api-put/<int:pk>/', views.StudentView.as_view()),
    path('api-patch/<int:pk>/', views.StudentView.as_view()),
    path('api-delete/<int:pk>/', views.StudentView.as_view()),

    path('api-uni/', views.UniversityView.as_view()),
    path('api-uni/<int:pk>/', views.UniversityView.as_view()),
    path('api-post-uni/', views.UniversityView.as_view()),
    path('api-put-uni/<int:pk>/', views.UniversityView.as_view()),
    path('api-patch-uni/<int:pk>/', views.UniversityView.as_view()),
    path('api-delete-uni/<int:pk>/', views.UniversityView.as_view()),

    path('api-teach/', views.TeacherView.as_view()),
    path('api-teach/<int:pk>/', views.TeacherView.as_view()),
    path('api-post-teach/', views.TeacherView.as_view()),
    path('api-put-teach/<int:pk>/', views.TeacherView.as_view()),
    path('api-patch-teach/<int:pk>/', views.TeacherView.as_view()),
    path('api-delete-teach/<int:pk>/', views.TeacherView.as_view()),

    path('api-song/', views.SongView.as_view()),
    path('api-song/<int:pk>/', views.SongView.as_view()),
    path('api-post-song/', views.SongView.as_view()),
    path('api-put-song/<int:pk>/', views.SongView.as_view()),
    path('api-patch-song/<int:pk>/', views.SongView.as_view()),
    path('api-delete-song/<int:pk>/', views.SongView.as_view()),

    path('api-profile/', views.StudentProfileView.as_view()),
    path('api-profile/<int:pk>/', views.StudentProfileView.as_view()),
    path('api-post-profile/', views.StudentProfileView.as_view()),
    path('api-put-profile/<int:pk>/', views.StudentProfileView.as_view()),
    path('api-patch-profile/<int:pk>/', views.StudentProfileView.as_view()),
    path('api-delete-profile/<int:pk>/', views.StudentProfileView.as_view()),
    # api end point generating token
    # path('token/', obtain_auth_token),
    # custimzed token we make auth.py file and write code for returning email user password
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
