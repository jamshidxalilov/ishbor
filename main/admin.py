from django.contrib import admin

from .models import NeedWork, NeedWorker, NeedPupil, NeedTeacher, Region, EducationCenter, Speciality

class NeedWorkAdmin(admin.ModelAdmin):
    class Meta:
        model = NeedWork

admin.site.register(NeedWork, NeedWorkAdmin)


class NeedWorkerAdmin(admin.ModelAdmin):
    class Meta:
        model = NeedWorker

admin.site.register(NeedWorker, NeedWorkerAdmin)


class NeedPupilAdmin(admin.ModelAdmin):
    class Meta:
        model = NeedPupil

admin.site.register(NeedPupil, NeedPupilAdmin)

class NeedTeacherAdmin(admin.ModelAdmin):
    class Meta:
        model = NeedTeacher

admin.site.register(NeedTeacher, NeedTeacherAdmin)


class RegionAdmin(admin.ModelAdmin):
    class Meta:
        model = Region

admin.site.register(Region, RegionAdmin)



class SpecialityAdmin(admin.ModelAdmin):
    class Meta:
        model = Speciality

admin.site.register(Speciality, SpecialityAdmin)


class EducationCenterAdmin(admin.ModelAdmin):
    class Meta:
        model = EducationCenter

admin.site.register(EducationCenter, EducationCenterAdmin)






