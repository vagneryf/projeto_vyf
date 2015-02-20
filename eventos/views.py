# -*- coding: utf-8 -*-
import datetime
# from datetime import timedelta # << se usar esse import nao precisa datetime.timedelta apentas timedelta
from django.shortcuts import render
from django.views import generic
from .models import Evento
from django.utils import timezone
from categorias.models import Categoria
import calendar

def eventos_index(request):
	eventos_list =  Evento.objects.all().order_by('-data_inicio')
	ano = request.GET.get('ano',)
	mes = request.GET.get('mes',)
	dia = request.GET.get('dia')
	tempo = request.GET.get('tempo',)
	tempoa = request.GET.get('tempoa')

	anos_list = range(2009,2021)
	meses_list = calendar.month_name # << receber mes em texto
	dias_list = range(1,32)
	
	em_andamento = request.GET.get('em_andamento',)

	if ano:
		if ano not in [str(x) for x in range(2009,2051)]:
			#raise ValueError('erro ano')
			ano = timezone.now().year
		eventos_list = eventos_list.filter(data_inicio__year=ano)
	if mes:
		if mes not in [str(x) for x in range(1,13)]:
			mes = timezone.now().month
		eventos_list = eventos_list.filter(data_inicio__month=mes)
	if dia:
		if dia not in [str(x) for x in range(1,32)]:
			dia = timezone.now().day
		eventos_list = eventos_list.filter(data_inicio__day=dia)
	if tempo:
		# try:
		# 	tempot = int(tempo)
		# except ValueError: 
		# 	tempot = 30
		# except OverflowError:
		# 	tempot = 1
		# 	print tempot, type(tempot)
		# except Exception, e:
		# 	raise e
		tempot = tempo

		if tempot not in [str(x) for x in range(0,365)]:
			tempot = 365
			# raise ValueError('Bosta')
		# if tempot not in range(0,31):
		# 	raise ValueError('Foda-se')

		tempox = timezone.now()
		tempoy = tempox+datetime.timedelta(days=tempot)
		eventos_list = eventos_list.filter(data_inicio__range=(tempox,tempoy))
		# eventos_list = eventos_list.filter(data_inicio__range=(timezone.now(),timezone.now()+datetime.timedelta(days=int(tempo))))

	if tempoa:
		tempoa = int(tempoa)
		tempoz = timezone.now()
		tempow = timezone.now()+datetime.timedelta(days=tempoa)
		eventos_list = eventos_list.filter(data_inicio__gte=tempoz)
		eventos_list = eventos_list.filter(data_inicio__lte=tempow)
		# eventos_list = eventos_list.exclude(data_inicio__gte=tempow)

	# if em_andamento:
	# 	eventos_list.evento = 1 #eventos_list.evento_em_andamento()
	# 	eventos_list = eventos_list.filter(evento=1)


	return render(request, 'eventos/index.html',{
		'eventos_list': eventos_list,
		'anos_list': anos_list,
		'meses_list': meses_list,
		'dias_list': dias_list,
		'em_andamento': em_andamento,
		'categorias_list': Categoria.objects.all(),
		})


#  Generic Class View para a lista de eventos:
# class IndexView(generic.ListView):
# 	template_name = 'eventos/index.html'
# 	context_object_name = 'eventos_list'

# 	def get_queryset(self):
# 		return Evento.objects.all().order_by('-data_inicio')[:10]

class DetailView(generic.DetailView):
	model = Evento
	template_name = 'eventos/detail.html'
