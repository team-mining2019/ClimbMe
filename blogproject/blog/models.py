from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_data = models.DateTimeField('data published')
    body = models.TextField()

    #googling :
    #this overrides the default name of the objects of this class, it's something like Auther:object which isn't very helpful.
    #overriding it gives a more human friendly name of the object like the Auther.name
    def __str__(self):
        return self.title  #위의 title

    

