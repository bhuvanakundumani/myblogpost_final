from django.db import models
from django.utils import timezone


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)

    def __str__(self):
        return self.first_name + '' + self.last_name

class Post(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    author =  models.ForeignKey(Author, null =True, on_delete=models.CASCADE)


    def publish(self):
        self.published_date = timezone.now
        self.save()


    def __str__(self):
        return self.title + '       '+ 'published on ' + str(self.published_date)



