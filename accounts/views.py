from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate
from blog.models import Post
from django.utils import timezone
from .forms import LoginForm, RegisterForm
from .models import BlogUser

# Create your views here.

def user_login(request):
	if request.method == "POST":
		login_form = request.POST
		"""
				if login_form.is_valid():
					attempt_user=login_form.save(commit=False)
					user = authenticate(username=attempt_user.username, password=attempt_user.password)
					if user is not None:
						return render(request, 'accounts/login_succeeded.html', {'user': user})
		"""
		"""
		#attempt_user=login_form.save(commit=False)
		#attempt_user=BlogUser(login_form)
		"""
		user = authenticate(username =login_form['username'], password=login_form['password'])
		if user is not None:
			return render(request, 'accounts/login_succeeded.html', {'user': user})
		else:
			return render(request, 'accounts/login_failed.html', {'attempt_user': login_form['username']})
	else:
		login_form=LoginForm()
	return render(request, 'accounts/login.html', {'form': login_form})

def user_logout(request):
	logout(request)
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

def user_register(request):
	if request.method == 'POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts:login')
		else:
			return redirect('accounts:register')
	else:
		register_form=RegisterForm()
	return render(request, 'accounts/register.html',{'form': register_form})
