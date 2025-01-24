from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from .models import Courses, Lessons
from .serializers import CoursesModelSerializer, LessonsModelSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesModelSerializer
    queryset = Courses.objects.all()


class LessonsCreateAPIView(CreateAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()


class LessonsUpdateAPIView(UpdateAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()


class LessonsDestroyAPIView(DestroyAPIView):
    serializer_class = LessonsModelSerializer


class LessonsRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()


class LessonsListAPIView(ListAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()
