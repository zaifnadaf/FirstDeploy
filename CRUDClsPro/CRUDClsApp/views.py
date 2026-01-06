from django.shortcuts import render
from .models import Book
from django.views.generic import ListView , DetailView ,CreateView , UpdateView

# Create your views here.
class Extracting(ListView):
    print('Hello')
    model = Book
    context_object_name = 'book'


class Single_view(DetailView):
    model=Book

class Extracting11(ListView):
    model=Book
    # template_name='testapp/index.html'
    # context_object_name='book'

class InsertingView(CreateView):
    model=Book
    fields = '__all__'

class UpdatingView(UpdateView):
    model = Book
    fields = '__all__'