from django.contrib import admin

from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General information", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ] 
    inlines = [ChoiceInline]



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice) 