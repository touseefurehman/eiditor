from django.shortcuts import render
from .models import Post  
from django.shortcuts import render, redirect


# Create your views here.
def create_post(request):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        
        Post.objects.create(title=title, content=content)
        
        
        return redirect('post_list') 

    
    return render(request, 'create_post.html')


def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'post_list.html', {'posts': posts})