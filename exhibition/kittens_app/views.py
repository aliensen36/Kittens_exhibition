from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Breed, Kitten, KittenRating
from .serializers import BreedSerializer, KittenSerializer, KittenDetailSerializer, KittenRatingSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API для получения списка пород котят.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    """
    API для управления котятами. Поддерживает CRUD операции: создание, получение, обновление, удаление котят.
    """
    serializer_class = KittenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated | permissions.AllowAny]

    def get_queryset(self):
        """
        Возвращает список котят. Можно фильтровать по id породы через параметр breed_id.
        """
        breed_id = self.request.query_params.get('breed_id')
        if breed_id:
            return Kitten.objects.filter(breed_id=breed_id)
        return Kitten.objects.all()

    def perform_create(self, serializer):
        """
        Создание нового котенка. Привязывает котенка к текущему авторизованному пользователю (владельцу).
        """
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """
        Обновление информации о котенке. Доступно только для владельцев.
        """
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        """
        Удаление котенка. Доступно только для владельцев.
        """
        kitten = self.get_object()
        self.check_object_permissions(request, kitten)
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_kittens(self, request):
        """
        Возвращает всех котят, добавленных текущим пользователем.
        """
        user = request.user
        kittens = Kitten.objects.filter(owner=user)
        serializer = self.get_serializer(kittens, many=True)
        return Response(serializer.data)


class KittenRatingViewSet(viewsets.ModelViewSet):
    """
    API для управления рейтингами котят. Поддерживает создание, получение, обновление и удаление рейтингов.
    """
    queryset = KittenRating.objects.all()
    serializer_class = KittenRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Создание рейтинга котенка. Привязывает рейтинг к текущему пользователю.
        """
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Создание нового рейтинга котенка. Проверяет, не был ли ранее оценен котенок этим пользователем.
        """
        kitten_id = request.data.get('kitten')
        if not kitten_id:
            return Response({'error': 'Поле kitten обязательно.'}, status=status.HTTP_400_BAD_REQUEST)

        if KittenRating.objects.filter(kitten_id=kitten_id, user=request.user).exists():
            return Response({'error': 'Вы уже оценили этого котенка.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
