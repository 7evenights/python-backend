from django.db import models

# Create your models here.
class ExamScore(models.Model):
    allsubject = (
        ("คณิต", "คณิตศาสตร์"),
        ("วิทย์", "วิทยาศาสตร์"),
        ("ศิลปะ", "ศิลปศาสตร์"),
        ("อังกฤษ", "ภาษาอังกฤษ"),
        ("ฟิสิกส์", "ฟิสิกส์"),
        ("ชีวะ", "ชีววิทยา"),
    )
    subject = models.CharField(max_length=200, choices=allsubject, default="math")
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student_name} {self.subject} {self.score}"
