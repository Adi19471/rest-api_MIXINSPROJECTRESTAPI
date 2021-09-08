from django.urls import path 

from mixinapp import views 

urlpatterns = [
    path('rest-api/',views.EmployeListView.as_view()),
    path('<int:pk>/',views.EmployeDetaileView.as_view()),
]