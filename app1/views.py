from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import addQuestionform
# Create your views here.


url = '/'
@login_required
def home(request):
    if request.method == 'POST':
        #print('Request post')
        #print(request.POST)
        #print('--------------------')
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)


def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 

@login_required
def about(request):
    globals()['url'] = request.get_full_path()
    context={}
    return render(request,'about.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect(url)
    if request.POST:
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['emailaddress']
        cpass = request.POST['cpassword']

        if(password == cpass):
            if User.objects.filter(username=username).exists():
                messages.error(request,"User is already exist with this username")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request,"User is already exist with this email")
                return redirect('register')
            else :
                user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
                user.save()
                return redirect('login')
        else :
            messages.error(request,"Password must be same")
            return redirect('register')
    context={}
    return render(request,'register.html',context)

def login(request):
    context={}
    if request.user.is_authenticated:
        return redirect(url)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username and password')
            return redirect('login')
        # if User.objects.filter(username=username).exists():
        #         user = User.objects.get(username=username)
        #         if user.password == password:
        #             messages.info(request,"Welcome {user.username}")
        #             return redirect('home')
        #         else:
        #             messages.info(request,"Incorrect password")
        #             return redirect('login')
        # else :
        #     messages.info(request,"Incorrect username and password")
        #     return redirect('login')
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('login')