from django.contrib import admin
from .models import User, Quiz, Challenger
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Challenger)
class ChallengerAdmin(admin.ModelAdmin):
    list_display = ['name']