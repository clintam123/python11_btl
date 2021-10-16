from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
import uuid
from django.db.models import enums
from datetime import datetime
# Create your models here.

# khởi tạo mô hình User tiêu chuẩn https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User
User = get_user_model()

# Profile của người dùng
class Profile(models.Model):
    id_user = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to='profile_image', default = 'blank-profile-picture.png')

    def __str__(self):
        return self.user.username
        #self.user lấy 

# Cấu trúc của mỗi bài Post
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4) # Lấy chuoi hash ngẫu nhiên làm id cho moi bai post
    user = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'post_images')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now)
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

# Lưu trữ người dùng đã like bài post chưa. Nếu like rồi thi ấn thêm sẻ xóa, nếu chưa thì lưu vào
class LikePost(models.Model):
    post_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 500)

    def __str__(self):
        return self.username