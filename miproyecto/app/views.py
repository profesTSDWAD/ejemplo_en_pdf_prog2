from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User, Role
from app.serializers import UserSerializer, RoleSerializer


# Create your views here.
class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        seializer = UserSerializer(data=request.data)
        if seializer.is_valid():
            seializer.save()
            return Response(seializer.data, status=201)
        return Response(seializer.errors, status=400)

class RoleView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

