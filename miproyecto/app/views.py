from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Users, Role
from app.serializers import UserSerializer, RoleSerializer


# Create your views here.
class UserView(APIView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
      