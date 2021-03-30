from django.contrib import admin

# Register your models here.
from apps.boards.models import Board, Task, Comment

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(Comment)
