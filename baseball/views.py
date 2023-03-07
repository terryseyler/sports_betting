from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Stadiums, Forecast, Odds, GameSchedule

class IndexView(generic.ListView):
    template_name = 'baseball/index.html'
    context_object_name = 'stadium_list'

    def get_queryset(self):

    
        return Stadiums.objects.all()
    