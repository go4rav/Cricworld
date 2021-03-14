from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.views.generic import View 
from django.contrib import messages	
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return redirect("league:main")
	else:
		context={}
		return render(request,"accounts/index.html",context)






class RegisterView(View):
	
		form=UserRegistration # User Registration
		def get(self,request):   #when first time this URL is requested http://localhost:8000/signup/, this is GET request
			if request.user.is_authenticated:
				return redirect("league:main")
			else:
				form=self.form(None)
				context={'form':form}
				return render(request,"accounts/signup.html",context)

	 
		def post(self,request):  # After submitting the form, we are requesting the same URL and so we differentite it using method attribute which here in this case is "POST"
			form=self.form(request.POST)	
			if form.is_valid():
				form.save()
				name= form.cleaned_data.get('first_name')
				messages.success(request, name+", you account is created. Please login")
				return redirect("start:login")
			context={'form':form}
			return render(request,"accounts/signup.html",context)


class LoginView(View):
		def get(self,request):
			if request.user.is_authenticated:
				return redirect("league:main")
			else:
				context={}
				return render(request,"accounts/login.html",context)
		def post(self,request):
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active: #if user is not blocked by admin
					login(request,user)
					return redirect('league:main')
			else:
				messages.info(request,"username or password is incorrect")
				context={}
				return render(request,"accounts/login.html",context)


class LogoutView(View):
	def get(self,request):
		logout(request)
		return redirect("start:index")
	













'''
---this one also works but this is not the right way because why are we creating User Model and User Registration form for LoginView in the first place---
form=UserRegistration 
	
def get(self,request):
		form=self.form(None)	
		context={'form':form}
		return render(request,"accounts/login.html",context)
def post(self,request):
	form=self.form(None)	
	username=self.request.POST.get('username')
	password=self.request.POST.get('password1')
	user=authenticate(username=username,password=password)
	if user is not None:
		login(request,user)
		return redirect('league:main')
	else:
		messages.info(request,"username or password is incorrect")
		context={'form':form}
		return render(request,"accounts/login.html",context)
'''