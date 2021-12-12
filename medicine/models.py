from django.db import models

# Create your models here.

class Medicine(models.Model):
  name =models.CharField(max_length=60)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
 

  def create_medicine(self):
    self.save()

  def delete_medicine(self):
    self.delete()

  @classmethod
  def search_medicine(cls, medicine):
    return cls.objects.filter(name__icontains=medicine).all()

  def __str__(self):
    return self.name