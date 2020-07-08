from django.shortcuts import render

# Create your views here.
from .models import Post

def home(request):
	posts = Post.objects.all()
	return render(request,"kidszone/home.html",{'posts':posts})

def contact(request):
	return render(request,"kidszone/contact.html")

def about(request):
	return render(request,"kidszone/about.html")

