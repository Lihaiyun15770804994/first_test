from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^sendsms/$',views.sendsms,name='sendsms'),
    url(r'^logout/$',views.logout,name='logout'),
]