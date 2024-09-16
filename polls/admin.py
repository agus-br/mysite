from django.contrib import admin

from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General information", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice) 