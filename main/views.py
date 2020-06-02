from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account

from django.core.files.storage import FileSystemStorage

# Create your views here.
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
def bio(request):
   return render(request, 'main/bio.html')
def achievements(request):
   return render(request, 'main/achievements.html')
