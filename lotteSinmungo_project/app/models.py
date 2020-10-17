from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

class Solution(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    original_date = models.DateTimeField(auto_now=True)
    upload_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title  
    
class myUser(AbstractUser):
    username = models.CharField(max_length=64,verbose_name = '사용자명', unique=True)
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    like_problems = models.ManyToManyField('Problem', blank=True, related_name='like_users')
    def __str__(self):
        return self.username  

    class Meta:
        db_table = 'my_user'

class Problem (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    userid = models.IntegerField()
    like_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    def __str__(self):
        return self.title

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  

class Photo(models.Model):
    post = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)