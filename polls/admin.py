from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.

# Chamar o choice de forma ideal:
# Class ChoiceInline(admin.StackedInline):  <<para deixar as opcoes sem colunas
class ChoiceInline(admin.TabularInline): #<< para deixar as opcoes com colunas e ganhar mais espaco na tela
	model = Choice
	extra = 3 #quantidade de slots para cada questao

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Artigo',{'fields': ['artigo']}),
		('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	# personalizar o Question
	list_display = ('question_text', 'pub_date', 'was_published_recently', 'artigo',) # por padrao o campo "was_published" sera apresentado como "was published" substituindo automaticamente os _ por espaco
	# obs. para ver a personalizacao do Question ver em models.py

	list_filter = ['pub_date'] # adicionar filtro na listagem

	search_fields = ['question_text'] # adicionar campo de busca para o campo question_text

admin.site.register(Question, QuestionAdmin)
# Chamar o choice de forma simples: admin.site.register(Choice)
