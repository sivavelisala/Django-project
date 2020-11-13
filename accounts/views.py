from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Posts

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('blog')
        else:
            messages.info(request,'username or password incorrect')
            print('username or password incorrect')
            return redirect('login')    
    else:
        return render(request,'login.html')

def register(request):

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                print('Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Id already exists')
                print('Email Id already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                messages.info(request,'Registered successfully, Please login')
                return redirect('login')
        else:
            messages.info(request,'password and confirm password are not matching')
            return redirect('register')
    else:                  
        return render(request,'register.html')        

def blog(request):
    posts = Posts.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def posts(request):

    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']

        if author is None:
            messages.info(request, 'Please provide author name')
            return redirect('blog')
        elif title is None:
            messages.info(request, 'Please provide title')
            return redirect('blog')
        elif content is None:
            messages.info(request, 'Please provide content')
            return redirect('blog')
        else:
            post=Posts(author=author,title=title,content=content)
            post.save()
            posts = Posts.objects.all()
            return render(request, 'blog.html', {'posts': posts})
    else:
        posts= Posts.objects.all()
        print(posts)
        return render(request, 'blog.html',{'posts':posts})



def logout(request):
    return redirect('home')        


