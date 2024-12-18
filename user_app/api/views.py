from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_app.api.serializers import UserSerializer


@api_view(['POST'])
def register(request):
	serializer = UserSerializer(data=request.data)
	data = {}

	if serializer.is_valid():
		account = serializer.save()
		data['response'] = "Successfully registered a new user."
		data['email'] = account.email
		data['username'] = account.username
		data['token'] = Token.objects.get(user=account).key
	else:
		data = serializer.errors
	return Response(data)
