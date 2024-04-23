from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from .models import JobPosition
from .models import User
from .models import UserJobPosition
from .serializer import JobPositionSerializer
from .serializer import UserJobPositionSerializer
from .serializer import UserSerializer


class UserListAPIView(GenericViewSet, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobPositionListCreateAPIView(GenericViewSet, generics.ListCreateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        job_position = JobPosition.objects.create(name=name)
        serializer = JobPositionSerializer(job_position)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)

        job_position = JobPosition.objects.create(name=name)
        serializer = JobPositionSerializer(job_position)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JobPositionRetrieveUpdateDestroyAPIView(GenericViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer

    @action(detail=True, methods=['POST'])
    def add_user(self, request, *args, **kwargs):
        job_position = self.get_object()
        user_id = request.data.get('user_id')

        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if UserJobPosition.objects.filter(job_position=job_position, user_id=user_id):
            return Response({'message': 'User already has this position'}, status=status.HTTP_400_BAD_REQUEST)

        UserJobPosition.objects.create(user=user, job_position=job_position)
        return Response({'message': 'User added to job position successfully'}, status=status.HTTP_201_CREATED)

    def _list_users(self, job_position):
        users = UserJobPosition.objects.filter(job_position=job_position)
        user_serializer = UserJobPositionSerializer(users, many=True)
        return [k['user'] for k in user_serializer.data]

    @action(detail=True, methods=['GET'])
    def list_users(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        users = self._list_users(instance)
        data = {
            'id': serializer.data['id'],
            'name': serializer.data['name'],
            'users': users
        }
        return Response(data)
