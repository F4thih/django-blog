from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request):
    blog_v=Blog.objects.all()
    return render(request,'index.html', {'blog' : blog_v})