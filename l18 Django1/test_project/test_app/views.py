from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from test_app.form import MyForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'GET':
        return  render(request, 'test_app/index.html',
        {'name':'Kirill'})

class MyView(View):
    def get(self, request):
        form = MyForm();
        c = {'form':form}
        return render(request, 'test_app/form.html', c)

    def post(self, request):
        form = MyForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
        else:
            messages.error(request, 'Validation failed')

        c = {'form': form}
        return render(request, 'test_app/form.html', c)

