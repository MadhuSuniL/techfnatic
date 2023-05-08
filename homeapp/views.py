from django.shortcuts import render,redirect
from adminpanel.models import *
from django.http import Http404
def Home(request):
    
    products = Product.objects.all()
    # print(products[0].url)
    
    return render(request , 'home.html',{
    'products':products,
    'intro_head':IntroHeading.objects.last().value,
    'intro_sub_head':IntroSubHeading.objects.last().value,
    'about':About.objects.last().value,
    'address':Address.objects.last().value,
    'email':Email.objects.last().value,

})
   
   
def AdminPage(request):    
    products = Product.objects.all()
    return render(request , 'admin.html',{
    'products':products,
    'intro_head':IntroHeading.objects.last().value,
    'intro_sub_head':IntroSubHeading.objects.last().value,
    'about':About.objects.last().value,
    'address':Address.objects.last().value,
    'email':Email.objects.last().value,
})
    
def ProductDelete(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/cus_admin')

    
    

    
    
    
def AddProduct(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES['img']
        product = Product.objects.create(title=title,content=content,img=img)
        return redirect('/cus_admin')
            
    
    
def UpdateIntro(request):
    if request.method == 'POST':
        value = request.POST['value']
        product = IntroHeading.objects.create(value=value)
        return redirect('/cus_admin')
    
    

def UpdateIntroSub(request):
    if request.method == 'POST':
        value = request.POST['value']
        product = IntroSubHeading.objects.create(value=value)
        return redirect('/cus_admin')
    
    

def UpdateAbout(request):
    if request.method == 'POST':
        value = request.POST['value']
        product = About.objects.create(value=value)
        return redirect('/cus_admin')
    
    

def UpdateEmail(request):
    if request.method == 'POST':
        value = request.POST['value']
        product = Email.objects.create(value=value)
        return redirect('/cus_admin')
    
    

def UpdateAddress(request):
    if request.method == 'POST':
        value = request.POST['value']
        product = Address.objects.create(value=value)
        return redirect('/cus_admin')
    
    
    
    
    