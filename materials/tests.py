from rest_framework.test import APITestCase

from users.models import User
from materials.models import Lessons, Courses, Subscription


class LessonsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test-test@test.test")
        self.client.force_authenticate(user=self.user)

        self.lessons = Lessons.objects.create(title="Урок", description="Описание урока", owner=self.user)

        self.courses = Courses.objects.create(title="Курс", description="Описание курса", owner=self.user)

    def test_retrieve(self):
        response = self.client.get("lesson/1/")
