from django.shortcuts import render
from .models import Postagem
from .forms import PostagemForm

# Create your views here.
def index(request):
    context = {
        'posts': Postagem.objects.all(),
        'form': PostagemForm(),
    }

    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)

        print("é um post!!!!!!!!!!")
        if form.is_valid():
            form.save()
            print("salvou")

        context['form'] = form

    return render(request, "blog/index.html", context)