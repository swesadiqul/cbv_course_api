from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from course.views import CourseViewSet
from course.views import CourseModelViewSet

router = DefaultRouter()
# router.register('courses', CourseViewSet, basename='course')
router.register('students', CourseModelViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('course.urls')),
    path('api/', include(router.urls)),
]
