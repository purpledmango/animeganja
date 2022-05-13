from django.db import models
from autoslug import AutoSlugField
from optimized_image.fields import OptimizedImageField

View = [
    ('Sub', 'SUB'),
    ('Dub', 'DUB'),
    ]

class Episodes(models.Model):
    description = models.CharField(max_length = 200,null = True, verbose_name = 'Descripton', help_text = 'Add the name of of the anime and the Episode no. (Eg: One Punch Man S1E1)')
    ep_slug = AutoSlugField(populate_from = 'description')
    episode_no = models.IntegerField(null = True, verbose_name = 'Episode no.')
    link = models.CharField(max_length = 5000, verbose_name = 'Link', help_text = 'Enter the link of the episode')
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name_plural = 'Episodes'
        ordering = ['date']

class NewAnime(models.Model):
    title = models.TextField(null = True, max_length = 80, verbose_name = 'Title', help_text = 'Enter the official Name of the Anime')
    slug = AutoSlugField(populate_from = 'title')
    thumbnail = OptimizedImageField(null =  True, blank =  True, upload_to = 'media/' ,verbose_name = 'Thumbanail', help_text = 'Upload the Official Anime Poster')
    thumbnail_url = models.CharField(null = True, max_length = 2000, verbose_name = 'Thumbnail url', help_text = 'Provide the link for the official Poster (Google it!)')
    description = models.TextField(null = True, max_length = 1500, verbose_name = 'Descripton', help_text = 'A breif summary about the Anime')
    language = models.CharField(null = True, max_length = 8, choices = View, default = "SUB", verbose_name = 'Language')
    genre= models.CharField(null = True, max_length = 80, verbose_name = 'Genre/Categories', help_text =  'Add Genres or tags seperated by a commar (Eg: Shounen, Horror)')
    episodes = models.ManyToManyField(Episodes)
    similar_shows = models.ManyToManyField('self', blank = True, verbose_name = 'Similar', help_text = 'Add similar shows like this one to be shown as recommended')
    date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Animes'
        ordering = ['-date']  



class Movies(models.Model):
    title = models.TextField(null = True, max_length = 80, verbose_name = 'Title', help_text = 'Enter the official Name of the Anime')
    slug = AutoSlugField(populate_from = 'title')
    thumbnail = OptimizedImageField(null =  True, blank =  True, upload_to = 'media/' ,verbose_name = 'Thumbanail', help_text = 'Upload the Official Anime Poster')
    thumbnail_url = models.CharField(null = True, max_length = 2000, verbose_name = 'Thumbnail url', help_text = 'Provide the link for the official Poster (Google it!)')
    description = models.TextField(null = True, max_length = 1500, verbose_name = 'Descripton', help_text = 'A breif summary about the Anime')
    language = models.CharField(null = True, max_length = 8, choices = View, default = "SUB", verbose_name = 'Language')
    genre= models.CharField(null = True, max_length = 80, verbose_name = 'Genre/Categories', help_text =  'Add Genres or tags seperated by a commar (Eg: Shounen, Horror)')
    link = models.CharField(max_length = 5000, verbose_name = 'Link', help_text = 'Enter the link of the movie')
    similar_shows = models.ManyToManyField('self', blank = True, verbose_name = 'Similar', help_text = 'Add similar shows like this one to be shown as recommended')
    date = models.DateTimeField(auto_now = True) 


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['-date']  



class Banner(models.Model):
    title = models.TextField(null = True, max_length = 80, verbose_name = 'Title', help_text = 'Enter the official Name of the Anime')
    slug = AutoSlugField(populate_from = 'title')
    thumbnail = OptimizedImageField(null =  True, blank =  True, upload_to = 'media/' ,verbose_name = 'Thumbanail', help_text = 'Upload the Official Anime Poster')
    thumbnail_url = models.CharField(null = True, max_length = 2000, verbose_name = 'Thumbnail url', help_text = 'Provide the link for the official Poster (Google it!)')
    date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Image Banner'
        ordering = ['-date'] 


class Contacts(models.Model):
    full_name = models.TextField(null = True, max_length = 80, verbose_name = 'Name')
    message = models.TextField(null = True, max_length = 2000, verbose_name = 'Message')
    email = models.CharField(null = True, max_length = 2000, verbose_name = 'Sender Email')
    time = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = 'Contacts'
        # ordering = ['-date']  

