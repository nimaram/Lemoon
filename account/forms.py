from django import forms
from django.contrib.auth import get_user_model

# getting user model
User = get_user_model()

class UserCreateFormAdmin(forms.ModelForms):

    password = forms.CharField(widget=forms.PasswordInput,label="رمز عبور")
    repeated_password = forms.CharField(widget=forms.PasswordInput,label="تایید رمز عبور") 
    
    class Meta:
        model = User
        exclude = ['password']

    # this method triggered when form submitted
    def clean_repeated_password(self):
        data = self.cleaned_data
        if data["password"] and data["repeated_password"] and data["password"] != data["repeated_password"]:
            raise forms.ValidationError("رمز و تایید آن باید یکی باشد")
        return data["repeated_password"]

    def save(self,commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user     
