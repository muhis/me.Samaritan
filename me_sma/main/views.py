from django.shortcuts import render
from django.http import HttpResponse
from main.models import code
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from main.requestInterpreter import is_okay
# Create your views here.
def codeview(request, var):

    if code.objects.filter(code=var).exists():
        info = code.objects.get(code = var)
        template = loader.get_template('main/codeview.html')
        context = {
        'name' : info.name(),
        'phone' : info.phone(),
        'email' : info.email(),
        'address' : info.address(),
        }
        return HttpResponse(template.render(context, request))
    else:
        #404
        pass
def create(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        data = request.POST.getlist('check')

        return redirect(is_okay(data))
    pass
def new(request):
    context = {}
    template = loader.get_template('main/create.html')
    return render(request, 'main/create.html', context)
