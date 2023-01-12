from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Articles
from .forms import ArticlesForm, DocumentForm, handle_uploaded_file


@login_required(login_url="/accounts/login/")
def article(request):
    form = ArticlesForm()
    if request.method == "POST":
        filled_form = ArticlesForm(
            request.POST, user=request.user, content=request.POST.get("content"))
        if filled_form.is_valid():
            filled_form.save()
            note = "Article has been published"
            return render(request, "articles/articles_form.html", {"note": note, "form": form})
        else:
            note = "Error! Couldn't publish the article!"
            return render(request, "articles/articles_form.html", {"note": note, "form": form})

    else:
        return render(request, "articles/articles_form.html", {"form": form})


class Articles_ListView(ListView):
    model = Articles
    context_object_name = "all_articles"

def Articles_subcategory_list(request, cat):
    category = ""
    if cat == 1:
        category = "Business News"
    elif cat == 2:
        category = "Tech News"
    elif cat == 3:
        category = "Politics News"
    elif cat == 4:
        category = "Sports News"
    elif cat ==5:
        category = "Entertainment News"

    subarticles = Articles.objects.filter(category=category)

    return render(request, "articles/article_subcategory_list.html", {"all_articles":subarticles, "category":category})

class Articles_DetailView(DetailView):
    model = Articles
    context_object_name = "article"


class Articles_DeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = '/news/articles/'
    template_name = 'articles/articles_delete.html'
    login_url = "/accounts/login/"




def upload_file(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            note = handle_uploaded_file(request.FILES['file'], request.user)
            return render(request, 'articles/upload_form.html', {'form': form, "note": note})
    else:
        return render(request, 'articles/upload_form.html', {'form': form})
