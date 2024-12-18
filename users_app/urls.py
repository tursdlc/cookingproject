from django.urls import include, path
from rest_framework import routers
from .views import UserView


router = routers.DefaultRouter()
router.register(r'-users', UserView, 'users_app')

urlpatterns = [
    path('', include(router.urls))

]