from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from . models import Post, Category, Tag


def index(request):
    
    return render (request, "index.html", {})

def articulos(request):
    query = request.GET.get('query')
    
    if query:
        articulos = Post.objects.filter(
            Q(title__icontains=query) 
        )
    
    else:
        articulos =  Post.objects.all()
        
    categorys = Category.objects.all()
    tags =Tag.objects.all()
    
    return render (request, "articulos.html", {'articulos': articulos, 'query':query, 'categorys':categorys, 'tags':tags})

def info(request, id):
    articulo = get_object_or_404(Post, id=id)
    
    return render(request, "info.html", {"articulo": articulo})

def filtro_categoria(request, id):
    category = get_object_or_404(Category, id=id)
    articulos = Post.objects.filter(category=category)
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    
    return render (request, 'articulos.html', {'category':category, 'articulos':articulos, 'categorys':categorys, 'tags':tags})
    
def filtro_etiqueta(request, id):
    tag = get_object_or_404(Tag, id=id)
    articulos = Post.objects.filter(tag=tag)
    tags = Tag.objects.all()
    categorys = Category.objects.all()
    
    return render(request, 'articulos.html', {'tag':tag, 'articulos':articulos, 'tags':tags, 'categorys':categorys})