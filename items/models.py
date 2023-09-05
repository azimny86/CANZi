from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Items(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items_post")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.ImageField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='items_likes', blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comments(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"