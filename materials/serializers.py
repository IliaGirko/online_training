from rest_framework.serializers import ModelSerializer

from .models import Courses, Lessons


class LessonsModelSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


class CoursesModelSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
