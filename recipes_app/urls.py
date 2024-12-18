from django.urls import include, path
from .views import RecipeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("-recipes", RecipeView)

urlpatterns = [
    path('', include(router.urls))
]