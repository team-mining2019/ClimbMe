from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    year_in_school = models.CharField(
        max_length=10,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='JR',
    )

    def __str__(self):
        return self.user.username

    def get_choices(self):
        temp = []
        for year in self.YEAR_IN_SCHOOL_CHOICES:
            temp.append(year[1])
        return temp

    #def get_year_in_school(self):
    #    
    #    return self.year_in_school