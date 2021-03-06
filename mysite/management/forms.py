from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db.transaction import commit
from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError


class AddadminForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(required=False, label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  forms.ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  forms.ValidationError("Email already exists")
        return email
 
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
 
        if password1 and password2:
            if password1 != password2:
                print('dont match')
                raise forms.ValidationError("Password don't match")
        # return password2
 
    def save(self, commit=True):
        user = User.objects.create_superuser(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    username.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password1.widget.attrs.update({'class': 'form-control'})
    password2.widget.attrs.update({'class': 'form-control'})


class AdminSearchForm(forms.Form):
    username = forms.CharField(label='ชื่อผู้ใช้งาน', min_length=4, max_length=150, required=False)

    username.widget.attrs.update({'class': 'form-control'})


class CreateVMForm(forms.Form):
    vm_amount = forms.IntegerField(label='จำนวน VM ที่ต้องการสร้าง', required=False)

    def clean_vm_amount(self):
        vm_amount = self.cleaned_data['vm_amount']
        try:
            if vm_amount <= 0:
                raise  forms.ValidationError("จำนวน Virtual Machine ที่ต้องการสร้างต้องมากกว่า 0")
            return vm_amount
        except TypeError:
            raise  forms.ValidationError("กรุณาใส่จำนวน Virtual Machine ที่ต้องการก่อนกดสร้าง")
            return vm_amount

    vm_amount.widget.attrs.update({'class': 'form-control'})