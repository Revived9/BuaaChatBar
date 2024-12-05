import code
import random
import os
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.utils import json
from rest_framework.views import APIView
from .models import *
from datetime import datetime
from django.db.models import F
# Create your views here.


def home(request):
    return HttpResponse("Hello, World!")


def generate_unique_user_id():
    while True:
        user_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not User.objects.filter(user_id=user_id).exists():
            return user_id


def generate_unique_post_id():
    while True:
        post_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not Post.objects.filter(post_id=post_id).exists():
            return post_id


def generate_unique_picture_id():
    while True:
        PC_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not Picture.objects.filter(PC_id=PC_id).exists():
            return PC_id

def generate_unique_firstlayercomment_id():
    while True:
        FLC_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not FirstLayerComment.objects.filter(FLC_id=FLC_id).exists():
            return FLC_id


def generate_unique_secondlayercomment_id():
    while True:
        SLC_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not SecondLayerComment.objects.filter(SLC_id=SLC_id).exists():
            return SLC_id

def generate_unique_collectpost_id():
    while True:
        CP_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not CollectPost.objects.filter(CP_id=CP_id).exists():
            return CP_id

def generate_unique_label_id():
    while True:
        LB_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not Label.objects.filter(LB_id=LB_id).exists():
            return LB_id

def generate_unique_postandlabel_id():
    while True:
        PL_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not PostAndLabels.objects.filter(PL_id=PL_id).exists():
            return PL_id

def generate_unique_postpicture_id():
    while True:
        PP_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not PostPicture.objects.filter(PP_id=PP_id).exists():
            return PP_id

def generate_unique_inform_id():
    while True:
        IF_id = random.randint(1000000000, 9999999999)  # 生成一个10位的随机数
        if not Inform.objects.filter(IF_id=IF_id).exists():
            return IF_id
