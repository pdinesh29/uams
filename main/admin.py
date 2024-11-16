from django.contrib import admin
from .models import Attendance, Sessionstaken, Faculty, Student, Department, Alloted

# Register models with the admin site
admin.site.register(Attendance)
admin.site.register(Sessionstaken)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Alloted)