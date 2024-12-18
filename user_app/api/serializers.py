from rest_framework import serializers
from rest_framework.authtoken.admin import User


class UserSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ["username", "password", "password2", "email"]
		extra_kwargs = {
			"password": {"write_only": True}
		}

	def save(self, **kwargs):
		password = self.validated_data["password"]
		password2 = self.validated_data["password2"]
		if password != password2:
			raise serializers.ValidationError({"password": "Passwords must match."})
		user = User(username=self.validated_data["username"], email=self.validated_data["email"])
		user.set_password(password)
		user.save()
		return user
