from rest_framework import serializers
from .models import User, Post, FirstLayerComment, SecondLayerComment,CollectPost,Picture,Inform,Reply,Label,PostAndLabels


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class FirstLayerCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FirstLayerComment
        fields = "__all__"

class SecondLayerCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecondLayerComment
        fields = "__all__"

class CollectPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CollectPost
        fields = "__all__"

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"

class InformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inform
        fields = "__all__"

class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"

class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"

class PostAndLabelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostAndLabels
        fields = "__all__"