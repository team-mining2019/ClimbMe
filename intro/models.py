from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
MY_CHOICES = (('1', '새벽'),
              ('2', '아침'),
              ('3', '낮'),
              ('4', '저녁'),
              ('5', '밤'))

MY_CHOICES2 = (('1', '한국어'),
              ('2', '영어'),
              ('3', '일어'),
              ('4', '중국어'),
              ('5', '스페인어'),
              ('6', '파이썬'),
              ('7', '아랍어'),
              ('8', 'C언어'),
              ('9', '사랑의 언어'),
              ('10', '제스쳐'))




class Info(models.Model):
    question_1 = models.BooleanField(default=True)  #https://stackoverflow.com/questions/5190313/django-booleanfield-how-to-set-the-default-value-to-true
    question_2 = models.CharField(max_length=1, choices=MY_CHOICES) #https://nachwon.github.io/django-field/
    question_3 = models.CharField(max_length=10, choices=MY_CHOICES2)
    question_4 = models.TextField()
    question_5 = models.TextField()

    def __str__(self):
        return(self.id)



#    question_2 = MultiSelectField(choices=MY_CHOICES) #https://github.com/goinnn/django-multiselectfield
#    question_3 = MultiSelectField(choices=MY_CHOICES2,
#                                 max_choices=10,
#                                 max_length=10)