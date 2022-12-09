from django.shortcuts import render
import datetime
from django.http import HttpResponse
from energy.models import Service, Data_transfer, News
from .forms import InputForm, ServiceForm, SearchForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework import routers, serializers, viewsets
from django_filters import FilterSet

# Create your views here.
def service_list1(request):
    form = InputForm(request.GET)
    search = request.GET.get('search', '')
    service_list = Service.objects.all()
    transfer_list = Data_transfer.objects.all()
    if search:
        service_list = service_list.filter(service_name__icontains=search)
        transfer_list = transfer_list.all()
    if form.is_valid():
        new_value = form.cleaned_data['new_value']
#        element = Data_transfer(user= , date= , value=new_value)
#        element.save()
#        return render(request, 'confirmation.html')
        pass
    else:
        form = InputForm()
    context = {
        'service_list': service_list,
        'transfer_list': transfer_list,
        'form': form,
        'errors': form.errors,
    }
    return render(request, 'values_transfer.html', context)

def get_queryset(self):
     queryset = super().get_queryset()
     queryset = queryset.filter(user_service__user=self.request.user)
     return queryset

def transfer_list(self):
    context = {
        'transfer_list': transfer_list
    }
    return render(self, 'autorith_page.html', context)


class SearchFormMixin:
    filter_form = None
    filter_form_class = None
    def get_filter_form(self):
        if self.filter_form is None:
            self.filter_form = SearchForm(self.request.GET)
        return self.filter_form
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.get_filter_form()
        if form.is_valid():
            for key,val in form.cleaned_data.items():
                if val:
                    queryset = queryset.filter(**{key: val})
        return queryset
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.get_filter_form()
        return context

class ServiceList(ListView):
    model = Service
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_service__user=self.request.user)
        return queryset
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['value'] = Data_transfer.objects.order_by('-date').values('value')[:1]
        context['form_input'] = InputForm
        return context
    def input_value(request):
        if request.method == "POST":
            form = InputForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'confirmation.html')
            else:
                context = {
                    'form': form
                }
                return render(request, 'service_create.html', context)




def service_list(self):
    service_list = Service.objects.all()
    context = {
        'service_list': service_list
    }
    return render(self, 'service_list.html', context)


def start_list(self):
    context = {
        'start_list': start_list
    }
    return render(self, 'start.html', context)

class ServiceDetail(DetailView):
    model = Service
    fields = "__all__"



def service_detail(request, pk):
    service = Service.objects.get(id=pk)
    context = {
        'service': service
    }
    return render(request, 'service_detail.html', context)

class ServiceCreate(CreateView):
    model = Service
    #fields = ('service_name',"site",'personal_account')
    #success_url = 'confirmation'
    form_class = ServiceForm
    def get_context_data(self, *args,**kwargs):
        form = ServiceForm
        context = super().get_context_data(*args,**kwargs)
        context['form'] = form
        return context

def service_create(request):
    if request.method == "GET":
        form = ServiceForm()
        context = {
            'form': form
        }
        return render(request, 'service_create.html', context)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            context = {
                'form': form
            }
            return render(request, 'service_create.html', context)




class ServiceUpdate(UpdateView):
    model = Service
    template_name_suffix = '_form_update'
    form_class = ServiceForm



def service_update(request,pk):
    if request.method == "GET":
        service = Service.objects.get(id=pk)
        form = ServiceForm(instance=service)
        context = {
            'form': form
        }
        return render(request, 'service_create.html', context)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'service_create.html', context)

def confirmation(self, request):
    context = {'confirmation': confirmation}
    return render(self, 'confirmation.html', context)

class NewsList(SearchFormMixin, ListView):
    model = News
    filter_form_class = SearchForm


def news_list_json(request):
    form = SearchForm(request.GET)
    news_list = News.objects.all()
    if form.is_valid():
        for key, val in form.cleaned_data.items():
            if val:
                news_list = news_list.filter(**{key: val})
    res = []
    for news in news_list:
        res.append({
            'id': news.id,
            'title': news.title,
            'date_posted': news.date_posted,
            'content': news.content,
        })
    return JsonResponse(res, safe=False)

class NewsSetFilter(FilterSet):
    class Meta:
        model = News
        fields = '__all__'
        exclude = []

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'date_posted', 'content' ]

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsSetFilter


class DataTransferSetFilter(FilterSet):
    class Meta:
        model = Data_transfer
        fields = '__all__'
        exclude = []

class DataTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_transfer
        fields = ['user_transfer', 'date', 'value']

class DataTransferViewSet(viewsets.ModelViewSet):
    queryset = Data_transfer.objects.all()
    serializer_class = DataTransferSerializer
    filterset_class = DataTransferSetFilter
