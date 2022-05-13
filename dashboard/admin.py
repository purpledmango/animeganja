from django.contrib import admin
from .models import NewAnime, Episodes, Banner, Movies, Contacts

class EpisodesAdmin(admin.ModelAdmin):
	list_display = ('description',)
	search_fields = ['description']

class NewAnimeAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ['title']
	filter_horizontal = ['similar_shows', 'episodes']


class BannerAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ['title']

class MoviesAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ['title']
	filter_horizontal = ['similar_shows']

class ContactsAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'message','time')
	search_fields = ['message', 'name']

admin.site.register(NewAnime, NewAnimeAdmin)
admin.site.register(Episodes, EpisodesAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Contacts, ContactsAdmin)