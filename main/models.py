from django.db import models



class Speciality(models.Model):
    name = models.CharField(max_length=100)



class Region(models.Model):
    name = models.CharField(max_length=50)

# NeedWork, NeedWorker, NeedPupil, NeedTeacher, EducationCenter
class Advertisement(models.Model):
    organization = models.CharField(max_length=100, blank=True, default=None, null=True)
    speciality = models.ManyToManyField(Speciality)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    person = models.CharField(max_length=50, verbose_name="Shaxs")
    age = models.PositiveSmallIntegerField(blank=True, default=None, null=True)
    start_answer_time = models.TimeField()
    end_answer_time = models.TimeField()
    start_working_time = models.TimeField(blank=True, default=None, null=True)
    end_working_time = models.TimeField(blank=True, default=None, null=True)
    salary = models.IntegerField()
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(blank=True, default=None, null=True)
    telegram = models.CharField(max_length=200, blank=True, default=None, null=True)
    facebook = models.CharField(max_length=200, blank=True, default=None, null=True)
    instagram = models.CharField(max_length=200, blank=True, default=None, null=True)
    website = models.URLField(max_length=200, blank=True, default=None, null=True)
    twitter = models.CharField(max_length=200, blank=True, default=None, null=True)
    linkedin = models.CharField(max_length=200, blank=True, default=None, null=True)
    extra = models.CharField(max_length=100, blank=True, default=None, null=True)