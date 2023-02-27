from django.contrib import admin
from baseball.models import Stadiums,Forecast,GameSchedule,Odds
# Register your models here.
admin.site.register(Stadiums)
admin.site.register(Forecast)
admin.site.register(GameSchedule)
admin.site.register(Odds)