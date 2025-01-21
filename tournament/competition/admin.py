from django.contrib import admin
from .models import Competition, Team, Participant, Match

admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Participant)
admin.site.register(Match)

# Register your models here.
