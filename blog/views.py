from django.shortcuts import render
from .models import Postagem

# Create your views here.
def index(request):
    context = {
        'posts': Postagem.objects.all(),
    }
    return render(request, "blog/index.html", context)