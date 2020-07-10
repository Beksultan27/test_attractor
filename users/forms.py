from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class UserCreationModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'gender', 'bio', 'location')

