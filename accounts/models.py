from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogUser(User):
	qq = models.PositiveIntegerField()
