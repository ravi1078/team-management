# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
	"""Model to define team member data"""

	ROLE = (
		('admin', 'Admin'),
		('regular', 'Regular')
	)

	first_name = models.CharField(verbose_name='First Name', max_length=20)
	last_name = models.CharField(verbose_name='Last Name', max_length=20)
	email = models.EmailField(verbose_name='Email')
	phone = models.CharField(verbose_name='Phone', max_length=15)
	role = models.CharField(verbose_name='Role', choices=ROLE, max_length=10, default='regular')

	def __str__(self):
		return self.first_name + " " + self.last_name

	
		
