from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import IntegerField 
from django.contrib.auth import get_user_model
import uuid
import datetime
from blogFood.settings import MEDIA_ROOT


# Create your models here.

class User(models.Model):
    id_user = IntegerField()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.ImageField(upload_to = MEDIA_ROOT); 
    user = models.CharField(max_length = 100)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(default= datetime.datetime.now, blank=True, editable= False)
    no_of_like = models.IntegerField(default=0)
    rate = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    description = models.TextField(blank=True)
    price = models.IntegerField(
    default=1,
    validators=[
        MinValueValidator(1)
    ]
    )

    def __str__(self):
        return self.user

