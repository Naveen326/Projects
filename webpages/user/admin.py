from django.contrib import admin
from .models import Question,Answer,UserProfile

# Register your models here.

admin.site.register(UserProfile)


class QuestionAdmin(admin.ModelAdmin):
    list_display =['title','question','user', 'created']

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display=['user','created','approved']

admin.site.register(Answer,AnswerAdmin)
