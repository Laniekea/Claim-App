from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AddClaimForm(forms.Form):
	username = forms.CharField(label="name", max_length=200)
	email = forms.CharField(label="email", max_length=200)
	mobile = forms.CharField(label="mobile", max_length=100)

	
	