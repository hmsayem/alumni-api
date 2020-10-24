from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

FACULTY_CHOICES = [

    ('FST', 'FST'),
    ('FBS', 'FBS'),
    ('FASS', 'FASS'),
    ('FSSS', 'FSSS'),

]

DEPARTMENT_CHOICES = [
    ('General', 'General'),
    ('AIS', 'AIS'),
    ('Marketing', 'Marketing'),
    ('Finance & Banking', 'Finance & Banking'),
    ('Management', 'Management'),
    ('ICT', 'ICT'),
    ('ES', 'ES'),
    ('English', 'English'),
    ('Economics', 'Economics'),
    ('Sociology', 'Sociology'),
    ('DS', 'DS'),
    ('PA', 'PA'),
    ('DHSM', 'DHSM'),
    ('Law', 'Law'),
    ('IR', 'IR'),
    ('MCJ', 'MCJ'),
    ('PHRDS', 'PHRDS'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    faculty = models.CharField(choices=FACULTY_CHOICES, max_length=200)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=200)
    roll = models.IntegerField()
    batch = models.IntegerField()
    passing_year = models.IntegerField()
    resume = models.FileField(null=True, blank=True, upload_to='files/')
    def __str__(self):
        return str(self.user.username)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Social(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
