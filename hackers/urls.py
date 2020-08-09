from django.urls import path

from . import views

app_name = 'hackers'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /candidates/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /candidates/5/results/
    path('<int:pk>/results/', views.DetailView.as_view(), name='results'),
    # ex: /candidates/5/vote/
    path('<int:candidate_id>/vote/', views.vote, name='vote'),
]