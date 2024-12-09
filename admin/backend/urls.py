from django.urls import path
from . import views

urlpatterns = [
    path('Register', views.studentRegistration),
    path('Login', views.studentLogin),
    path('CreatePost', views.createPost),
    path('PasswordModify', views.modifyPassword),
    path('DeletePost', views.deletePost),
    path('Comment', views.createFirstLayerComment),
    path('SecondComment', views.createSecondLayerComment),
    path('EmailModify', views.modifyEmail),
    path('UsernameModify', views.modifyUserName),
    path('AvaterModify', views.modifyPicture),
    path('BioModify', views.modifyIntroduction),
    path('GetAllPost', views.getPostBriefInfo),
    path('GetSinglePost', views.getPostAllInfo),
    path('GetAllReplies', views.getPostAllInfo),
    path('GetPersonPost', views.getUserPost),
    path('GetUsers', views.getTopThreeUserInfo),
    path('GetUserAvatar', views.getUserAvatar),
]