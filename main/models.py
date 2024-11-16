from django.db import models

# Create your models here.
# class Subject(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# Faculty model
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Student model
class Student(models.Model):
    student_id = models.CharField(max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    # email = models.EmailField()

    def __str__(self):
        return self.student_id

# Department model
class Department(models.Model):
    dp_name = models.CharField(max_length=255)
    year=models.IntegerField()
    section = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dp_name} - {self.section}"

# Alloted model (Faculty allowed to teach a subject in a department)
class Alloted(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    dept = models.ForeignKey('Department', on_delete=models.CASCADE ,related_name="d")

    def __str__(self):
        return f"{self.faculty} allowed to teach {self.subject} in {self.dept}"

# Sessionstaken model (Class sessions)
class Sessionstaken(models.Model):
    date = models.DateField()
    period_no = models.IntegerField()  # e.g., Period 1, Period 2, etc.
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=255)
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"Session {self.id} on {self.date} (Period {self.period_no})"

# Attendance model (Student attendance in a session)
class Attendance(models.Model):
    session = models.ForeignKey('Sessionstaken', on_delete=models.CASCADE, related_name="attended")
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    count = models.PositiveIntegerField()  # Assuming "count" is an integer value

    def __str__(self):
        return f"Attendance for {self.student} in {self.session}"

# # Timing model (Timings for sessions)
# class Timing(models.Model):
#     time = models.TimeField()  # Time of the session
#     allowed = models.ForeignKey('Allowed', on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.time)