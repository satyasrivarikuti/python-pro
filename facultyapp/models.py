
from django.db import models
from adminapp.models import StudentList

class AddCourse(models.Model):
    COURSE_CHOICES =[
        ('AOOP' , 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
        ('NPS', 'Network Protocols And Security'),
    ]
    SECTION_CHOICES=[
        ('S11','SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
        ('S16', 'SECTION S16'),
        ('S17', 'SECTION S17'),
    ]
    student = models.ForeignKey(StudentList, on_delete= models.CASCADE)
    course=models.CharField(max_length=50, choices = COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.name} - {self.course}'

# blog/models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('DBMS', 'DataBase Management System'),
        ('LAA', 'Linux Automation and Administration'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.course} )'


def studentlist():
    return None