from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

# Create your views here.


def home(request): 
  wish_list = Wish.objects.all()
  return render(request, 'home.html', {'wish_list': wish_list})

class CreateWish(CreateView):
  model = Wish
  fields = '__all__'
  success_url = '/'

class DeleteWish(DeleteView):
  model = Wish
  success_url = '/'