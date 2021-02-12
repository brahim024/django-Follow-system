from django.urls import path
from .views import ProfileListView,ProfileDetail

app_name='profiles'

urlpatterns=[
	path('',ProfileListView.as_view(),name='profile-list-view'),
	path('<pk>/',ProfileDetail.as_view(),name='profile-detail-view'),
]