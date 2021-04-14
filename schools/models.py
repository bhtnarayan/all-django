from django.db import models

# Create your models here.
from django.urls import reverse 

class University(models.Model):
    # choice field to university whaere all uppercase name used 
    UNIVERSITY_TYPE = (
        ('PUBLIC', 'A public university'),
        ('PRIVATE', 'A private university')
    )


    full_name = models.CharField(
        max_length = 100,
        verbose_name = 'university full name',  # verbose name for name or label 
    )

    university_type = models.CharField(
        choices = UNIVERSITY_TYPE,
        max_length = 7, 
        verbose_name = 'type of university',
    )

    # meta class for long list of features 
    class Meta:
        indexes = [models.Index(fields = ['full_name'])] 
        ordering = ['-full_name'] 
        verbose_name = 'university'
        verbose_name_plural = 'universities'

    def __str__(self):
        return self.full_name 

    # get absolute url for canonical url for model 
    def get_absolute_url(self):
        return reverse('university_detail', args = [str(self.id)]) 




class Student(models.Model):
    first_name = models.CharField('first_name', max_length = 30) 
    last_name = models.CharField('last_name', max_length = 30) 
    university = models.ForeignKey(
        University, 
        on_delete = models.CASCADE,
        related_name = 'students',
        related_query_name = 'person',
    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name) 
    
    def get_absolute_url(self):
        return reverse('student_detail', args = [str(self.id)])
    