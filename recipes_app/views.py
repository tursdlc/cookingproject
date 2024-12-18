from rest_framework import viewsets
from recipes_app.models import Recipe
from recipes_app.serializer import RecipeSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    # use model through ORM
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
