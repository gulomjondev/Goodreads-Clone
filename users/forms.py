from django import forms
from django.core.mail import send_mail

from users.models import CustomUser
app_name = 'users'

class UserCreateForm(forms.ModelForm):
   class Meta:
       model = CustomUser
       fields = ('username','first_name','last_name','email','password')

   def save(self, commit = True):

       user  = super().save(commit)
       user.set_password(self.cleaned_data['password'])
       user.save()

       if user.email :
           send_mail(
               'asalom',
               'jollmi',
               'jahongirboyevgulomjon@gmail.com',
               [user.email],
           )


       return user

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email')

