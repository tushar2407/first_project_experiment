from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import Account

from django.core.files.storage import FileSystemStorage

from .forms import Bookform
from .models import Book
# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
def index(request):
    context={}
    accounts=Account.objects.all()
    context['accounts']=accounts
    return render(request, 'main/users.html',context)
def upload(request):
    context={}
    if request.method=="POST":
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs=FileSystemStorage()
        if( not fs.exists(uploaded_file.name)):
            #print("asdasdas")
            name=fs.save(uploaded_file.name, uploaded_file)
            print(name)
        url=fs.url(uploaded_file.name)
        print(url)
        context['url']=url
    return render(request, 'main/upload.html',context)

def book_list(request):
    books=Book.objects.all()
    return render(request,'main/book_list.html',  {'books':books})
def book_upload(request):
    if(request.method=="POST"):
        form=Bookform(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('book_list')
    else :
        form=Bookform()
    return render(request,'main/book_upload.html',{'form':form})
def bio(request):
   return render(request, 'main/bio.html')
def achievements(request):
   return render(request, 'main/achievements.html')
class BookListView(ListView):
    model=Book
    template_name='main/class_book_list.html'
    context_object_name="books"
class UploadBookView(CreateView):
    model=Book
    #fields=['title','author','pdf','cover']
    form_class=Bookform
    success_url=reverse_lazy("book_list")
    template_name="main/book_upload.html"