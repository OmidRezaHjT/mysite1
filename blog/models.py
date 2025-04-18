from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class post(models.Model):
    image = models.ImageField(upload_to='Blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = TaggableManager()
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return "{} - {}".format(self.title,self.id)
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})

class Comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approach = models.BooleanField(default=False)
    class meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name
    