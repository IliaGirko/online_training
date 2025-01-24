from rest_framework.serializers import SerializerMethodField, ModelSerializer

from .models import Courses, Lessons


class LessonsModelSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


class CoursesModelSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, courses):
        return Lessons.objects.filter(courses=courses).count()

    class Meta:
        model = Courses
        fields = ["id", "title", "image", "description", "count_lessons"]
