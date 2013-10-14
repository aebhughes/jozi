from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length = 255)
	location = models.CharField(max_length = 255)
	exDate = models.DateField()
	slug = models.SlugField(unique = True, max_length = 255)
	description = models.CharField(max_length = 255)
	content = models.TextField(default='<img border="0" src="" alt="Pulpit rock" width="250" height="300">')
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)

class Meta:
	ordering = ['-exDate']

def __unicode__(self):
	return u'%s' % self.title

def get_absolute_url(self):
	return reverse('blog.views.post',args = [self.slug])

# Create your models here.
