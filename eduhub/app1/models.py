from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.IntegerField()
    semester_cleared = models.CharField(max_length=20)
    extracurricular = models.CharField(max_length=200)
    cocurricular = models.CharField(max_length=200)
    attendance_percentage = models.FloatField()
    cgpi = models.FloatField()
    sgpi = models.FloatField()

