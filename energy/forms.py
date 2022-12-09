import datetime
from django import forms
from energy.models import Service, Client, Data_transfer, News


class BootsrapModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class InputForm(BootsrapModelForm):
    model = Data_transfer
    value = forms.IntegerField(label='Введите значение', required=False)
    class Meta:
        model = Data_transfer
        fields = ('value', 'date', )

class ServiceForm(BootsrapModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class SearchForm(BootsrapModelForm):
    content__icontains = forms.CharField(label='Название счетчика', max_length=100, required=False)
    class Meta:
        model = News
        fields = ('content__icontains',)
    #date__gte =forms.DateField(
        #input_formats=['%d.%m.%Y','%Y-%m-%d'],
        #label='Дата',required=False)
    #service =forms.ModelChoiceField(queryset=Service.objects.all(),required=False)
    #typ = forms.ChoiceField(
        #choices = Article.TYPE_CHOICES,
        #required=False)