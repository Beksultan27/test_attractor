from django.urls import path
from . import views
from .views import (
    ProfileDetailView,
    ProfileDeleteView,
    ProfileUpdateView
)


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:id>/detail/', ProfileDetailView.as_view(), name='profiles-detail'),
    path('<int:id>/delete/', ProfileDeleteView.as_view(), name='profiles-delete'),
    path('<int:id>/update/', ProfileUpdateView.as_view(), name='profiles-update'),

]
