from django.db import models


# Create your models here.
class User(models.Model):
    objects = models.Manager()
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    user_password = models.CharField(max_length=20)
    user_student_id = models.BigIntegerField()
    user_experience = models.BigIntegerField()
    user_sign_date = models.DateField()
    user_birthday = models.DateField()
    user_uploaded = models.IntegerField()
    user_role = models.IntegerField()
    user_post_cnt = models.IntegerField()
    user_info_cnt = models.IntegerField()
    user_introduction = models.TextField()


class Label(models.Model):
    objects = models.Manager()
    LB_id = models.BigIntegerField(primary_key=True)
    LB_tag_name = models.CharField(max_length=30)


class Post(models.Model):
    objects = models.Manager()
    post_id = models.BigIntegerField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_label = models.CharField(max_length=30)
    post_tag_id = models.ForeignKey(Label, on_delete=models.CASCADE)
    post_heat = models.IntegerField()
    post_time = models.DateTimeField()
    post_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_isTop = models.BooleanField()


class FirstLayerComment(models.Model):
    objects = models.Manager()
    FLC_id = models.BigIntegerField(primary_key=True)
    FLC_content = models.TextField()
    FLC_time = models.DateTimeField()
    FLC_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    FLC_author_id = models.ForeignKey(User, on_delete=models.CASCADE)


class SecondLayerComment(models.Model):
    objects = models.Manager()
    SLC_id = models.BigIntegerField(primary_key=True)
    SLC_author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    SLC_comment_id = models.ForeignKey(FirstLayerComment, on_delete=models.CASCADE)
    SLC_content = models.TextField()
    SLC_time = models.DateTimeField()


class CollectPost(models.Model):
    objects = models.Manager()
    CP_id = models.BigIntegerField(primary_key=True)
    CP_author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    CP_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    CP_annotation = models.TextField()


class Picture(models.Model):
    objects = models.Manager()
    PC_id = models.BigIntegerField(primary_key=True)
    # 最长路径为300
    PC_path = models.CharField(max_length=300)
    PC_category = models.IntegerField()
    PC_author_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Inform(models.Model):
    objects = models.Manager()
    IF_id = models.BigIntegerField(primary_key=True)
    IF_content = models.TextField()
    IF_receiver_id = models.ForeignKey(User, related_name='received_informs', on_delete=models.CASCADE)
    IF_sender_id = models.ForeignKey(User, related_name='sent_informs', on_delete=models.CASCADE)


class Reply(models.Model):
    objects = models.Manager()
    RP_id = models.BigIntegerField(primary_key=True)
    RP_content = models.TextField()
    RP_receiver_id = models.ForeignKey(User, related_name='received_replies', on_delete=models.CASCADE)
    RP_sender_id = models.ForeignKey(User, related_name='sent_replies', on_delete=models.CASCADE)
    RP_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    RP_comment_date = models.DateField()


class PostAndLabels(models.Model):
    objects = models.Manager()
    PL_id = models.BigIntegerField(primary_key=True)
    PL_tag_id = models.ForeignKey(Label, on_delete=models.CASCADE)
    PL_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostPicture(models.Model):
    objects = models.Manager()
    PP_id = models.BigIntegerField(primary_key=True)
    PP_path = models.CharField(max_length=300)
    PP_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)