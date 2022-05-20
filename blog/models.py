from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=100,unique=True,null=False,blank=False)
    catrgory_author = models.ForeignKey(User,null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('posts_by_category', args=[self.name])
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_pic',null=True,blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(User,related_name="favourite", blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} comments on {self.post.title} post.'