from django.contrib import admin
from .models import Dersler, tutorials, study_question, testler, test_questions, test_answers, winners
# Register your models here


class TestAdmin(admin.ModelAdmin):
    list_display = ("test_adi", "ders","test_tipi","test_seviyesi",)
    list_editable = ( 'ders', 'test_tipi',"test_seviyesi", )
    list_filter = ('ders',)

class StudyQuestionsAdmin(admin.ModelAdmin):
    list_display = ("pk","questions","ders","right_answer",)
    list_editable = ( "questions",'ders', "right_answer", )
    list_filter = ('ders',)

admin.site.register(Dersler)
admin.site.register(tutorials)
admin.site.register(study_question,StudyQuestionsAdmin)
admin.site.register(testler,TestAdmin)
admin.site.register(test_questions)
admin.site.register(test_answers)
admin.site.register(winners)
