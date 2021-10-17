from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apimoto import views



router = routers.DefaultRouter()
router.register(r"bike", views.DataBikesViewSet, basename='bikes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/v1/', include('rest_framework.urls', namespace='rest_framework'))
]


