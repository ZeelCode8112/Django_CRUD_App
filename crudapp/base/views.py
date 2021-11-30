from django.shortcuts import redirect, render
from .models import Data 

# Create your views here.
def home(request):
    details = Data.objects.all()
    context = {"details":details}
    return render(request,'home.html',context)

def insertData(request):    


    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        data = Data(name=name, email=email, phone=phone, age=age, gender=gender)
        data.save()
        return redirect('/')

    return render(request,'home.html')

def editData(request, id):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        detail = Data.objects.get(id=id)
        detail.name= name
        detail.email= email
        detail.phone= phone
        detail.age= age
        detail.gender= gender
        detail.save()
        return redirect('/')

    details = Data.objects.get(id=id)
    context = {"details":details}

    return render(request,'edit.html',context)

def deleteData(request, id):
    details = Data.objects.get(id=id)
    details.delete()
    return redirect('/')
