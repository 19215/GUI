from django.db import models
from django.urls import reverse

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('COOKING', 'Cooking'),
        ('TRAVEL', 'Travel'),
        ('GAMING', 'Gaming'),
        ('TECHNOLOGY', 'Technology'),
        ('ART', 'Art'),
        ('MEMES', 'Memes'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.CharField(max_length = 20, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])    

# Create your models here.
