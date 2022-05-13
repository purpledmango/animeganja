from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.Homepage, name ='homepage'),
    path('home/<slug:slug>/', views.SingleAnimePost.as_view(), name ='single_post'),
	path('watch/<slug:ep_slug>/', views.Stream_page, name ='stream_page'),
	path('search_result/', views.search, name ='search_result'),
	path('all_animes/', views.all_animes, name ='all_animes'),
	path('contact_us/', views.contact_us, name ='contact_us'),
	path('thank_you/', views.thanks, name ='thanks'),
	path('movies/', views.movies, name ='movies'),

]

