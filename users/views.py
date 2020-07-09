from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationModelForm, ProfileForm
from .models import Profile

User = get_user_model()


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'user.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationModelForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationModelForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'message': 'Logged out'})


class ProfileObjectMixin(object):
    model = Profile
    lookup = 'id'

    def get_object(self, *args, **kwargs):
        return self.model.objects.get_auth_profile(
            self.kwargs.get(self.lookup),
            self.request.user
        )


class ProfileDetailView(DetailView):
    queryset = Profile.objects.all()
    context_object_name = 'profile'
    template_name = 'profile_detail.html'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Profile, pk=self.kwargs.get('id'))

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = self.get_object().first_name
        return context


class ProfileDeleteView(LoginRequiredMixin, ProfileObjectMixin, DeleteView):
    queryset = Profile.objects.all()
    context_object_name = 'profile'
    template_name = 'profile_delete.html'

    def get_context_data(self, *args, **kwargs):
        if self.get_object():
            context = super(ProfileDeleteView, self).get_context_data(*args, **kwargs)
            context['title'] = 'Delete Profile'
            return context

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'Profile has been deleted successfully!')
        return reverse('index')


class ProfileUpdateView(LoginRequiredMixin, ProfileObjectMixin, UpdateView):
    queryset = Profile.objects.all()
    context_object_name = 'profile'
    template_name = 'profile_update.html'
    form_class = ProfileForm

    def get_context_data(self, *args, **kwargs):
        if self.get_object():
            context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
            context['title'] = 'Update Profile'
            return context

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'Profile has been updated successfully!')
        return reverse(
            'profiles-detail', kwargs={'id': self.get_object().pk}
        )
