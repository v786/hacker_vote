from django.contrib import admin

from .models import Candidate, Expertise, Vote

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Expertise)
admin.site.register(Vote)