from django.db import models
import datetime
from django.contrib.auth.models import User



class memory(models.Model):
    content = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)
    color = models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )