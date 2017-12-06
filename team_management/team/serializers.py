from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):

	class Meta:
		model = Team
		fields = ("id", "first_name", "last_name", "email", "phone", "role")