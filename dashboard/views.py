
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.db.models import Q
from .models import NewAnime, Episodes, Banner, Contacts, Movies
from django.core.paginator import Paginator
from django.utils import timezone


# Homepage
def Homepage(request):
	anime_object = NewAnime.objects.all()
	epsiodes_object = Episodes.objects.all()[:3]
	banner_ = Banner.objects.get(id=1)
	banner = banner_.thumbnail	
	paginator = Paginator(anime_object, 12)
	page = request.GET.get('page')

	#?page=2

	shows = paginator.get_page(page)

	context = {'shows' : shows, 'episodes': epsiodes_object, 'banner': banner}

	return render(request, 'home.html', context)


## A single anime with all the episode button
class SingleAnimePost(DetailView):
	model = NewAnime
	template_name = 'single_post.html'


#the streaming page
def Stream_page(request, ep_slug):
	single_episode = Episodes.objects.get(ep_slug = ep_slug)
	episode_description = single_episode.description
	episode_link = single_episode.link

	context = {'episode_description' : episode_description, 'episode_link' : episode_link}
	return render(request, 'stream.html', context)

## search bar
def search(request):
	if request.method == 'POST':
		searches = request.POST['searches']
		if searches:
			result = NewAnime.objects.filter(Q(title__icontains = searches) | Q(description__startswith = searches))
			print(result)
			if result:
				return render(request, 'search_result.html', {'result' : result, 'searches' : searches})
			
			else:
				return render(request, 'no_result_page.html')

		else:
			return render(request, 'search_result.html')


## All animes list
def all_animes(request):
	all_animes = NewAnime.objects.order_by('title')
	context = {'all_animes': all_animes}
	return render(request, 'all_animes.html', context)

#Genres
def genres(request):
	action = NewAnime.objects.filter(Q(genre__icontains = 'Action'))
	fantasy = NewAnime.objects.filter(Q(genre__icontains = 'Fantasy'))
	horror = NewAnime.objects.filter(Q(genre__icontains = 'Horror'))
	mecha = NewAnime.objects.filter(Q(genre__icontains = 'Mecha'))
	scifi = NewAnime.objects.filter(Q(genre__icontains = 'Sci Fi'))

	context = {action: 'action', fantasy: 'fantasy', horror: 'horror', mecha: 'mecha', scifi: 'scifi' }

	return render (request, 'genre.html', context)


def contact_us(request):
	if request.method == 'POST':
		full_name = request.POST['names']
		message = request.POST['message']
		email = request.POST['email']
		

		form = Contacts(full_name = full_name, message = message, email = email, time=timezone.now())
		form.save()

	

	return render(request, 'contact_us.html')


def thanks(request):
	return render(request, 'thanks.html')


def movies(request):
	movie = Movies.objects.all()

	context = {'movies': movie}

	return render(request, 'movies.html', context)