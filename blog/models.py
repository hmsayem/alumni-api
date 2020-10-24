from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

CATERGORY_CHOICES = [
    ('Number Theory', 'Number Theory'),
    ('Dynamic Programming', 'Dynamic Programming'),
    ('Data Structure', 'Data Structure'),
    ('Graph', 'Graph'),
    ('String', 'String'),
    ('Greedy', 'Greedy'),
    ('Miscellaneous', 'Miscellaneous')
]
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(choices=CATERGORY_CHOICES,max_length=250, default='Miscellaneous')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title) + " | " + str(self.author)



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + " | " + str(self.user.username)
