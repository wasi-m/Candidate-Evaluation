from django.urls import path
from .views import SignUpView
from . import views


app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('topresults/', views.allfivestarresults, name='topresults'),
    path('<str:candidate_email>/', views.detail, name='detail'),
    path('<str:candidate_email>/results/', views.results, name='results'),
    path('<str:candidate_email>/evaluate/', views.evaluate, name='evaluate'),
]