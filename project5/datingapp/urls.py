from django.urls import path
from.import views

urlpatterns = [
    path('home/', views.homefn),
    path('about/',views.aboutfn),
    path('contact/',views.contactfn),
         
]
