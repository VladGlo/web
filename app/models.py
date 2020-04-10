from django.db import models

# Create your models here.


class ExamMarks(models.Model):
    exam_id = models.IntegerField()
    stud_id = models.IntegerField()
    subj_id = models.IntegerField()
    mark = models.IntegerField(default=None, blank=True, null=True)
    exam_date = models.DateField()

    def __str__(self):
        return f"id: ${self.exam_id}, stud_id: ${self.stud_id}, subj_id: ${self.subj_id}, mark: ${self.mark}, date: ${self.exam_date}"


class Subject(models.Model):
    subj_id = models.IntegerField(primary_key=True)
    subj_name = models.CharField(max_length=40)
    hour = models.IntegerField()
    semester = models.IntegerField()

