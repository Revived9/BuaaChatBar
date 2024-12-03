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
# class studentRegister(APIView):
#     def post(self, request):
#         print("!!!!")
#         request = JSONParser().parse(request)
#         # 生成一个随机的、唯一的BigInt作为用户ID
#         user_id = generate_unique_user_id()
#         user_name = request.data["name"]
#         user_password = request.data["password"]
#         user_email = request.data["email"]
#         user_student_id = request.data["student_id"]
#         user_experience = 0
#         user_sign_date = datetime.now().date()
#         user_birthday = datetime(2024,1,1)
#         # 头像上传状态先默认为0
#         user_uploaded = 0
#         # 用户状态先默认为0
#         user_role = 0
#         user_post_cnt = 0
#         user_info_cnt = 0
#         user = User(user_id = user_id, user_name = user_name, user_password = user_password, user_email = user_email, user_student_id = user_student_id, user_experience = user_experience,
#                     user_sign_date = user_sign_date, user_birthday = user_birthday, user_uploaded = user_uploaded, user_role = user_role,
#                     user_post_cnt = user_post_cnt, user_info_cnt = user_info_cnt)
#         if User.objects.filter(user_name = user_name):
#             code = -1
#             message = "用户名已经被注册了，请重新注册"
#             return Response({'code': code, 'message': message}, status=HTTP_400_BAD_REQUEST)
#         else:
#             user.save()
#             code = 1
#             message = "注册成功"
#             return Response({'code': code, 'message': message}, status=HTTP_200_OK)


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
            PC_path = "src\\assets\\avater.jpg"
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

# class adminRegister(APIView):
#     def post(self, request):
#         user_name = request.data["name"]
#         user_password = request.data["password"]
#         user_email = request.data["email"]
#         user_student_id = request.data["student_id"]
#         user_experience = 0
#         user_sign_date = datetime.now().date()
#         # 刚注册的用户的生日默认为2024.1.1
#         user_birthday = datetime(2024,1,1)
#         # 头像上传状态先默认为0
#         user_uploaded = 0
#         # 管理员状态先默认为1
#         user_role = 1
#         user_post_cnt = 0
#         user_info_cnt = 0
#         user = User(user_name = user_name, user_password = user_password, user_email = user_email, user_student_id = user_student_id, user_experience = user_experience,
#                     user_sign_date = user_sign_date, user_birthday = user_birthday, user_uploaded = user_uploaded, user_role = user_role,
#                     user_post_cnt = user_post_cnt, user_info_cnt = user_info_cnt)
#         if User.objects.filter(user_name = user_name):
#             code = -1
#             message = "用户名已经被注册了，请重新注册"
#             return Response({'code': code, 'message': message}, status=HTTP_400_BAD_REQUEST)
#         else:
#             user.save()
#             code = 1
#             message = "注册成功"
#             return Response({'code': code, 'message': message}, status=HTTP_200_OK)


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
                    picture = Picture.objects.get(PC_author_id = user.user_id)
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

# class UserLogin(APIView):
#     def post(self, request):
#         request = JSONParser().parse(request)
#         user_student_id = request.data["student_id"]
#         user_password = request.data["password"]
#         if User.objects.filter(user_student_id = user_student_id):
#             if User.objects.filter(user_student_id = user_student_id, user_password = user_password):
#                 code = 1
#                 message = "登陆成功，欢迎"
#                 return Response({'code': code, 'message': message}, status=HTTP_200_OK)
#             else:
#                 code = -2
#                 message = "登陆失败，密码错误"
#                 return Response({'code': code, 'message': message}, status=HTTP_400_BAD_REQUEST)
#         else:
#             code = -1
#             message = "登录失败，没有这个用户"
#             return Response({'code': code, 'message': message}, status=HTTP_400_BAD_REQUEST)

# class CreatePost(APIView):
#     def post(self, request):
#         post_id = generate_unique_user_id()
#         post_title = request.data["title"]
#         post_content = request.data["content"]
#         post_category = request.data["category"]
#         post_heat = 1
#         post_time = request.data["created_at"]
#         post_user_id = request.data["user_id"]
#         post_isTop = False


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
            post_isTop = False
            user = User.objects.get(user_student_id=post_user_id)
            LB_tag_name = data.get("tag_name")
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
                        post_heat = post_heat, post_time = post_time,post_user_id = user, post_isTop = post_isTop)
            post.save()
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


# @csrf_exempt
# def modifyPersonalInfo(request):
#     res = {"code": 1, "message": "", "data": None,"sign_date": datetime.now().date(),"post_cnt": -1}
#     if request.method == 'POST':
#         try:
#             data = JSONParser().parse(request)
#             user_id = data.get("user_id")
#             username = data.get("username")
#             email = data.get("email")
#             birthday = data.get("birthday")
#             uploaded = data.get("uploaded")
#             PC_path = data.get("path")
#             user = User.objects.get(user_id = user_id)
#             PC_id = generate_unique_picture_id()
#             PC_category = 0
#             picture = Picture(PC_id = PC_id, PC_path = PC_path,PC_author_id = user_id,PC_category = PC_category)
#             if not User.objects.filter(user_name = username):
#                 picture.save()
#                 user.user_name = username
#                 user.user_email = email
#                 user.user_birthday = birthday
#                 user.user_uploaded = uploaded
#                 res["code"] = 1
#                 res["message"] = "用户信息修改成功"
#                 res["sign_date"] = user.user_sign_date
#                 res["post_cnt"] = user.user_post_cnt
#             else:
#                 res["code"] = -1
#                 res["message"] = "用户信息修改失败，用户名已存在"
#         except Exception as e:
#             res["code"] = -1
#             res["message"] = "用户信息修改失败，用户id不存在"+str(e)
#     else:
#         res["code"] = -1
#         res["message"] = "请使用POST方法"
#     return JsonResponse(res)


@csrf_exempt
def createFirstLayerComment(request):
    res = {"code": 1, "message": "", "data": None,"comment_id": -1,"created_at": datetime.now().date(),"heat": 1,"path": None}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            content = data.get("content")
            user_id = data.get("user_id")
            post_id = data.get("post_id")
            PC_id = data.get("picture_id")
            user = User.objects.get(user_student_id = user_id)
            post = Post.objects.get(post_id=post_id)
            FLC_id = generate_unique_picture_id()
            FLC_time = datetime.now().date()
            FLC_content = content
            FLC_post_id = post_id
            FLC_author_id = user_id
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
            res["path"] = Picture.objects.get(PC_id = PC_id).PC_path
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
            PC_id = data.get("picture_id")
            user = User.objects.get(user_student_id = user_id)
            post = Post.objects.get(post_id=post_id)
            SLC_id = generate_unique_secondlayercomment_id()
            SLC_author_id = user_id
            SLC_comment_id = comment_id
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
            res["path"] = Picture.objects.get(PC_id = PC_id).PC_path
        except Exception as e:
            res["code"] = -1
            res["message"] = "发布评论失败，该用户不存在" + str(e)
    else:
        res["code"] = -1
        res["message"] = "请使用POST方法"
    return JsonResponse(res)

@csrf_exempt
def collectPost(request):
    res = {"code": 1, "message": "", "data": None, "id": -1}
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            # TODO
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
            print(user_id)
            print(newUsername)
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