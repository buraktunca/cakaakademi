# Generated by Django 3.0.7 on 2022-09-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_winners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winners',
            name='winner_student_comment',
            field=models.TextField(max_length=500),
        ),
    ]
