from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
	STATUS_CHOICE = (
		('draft', 'Draft'),
		('published', 'Published')
	)
	title = models.CharField(max_length=250)
	image = models.ImageField(null = True, blank = True)
	slug = models.SlugField(max_length=250,
						    unique_for_date='publish')
	author = models.ForeignKey(User,
						   	   on_delete=models.CASCADE,
						   	   related_name='blog_posts')
	body = RichTextField(blank=True, null=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,
						  	  choices=STATUS_CHOICE,
						  	  default='draft')
	tags = TaggableManager()


	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	objects = models.Manager()
	published = PublishedManager()

	def get_absolute_url(self):
		return reverse('blog:post_detail',
						args=[self.publish.year,
							  self.publish.strftime('%m'),
							  self.publish.strftime('%d'),
							  self.slug])
	@property
	def image_url(self):
		if self.image:
			return getattr(self.image, 'url', None)
		return None




class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,
							 related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField(blank=True,  max_length=100)
	body = RichTextField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return f'Comment added by {self.name} for post {self.post}'