from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from App_Cobb_Cars.models import Dealer
from django.contrib.auth.views import LoginView


# Create your views here.
class DealerLogin(LoginView):
    template_name = 'App_Cobb_cars/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self): 
        return reverse_lazy('dealer-view')

class DealerView(ListView):
    model = Dealer
    context_object_name = 'dealer'


class DealerDetail(DetailView):

    model = Dealer
    context_object_name = 'dealer'


class DealerCreate(CreateView):
    model = Dealer
    fields = '__all__'
    success_url = reverse_lazy('dealer-view')


class DealerUpdate(UpdateView):

    model = Dealer
    fields = '__all__'
    context_object_name = 'dealer'
    success_url = reverse_lazy('dealer-view')

class DealerDelete(DeleteView):
    model = Dealer
    context_object_name = 'dealer'
    success_url = reverse_lazy('dealer-view')


