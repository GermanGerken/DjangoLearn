from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView

def articles_home(request):
    article = Articles.objects.all()
    return render(request, 'articles/articles.html', {'article': article})

class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'articles/create.html'
    form_class = ArticlesForm

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'articles/detail_view.html'
    context_object_name = 'post'

def articles_delete(request, id):
    item = Articles.objects.get(id=id)
    item.delete()
    return redirect('/article')

def articles_create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/article')
        else:
            error = 'Someting wrong with data'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'articles/create.html', data)