from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .form import UserRegisterForm, UserLoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'user registered')
            return redirect('account:user_login')
        return render(request, self.template_name, {'form': self.form_class})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login successfully')
                return redirect('product:home')
            messages.error(request, 'user not found')
        return render(request, self.template_name, {'form': self.form_class})


class UserProfileView(View):
    template_name = 'accounts/profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        return render(request, self.template_name, {'user': user})


class UserLogoutView(View):

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        if user is not None:
            logout(request)
            messages.success(request, 'logged out')
        return redirect('product:home')
