from django.db import models

# Create your models here.
class Student(models.Model):
    # id -> Django generates this for us
    name = models.CharField(max_length=55)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Student object: Name = {self.name}, Email = {self.email}>"