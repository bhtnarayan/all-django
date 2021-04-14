from django.db import models
from django.template.defaultfilters import slugify 
from django.urls import reverse 
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255) 
    body = models.TextField() 
    slug = models.SlugField(null = False, unique = True) 

    def __str__(self):
        return self.title 

    # def get_absolute_url(self):
    #     return reverse('article_detail', args = [str(self.id)]) 

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})







    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title) 
    #     return super().save(*args, **kwargs) 
    