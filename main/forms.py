from django import forms
from .models import Speciality, Region, Advertisement


#
# class NeedWorker(forms.Form):
#     organization = forms.CharField(max_length=100)
#     # speciality = forms.ManyToManyField(Speciality)
#     # region = forms.ForeignKey(Region, on_delete=forms.RESTRICT)
#     responsible = forms.CharField(max_length=50, verbose_name="Mas'ul", blank=True, default=None, null=True)
#     start_answer_time = forms.TimeField()
#     end_answer_time = forms.TimeField()
#     start_working_time = forms.TimeField()
#     end_working_time = forms.TimeField()
#     salary = forms.CharField(max_length=50)
#     phone_number = forms.CharField(max_length=50)
#     email = forms.EmailField(blank=True, default=None, null=True)
#     telegram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     facebook = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     instagram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     website = forms.URLField(max_length=200, blank=True, default=None, null=True)
#     twitter = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     linkedin = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     extra = forms.CharField(max_length=100, blank=True, default=None, null=True)
#
#
# class NeedWork(forms.Form):
#     worker = forms.CharField(max_length=100)
#     age = forms.PositiveSmallIntegerField()
#     speciality = forms.ManyToManyField(Speciality)
#     region = forms.ForeignKey(Region, on_delete=forms.RESTRICT)
#     salary = forms.CharField(max_length=100)
#     is_working = forms.BooleanField(default=False)
#     start_answer_time = forms.TimeField()
#     end_answer_time = forms.TimeField()
#     phone_number = forms.CharField(max_length=50)
#     email = forms.EmailField(blank=True, default=None, null=True)
#     telegram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     facebook = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     instagram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     website = forms.URLField(max_length=200, blank=True, default=None, null=True)
#     twitter = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     linkedin = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     extra = forms.CharField(max_length=100, blank=True, default=None, null=True)
#
#
# class NeedTeacher(forms.Form):
#     pupil = forms.CharField(max_length=50)
#     age = forms.PositiveSmallIntegerField()
#     speciality = forms.ManyToManyField(Speciality)
#     region = forms.ForeignKey(Region, on_delete=forms.RESTRICT)
#     salary = forms.CharField(max_length=100)
#     is_working = forms.BooleanField(default=False)
#     start_answer_time = forms.TimeField()
#     end_answer_time = forms.TimeField()
#     phone_number = forms.CharField(max_length=50)
#     email = forms.EmailField(blank=True, default=None, null=True)
#     telegram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     facebook = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     instagram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     website = forms.URLField(max_length=200, blank=True, default=None, null=True)
#     twitter = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     linkedin = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     extra = forms.CharField(max_length=100, blank=True, default=None, null=True)
#
#
# class NeedPupil(forms.Form):
#     teacher = forms.CharField(max_length=50)
#     age = forms.PositiveSmallIntegerField()
#     speciality = forms.ManyToManyField(Speciality)
#     region = forms.ForeignKey(Region, on_delete=forms.RESTRICT)
#     salary = forms.CharField(max_length=100)
#     is_working = forms.BooleanField(default=False)
#     start_answer_time = forms.TimeField()
#     end_answer_time = forms.TimeField()
#     phone_number = forms.CharField(max_length=50)
#     email = forms.EmailField(blank=True, default=None, null=True)
#     telegram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     facebook = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     instagram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     website = forms.URLField(max_length=200, blank=True, default=None, null=True)
#     twitter = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     linkedin = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     extra = forms.CharField(max_length=100, blank=True, default=None, null=True)
#
# class EducationCenter(forms.Form):
#     organization = forms.CharField(max_length=100)
#     speciality = forms.ManyToManyField(Speciality)
#     region = forms.ForeignKey(Region, on_delete=forms.RESTRICT)
#     responsible = forms.CharField(max_length=50, verbose_name="Mas'ul")
#     start_answer_time = forms.TimeField()
#     end_answer_time = forms.TimeField()
#     start_working_time = forms.TimeField()
#     end_working_time = forms.TimeField()
#     salary = forms.IntegerField()
#     phone_number = forms.CharField(max_length=50)
#     email = forms.EmailField(blank=True, default=None, null=True)
#     telegram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     facebook = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     instagram = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     website = forms.URLField(max_length=200, blank=True, default=None, null=True)
#     twitter = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     linkedin = forms.CharField(max_length=200, blank=True, default=None, null=True)
#     extra = forms.CharField(max_length=100, blank=True, default=None, null=True)


# class Advertisement(models.Model):
#     organization = models.CharField(max_length=100, blank=True, default=None, null=True)
#     speciality = models.ManyToManyField(Speciality)
#     region = models.ForeignKey(Region, on_delete=models.RESTRICT)
#     person = models.CharField(max_length=50, verbose_name="Shaxs")
#     age = models.PositiveSmallIntegerField(blank=True, default=None, null=True)
#     start_answer_time = models.TimeField()
#     end_answer_time = models.TimeField()
#     start_working_time = models.TimeField(blank=True, default=None, null=True)
#     end_working_time = models.TimeField(blank=True, default=None, null=True)
#     salary = models.IntegerField()
#     phone_number = models.CharField(max_length=50)
#     email = models.EmailField(blank=True, default=None, null=True)
#     telegram = models.CharField(max_length=200, blank=True, default=None, null=True)
#     facebook = models.CharField(max_length=200, blank=True, default=None, null=True)
#     instagram = models.CharField(max_length=200, blank=True, default=None, null=True)
#     website = models.URLField(max_length=200, blank=True, default=None, null=True)
#     twitter = models.CharField(max_length=200, blank=True, default=None, null=True)
#     linkedin = models.CharField(max_length=200, blank=True, default=None, null=True)
#     extra = models.CharField(max_length=100, blank=True, default=None, null=True)



class NeedWorkerForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['organization', 'speciality', 'region', 'person', 'start_answer_time', 'end_answer_time',
                  'start_working_time', 'end_working_time', 'salary', 'phone_number', 'email', 'telegram',
                  'facebook', 'instagram', 'website', 'twitter', 'linkedin', 'extra']


class NeedWorkForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['']