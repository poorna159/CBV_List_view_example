from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from app.models import *



class Trainers_List(ListView):
    model=Trainer

    template_name='Trainers_List.html'
    
    context_object_name='tl'
    #queryset=Trainer.objects.filter(trainer_name='lucky')
    ordering=['trainer_name']