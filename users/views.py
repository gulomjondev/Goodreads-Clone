from django.contrib.auth import login, logout

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, UpdateView

from .forms import UserCreateForm, UserUpdateForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import CustomUser


class RegisterView(View):
    def get(self, request):
        user_form = UserCreateForm()
        context = {
            'form': user_form,
        }
        return render(request, 'users/register.html', context)

    def post(self, request):


        user_form = UserCreateForm(data=request.POST)
        if user_form.is_valid():

            user_form.save()
            context = {
                    'form': user_form,
                }
            return render(request, 'users/login.html', context)
        else:
            context = {
                'form': user_form,
            }
            return render(request, 'users/register.html', context)

# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render, redirect
# from django.views import View

class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli tizimga kirdingiz ✅")

            # next parametri bo‘lsa, shunga yo‘naltiramiz, bo‘lmasa /profile/
            next_url = request.GET.get('next') or '/profile/'
            return redirect(next_url)

        # agar login xato bo‘lsa, form qaytadan chiqariladi
        return render(request, 'users/login.html', {'login_form': login_form})


class UserProfileView(LoginRequiredMixin,DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile_edit.html', {'form': user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(instance=request.user, data=request.POST)

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "Congratulations, profile updated!")
            return redirect('users:profile')

        return render(request, 'users/profile_edit.html', {'form': user_update_form})
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')
