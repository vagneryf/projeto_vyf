import datetime
from django.db import models

from django.db import models
from django.utils import timezone
from artigos.models import Artigo

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('data published')
	artigo = models.ForeignKey(Artigo)

	def __unicode__(self):
		return self.question_text

	def was_published_recently(self):
		# return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		#abaixo a correcao feita apos o tests.py
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	# abaixo a personalizacao do Question no admin
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True 
	was_published_recently.short_description = 'Published recently?'


		

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text



