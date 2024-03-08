from rest_framework import status
from rest_framework.decorators import action
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserInfoSerializer

class CustomUserViewSet(UserViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'me':
            return UserInfoSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['put'], url_path='update-profile')
    def update_profile(self, request, pk=None):
        user = self.get_object()
        profile = user.profile

        serializer = UserInfoSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'me':
            return UserInfoSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['put'], url_path='update-profile')
    def update_profile(self, request, pk=None):
        user = self.get_object()
        profile = user.profile

        serializer = UserInfoSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)