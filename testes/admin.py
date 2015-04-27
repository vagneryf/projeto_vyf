from django.contrib import admin
from django import forms
from .models import Teste, Tag
from categorias.models import Categoria
# from easy_select2 import select2_modelform
from easy_select2 import select2_modelform_meta, Select2TextInput
from easy_select2 import select2_modelform

# Register your models here.


# class TesteAdmin(admin.ModelAdmin):
#   list_display = ('titulo','publicacao','categoria',)
#   fieldsets = [
#       (None, {'fields': ['titulo']}),
#       ('Data publicacao', {'fields': ['publicacao']}),
#       ('Texto', {'fields': ['conteudo']}),
#       ('Categoria',{'fields':['categoria']})

#   ]
#   list_filter = ['publicacao','categoria']
#   search_fields = ['titulo']

    # class Media:
    #   js = [
    #       '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
    #       '/static/tinymce_setup.js',
    #   ]

TesteForm = select2_modelform(Teste, attrs={'width': '350px'})


# class TesteAdminForm(forms.ModelForm):
#     Meta = select2_modelform_meta(Teste)

#     def __init__(self, *args, **kwargs):
#         super(TesteAdminForm, self).__init__(*args, **kwargs)

        #
        # Let's create the *current* list of choices for the tag field. By
        # putting this code here, it will ensure that the list is up-to-date
        # for each usage of the form.
        #
        # Also, you could personalize the experience by filtering the query to
        # only those Notes previously edited by this user. The effect would be
        # that each project Admin would see only their personal list of moods
        # that they've used in the past.
        #
        # You should note, that we are using denormalized table
        # structure there, what perfectly solves the problem.
        #
        # tag_data = Teste.objects.values_list('tag', flat=True).order_by('tag')

        # self.fields['tag'].widget = Select2TextInput(select2attrs={
        #     #
        #     # This is how Select2 expects the list of choices.
        #     #
        #     'data': [{'id': x, 'text': x} for x in tag_data]
        # })


class TesteAdmin(admin.ModelAdmin):
    form = TesteForm

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

admin.site.register(Tag)
admin.site.register(Teste, TesteAdmin)