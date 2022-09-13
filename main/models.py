from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dersler(models.Model):
    Type = (
        ('TYT', 'TYT'),
        ('AYT', 'AYT'),
    )
    Zorluk =(
        ("Kolay","Kolay"),
        ("Orta","Orta"),
        ("Zor","Zor"),
    )
    ders_adi = models.CharField(max_length=360)
    ders_tipi = models.CharField(max_length=3, choices=Type)
    upload_date=models.DateField(auto_now_add=False)
    ders_konu = models.CharField(max_length=360)
    ders_resmi = models.ImageField(upload_to ='uploads/')
    ders_seviyes =models.CharField(max_length=30, choices=Zorluk,default="Orta")

    def __str__(self):
        return "%s - %s" % (self.pk,self.ders_konu)

class tutorials(models.Model):
    ders=models.ForeignKey(Dersler,on_delete=models.CASCADE)
    tutorial = models.FileField(upload_to="tutorials/")

    def __str__(self):
        return "%s" % (self.ders)

class study_question(models.Model):
    ans = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    ders=models.ForeignKey(Dersler,on_delete=models.CASCADE)
    questions = models.ImageField(upload_to ='questions/')
    right_answer = models.CharField(max_length=1, choices=ans)

class testler(models.Model):
    Type = (
        ('TYT', 'TYT'),
        ('AYT', 'AYT'),
    )
    Zorluk =(
        ("Kolay","Kolay"),
        ("Orta","Orta"),
        ("Zor","Zor"),
    )
    test_seviyesi =models.CharField(max_length=30, choices=Zorluk,default="Orta")
    test_tipi = models.CharField(max_length=3, choices=Type)
    test_adi = models.CharField(max_length=360)
    ders = models.ForeignKey(Dersler,on_delete=models.CASCADE)

class test_questions(models.Model):
    ans = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    test=models.ForeignKey(testler,on_delete=models.CASCADE)
    test_question = models.ImageField(upload_to ='test_questions/')
    right_answer = models.CharField(max_length=1, choices=ans)

class test_answers(models.Model):
    ans = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    test=models.ForeignKey(testler,on_delete=models.CASCADE)
    test_question=models.ForeignKey(test_questions,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1, choices=ans)

class winners(models.Model):
    winner_student = models.ImageField(upload_to ='winners')
    winner_student_name = models.CharField(max_length=100)
    winner_student_uni = models.CharField(max_length=100)
    winner_student_comment = models.TextField()

#class ders_programi(models.Model):
#    sınıflar = (
#        ('12.Sınıf', '12.Sınıf'),
#        ('11.Sınıf', '11.Sınıf'),
#    )
#    type = (
#        ('MF', 'MF'),
#        ('TM', 'TM'),
#    )
#    sinif = models.CharField(max_length=100, choices=sınıflar)
#    sinif_type = models.CharField(max_length=100, choices=type)
#    hafta = models.IntegerField()
