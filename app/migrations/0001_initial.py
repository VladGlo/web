# Generated by Django 3.0.4 on 2020-03-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.IntegerField()),
                ('stud_id', models.IntegerField()),
                ('subj_id', models.IntegerField()),
                ('mark', models.IntegerField(blank=True, default=None, null=True)),
                ('exam_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subj_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subj_name', models.CharField(max_length=40)),
                ('hour', models.IntegerField()),
                ('semester', models.IntegerField()),
            ],
        ),
    ]