from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Courses, Lessons
from .serializers import CoursesModelSerializer, LessonsModelSerializer
from .permissions import ModersPermission, IsOwnerPermission

class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesModelSerializer
    queryset = Courses.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~ModersPermission,)
        elif self.action == "list":
            self.permission_classes = (ModersPermission | IsOwnerPermission,)
        elif self.action in ("retrieve", "update"):
            self.permission_classes = (ModersPermission | IsOwnerPermission,)
        elif self.action == "destroy":
            self.permission_classes = (~ModersPermission | IsOwnerPermission,)
        return super().get_permissions()


class LessonsCreateAPIView(CreateAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ~ModersPermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonsUpdateAPIView(UpdateAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ModersPermission | IsOwnerPermission]


class LessonsDestroyAPIView(DestroyAPIView):
    serializer_class = LessonsModelSerializer
    permission_classes = [IsAuthenticated, ~ModersPermission, IsOwnerPermission]


class LessonsRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ModersPermission | IsOwnerPermission]


class LessonsListAPIView(ListAPIView):
    serializer_class = LessonsModelSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, ModersPermission | IsOwnerPermission]

    def get_queryset(self):
        if ModersPermission().has_permission(self.request, self):
            return Lessons.objects.all()
        else:
            return Lessons.objects.filter(owner=self.request.user)