@csrf_exempt
def studentRegistration(request):
    res = {"code": 1, "message": "", "data": None,"id": -1}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = generate_unique_user_id()
            user_name = data.get("username")
            user_password = data.get("password")
            user_email = data.get("email")
            user_student_id = data.get("student_id")
            user_experience = 0
            user_sign_date = datetime.now().date()
            user_birthday = datetime(2024, 1, 1)
            # 头像上传状态先默认为0
            user_uploaded = 0
            # 用户状态先默认为0
            user_role = 0
            user_post_cnt = 0
            user_info_cnt = 0
            user_introduction = "快来填写简介吧"
            # hash存储密码更安全
            user = User(user_id=user_id, user_name=user_name, user_password=make_password(user_password), user_email=user_email,
                        user_student_id=user_student_id, user_experience=user_experience,
                        user_sign_date=user_sign_date, user_birthday=user_birthday, user_uploaded=user_uploaded,
                        user_role=user_role,
                        user_post_cnt=user_post_cnt, user_info_cnt=user_info_cnt,user_introduction=user_introduction)
            PC_id = generate_unique_picture_id()
            # 默认路径
            PC_path = "https://img0.baidu.com/it/u=1864154549,3150614661&fm=253&fmt=auto&app=138&f=JPEG?w=285&h=285"
            # 图片种类默认为0
            PC_category = 0
            PC_author_id = user
            picture = Picture(PC_id = PC_id, PC_path = PC_path, PC_author_id = PC_author_id, PC_category = PC_category)
            if User.objects.filter(user_student_id = user_student_id).exists():
                res["code"] = -1
                res["message"] = "学号已被注册"
            else:
                res["code"] = 1
                res["message"] = "注册成功"
                res["id"] = user_id
                user.save()
                picture.save()
        except Exception as e:
            res["code"] = -1
            res["message"] = "服务器错误：用户创建失败" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def studentLogin(request):
    res = {"code": 1, "message": "", "data": None,"id": -1,"path": None,"username": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_student_id = data.get("student_id")
            user_password = data.get("password")
            if User.objects.filter(user_student_id=user_student_id).exists():
                # 进行hash比较登录更加安全
                if check_password(user_password, User.objects.get(user_student_id=user_student_id).user_password):
                    res["code"] = 1
                    res["message"] = "登陆成功"
                    user = User.objects.get(user_student_id=user_student_id)
                    picture = Picture.objects.get(PC_author_id = user)
                    res["id"] = user.user_id
                    res["username"] = user.user_name
                    res["path"] = picture.PC_path
                else:
                    res["code"] = -1
                    res["message"] = "登陆失败，密码不正确"
            else:
                res["code"] = -1
                res["message"] = "登录失败，不存在这个学号的用户"
        except Exception as e:
            res["code"] = -1
            res["message"] = "服务器错误：用户创建失败" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def createPost(request):
    res = {"code": 1, "message": "", "data": None, "heat": 1,"id": -1,"created_at": datetime.now().date()}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            post_id = generate_unique_post_id()
            post_title = data.get("title")
            post_content = data.get("content")
            post_user_id = data.get("user_id")
            post_images = data.get("images")

            post_label = 'aaa'
            post_isTop = False
            user = User.objects.get(user_student_id=post_user_id)
            LB_tag_name = data.get("section")
            if Label.objects.filter(LB_tag_name=LB_tag_name).exists():
                label = Label.objects.get(LB_tag_name=LB_tag_name)
            else:
                LB_id = generate_unique_label_id()
                label = Label(LB_tag_name=LB_tag_name, LB_id = LB_id)
                label.save()
            post_heat = 1
            res["heat"] = post_heat
            post_time = datetime.now().date()

            post = Post(post_id=post_id, post_title=post_title, post_content=post_content, post_tag_id = label,
                        post_heat = post_heat, post_time = post_time,post_user_id = user, post_isTop = post_isTop,
                        post_label = post_label)
            post.save()
            for image in post_images:
                PP_id = generate_unique_postpicture_id()
                PP_path = image
                PP_post_id = post
                postpicture = PostPicture(PP_id=PP_id, PP_path=PP_path, PP_post_id=PP_post_id)
                postpicture.save()

            PL_id = generate_unique_postandlabel_id()
            PL_tag_id = label
            PL_post_id = post
            postandlabel = PostAndLabels(PL_id=PL_id, PL_tag_id=PL_tag_id, PL_post_id=PL_post_id)
            postandlabel.save()
            # 用户帖子数+1
            user.user_post_cnt = user.user_post_cnt + 1
            # 经验+3
            user.user_experience = user.user_experience + 3
            user.save()
            res["code"] = 1
            res["message"] = "成功创建帖子"
            res["id"] = post_id
            res["created_at"] = post_time
        except Exception as e:
            res["code"] = -1
            res["message"] = "服务器错误：用户创建失败" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def modifyPassword(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get("user_id")
            old_password = data.get("old_password")
            new_password = data.get("new_password")
            user = User.objects.get(user_student_id = user_id)
            if check_password(old_password, user.user_password):
                user.user_password = make_password(new_password)
                user.save()
                res["code"] = 1
                res["message"] = "修改成功"
            else:
                res["code"] = -1
                res["message"] = "修改失败，旧密码错误"
        except Exception as e:
            res["code"] = -1
            res["message"] = "服务器错误：用户创建失败" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def deletePost(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get("user_id")
            post_id = data.get("post_id")
            post = Post.objects.get(post_id=post_id)
            user = User.objects.get(user_student_id = user_id)
            if post.post_user_id == user_id:
                user.user_post_cnt = user.user_post_cnt - 1
                user.save()
                post.delete()
                res["code"] = 1
                res["message"] = "帖子删除成功"
            else:
                res["code"] = -1
                res["message"] = "帖子删除失败，发帖用户不对"
        except Exception as e:
            res["code"] = -1
            res["message"] = "帖子删除失败,帖子id不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)



@csrf_exempt
def createFirstLayerComment(request):
    res = {"code": 1, "message": "", "data": None,"comment_id": -1,"created_at": datetime.now().date(),"heat": 1,"path": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            content = data.get("content")
            user_id = data.get("user_id")
            post_id = data.get("post_id")
            user = User.objects.get(user_student_id = user_id)
            post = Post.objects.get(post_id=post_id)
            receiver = post.post_user_id
            IF_id = generate_unique_inform_id()
            IF_content = "你有新的消息"
            IF_receiver_id = receiver
            IF_sender_id = user
            inform = Inform(IF_id = IF_id,IF_content = IF_content,IF_receiver_id = IF_receiver_id,IF_sender_id = IF_sender_id)
            inform.save()
            FLC_id = generate_unique_picture_id()
            FLC_time = datetime.now().date()
            FLC_content = content
            FLC_post_id = post
            FLC_author_id = user
            # 经验+3
            user.user_experience = user.user_experience + 3
            user.save()
            # 帖子热度+1
            post.post_heat = post.post_heat + 1
            post.save()
            firstlayercomment = FirstLayerComment(FLC_id = FLC_id, FLC_time = FLC_time, FLC_content = FLC_content, FLC_post_id = FLC_post_id
                                                  , FLC_author_id = FLC_author_id)
            firstlayercomment.save()
            res["code"] = 1
            res["message"] = "成功发表一级评论"
            res["comment_id"] = FLC_id
            res["created_at"] = FLC_time
            res["heat"] = post.post_heat
            res["path"] = Picture.objects.get(PC_author_id = user).PC_path
        except Exception as e:
            res["code"] = -1
            res["message"] = "发布评论失败，该用户不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def createSecondLayerComment(request):
    res = {"code": 1, "message": "", "data": None, "comment_id": -1,"created_at": datetime.now().date(), "path": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            content = data.get("content")
            comment_id = data.get("comment_id")
            post_id = data.get("post_id")
            user_id = data.get("user_id")
            flc = FirstLayerComment.objects.get(FLC_id = comment_id)
            user = User.objects.get(user_student_id = user_id)
            post = Post.objects.get(post_id=post_id)
            receiver = User.objects.get(user_id=post.post_user_id)
            IF_id = generate_unique_inform_id()
            IF_content = "你有新的消息"
            IF_receiver_id = receiver
            IF_sender_id = user
            inform = Inform(IF_id=IF_id, IF_content=IF_content, IF_receiver_id=IF_receiver_id,
                            IF_sender_id=IF_sender_id)
            inform.save()
            SLC_id = generate_unique_secondlayercomment_id()
            SLC_author_id = user
            SLC_comment_id = flc
            SLC_content = content
            SLC_time = datetime.now().date()
            # 经验+3
            user.user_experience = user.user_experience + 3
            user.save()
            # 帖子热度+1
            post.post_heat = post.post_heat + 1
            post.save()
            secondlayercomment = SecondLayerComment(SLC_id = SLC_id, SLC_author_id = SLC_author_id,SLC_comment_id = SLC_comment_id,
                                                    SLC_content = SLC_content, SLC_time = SLC_time)
            secondlayercomment.save()
            res["code"] = 1
            res["message"] = "成功发表二级评论"
            res["comment_id"] = SLC_id
            res["created_at"] = SLC_time
            res["path"] = Picture.objects.get(PC_author_id = user).PC_path
        except Exception as e:
            res["code"] = -1
            res["message"] = "发布评论失败，该用户不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def modifyEmail(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get("user_id")
            newEmail = data.get("newEmail")
            user = User.objects.get(user_student_id = user_id)
            user.user_email = newEmail
            user.save()
            res["code"] = 1
            res["message"] = "修改邮件成功"
        except Exception as e:
            res["code"] = -1
            res["message"] = "修改邮件失败，用户id不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def modifyUserName(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get("user_id")
            newUsername = data.get("newUsername")
            user = User.objects.get(user_student_id = user_id)
            user.user_name = newUsername
            user.save()
            res["code"] = 1
            res["message"] = "修改用户名成功"
        except Exception as e:
            res["code"] = -1
            res["message"] = "修改邮件失败，用户id不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def modifyIntroduction(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get("user_id")
            new_bio = data.get("new_bio")
            user = User.objects.get(user_student_id = user_id)
            user.user_introduction = new_bio
            user.save()
            res["code"] = 1
            res["message"] = "修改简介成功"
        except Exception as e:
            res["code"] = -1
            res["message"] = "修改邮件失败，用户id不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def modifyPicture(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data.get("user_id")
            new_avater = data.get("new_avatar")
            user = User.objects.get(user_student_id = user_id)
            picture = Picture.objects.get(PC_author_id = user, PC_category = 0)
            picture.PC_path = new_avater
            picture.save()
            res["code"] = 1
            res["message"] = "修改头像成功"
        except Exception as e:
            res["code"] = -1
            res["message"] = "修改邮件失败，用户id不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)


@csrf_exempt
def getPostBriefInfo(request):
    res = {"code": 1, "message": "", "data": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            part = data.get("section")
            sort = data.get("sort")
            if part == "all":
                if sort == "new":
                    posts = Post.objects.order_by("-post_time").values('post_id', 'post_title', 'post_heat',
                                                                       'post_time', 'post_user_id')
                    post_list = list(posts)
                    for post in post_list:
                        post_user_id = post['post_user_id']
                        post['username'] = User.objects.get(user_id=post_user_id).user_name
                        post['avatar'] = Picture.objects.get(PC_author_id=post_user_id).PC_path
                    res["data"] = post_list
                else:
                    posts = Post.objects.order_by("-post_heat").values('post_id', 'post_title', 'post_heat',
                                                                       'post_time', 'post_user_id')
                    post_list = list(posts)
                    for post in post_list:
                        post_user_id = post['post_user_id']
                        post['username'] = User.objects.get(user_id=post_user_id).user_name
                        post['avatar'] = Picture.objects.get(PC_author_id=post_user_id).PC_path
                    res["data"] = post_list
            else:
                if sort == "new":
                    posts = Post.objects.order_by("-post_time").values('post_id', 'post_title', 'post_heat',
                                                                       'post_time', 'post_user_id', 'post_tag_id')
                    post_list = []
                    for post in posts:
                        post_user_id = post['post_user_id']
                        post['username'] = User.objects.get(user_id=post_user_id).user_name
                        post['avatar'] = Picture.objects.get(PC_author_id=post_user_id).PC_path
                        LB_id = post['post_tag_id']
                        if Label.objects.get(LB_id=LB_id).LB_tag_name == part:
                            post_list.append(post)
                    res["data"] = post_list
                else:
                    posts = Post.objects.order_by("-post_heat").values('post_id', 'post_title', 'post_heat',
                                                                       'post_time', 'post_user_id', 'post_tag_id')
                    post_list = []
                    for post in posts:
                        post_user_id = post['post_user_id']
                        post['username'] = User.objects.get(user_id=post_user_id).user_name
                        post['avatar'] = Picture.objects.get(PC_author_id=post_user_id).PC_path
                        LB_id = post['post_tag_id']
                        if Label.objects.get(LB_id=LB_id).LB_tag_name == part:
                            post_list.append(post)
                    res["data"] = post_list
        except Exception as e:
            res["code"] = -1
            res["message"] = "获取帖子简要信息失败" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    print("!!")
    print(res["data"])
    return JsonResponse(res)


@csrf_exempt
def getPostAllInfo(request):
    res = {"code": 1, "message": "", "data": None,"content": None,"post_title": None,"heat":None,"post_time":None,"username":None,"avatar":None
           ,"section": None,"user_id": None,"picture":None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            post_id = data.get("post_id")
            post = Post.objects.get(post_id=post_id)
            user = post.post_user_id
            picture = Picture.objects.get(PC_author_id=user)
            label = post.post_tag_id
            res["code"] = 1
            res["content"] = post.post_content
            res["post_title"] = post.post_title
            res["heat"] = post.post_heat
            res["post_time"] = post.post_time
            res["username"] = user.user_name
            res["user_id"] = user.user_id
            res["avatar"] = picture.PC_path
            res["section"] = label.LB_tag_name
            pictureBack = PostPicture.objects.filter(PP_post_id = post).values('PP_path')
            pictureBackList = list(pictureBack)
            for picture1 in pictureBackList:
                picture1['path'] = picture1['PP_path']
            res["picture"] = pictureBackList
            comment_list = FirstLayerComment.objects.filter(FLC_post_id = post).values('FLC_id','FLC_content','FLC_time','FLC_author_id')
            comment_list1 = list(comment_list)
            print("!!")
            print(len(comment_list1))
            for comment in comment_list1:
                comment['id'] = comment['FLC_id']
                comment['content'] = comment['FLC_content']
                comment['reply_time'] = comment['FLC_time']
                comment_user_id = comment['FLC_author_id']
                user = User.objects.get(user_id=comment_user_id)
                picture = Picture.objects.get(PC_author_id=user)
                comment['username'] = user.user_name
                comment['avatar'] = picture.PC_path
                comment['user_id'] = user.user_id
            res["data"] = comment_list1
        except Exception as e:
            res["code"] = -1
            res["message"] = "获取帖子全部信息失败" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    print(res["code"])
    print(res["post_title"])
    print(res["content"])
    print(res["username"])
    print(res["picture"])
    print(res["data"])
    return JsonResponse(res)


# @csrf_exempt
# def getAllComment(request):
#     res = {"code": 1, "message": "", "data": None}
#     if request.method == 'POST':
#         try:
#             data = JSONParser().parse(request)
#
#         except Exception as e:
#             res["code"] = -1
#             res["message"] = "获取帖子全部信息失败" + str(e)
#     else:
#         res["code"] = -1
#         res["message"] = "请使用POST方法"
#     return JsonResponse(res)