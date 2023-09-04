from rest_framework import serializers

from dj_app_blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
        )
        model = Post
