from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator



class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        ordering =['name', 'about', 'website']



class WatchList(models.Model):

    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')

    title = models.CharField(max_length=250)
    stroyline = models.TextField(max_length=250)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        ordering =['title', 'stroyline', 'active', 'created']


class Review(models.Model):
    rating =models.PositiveIntegerField(validators =[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null =True)
    watchlist =models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active =models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) 


  