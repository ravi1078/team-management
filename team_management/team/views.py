# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Team
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .serializers import TeamSerializer
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class TeamView(APIView):
	"""API to manage team members """
	
	def get(self, request):
		teams = Team.objects.all()
		serializer = TeamSerializer(teams, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = TeamSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request):
		team = Team.objects.filter(id=request.data.get("id"))
		if team.exists():
			serializer = TeamSerializer(team[0], data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response({"messsage": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request):
		team = Team.objects.filter(id=request.data.get("id"))
		if team.exists():
			team.delete()
			return Response({"messsage": "Deleted Successfully"}, status=status.HTTP_200_OK)
		return Response({"messsage": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

