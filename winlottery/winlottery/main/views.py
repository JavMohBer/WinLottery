import shelve
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    list = {'loteria': ''}
    if 'bonoloto' in request.POST:
        print('lista de apuestas de bonoloto')
        list = {'loteria': 'lista de apuestas de bonoloto'}
    elif 'euro' in request.POST:
        print('gdhgdjhdjghdg')
        list = {'loteria': 'lista de apuestas de euromillones'}
    elif 'gordo' in request.POST:
        print('gdhgdjhdjghdg')
        list = {'loteria': 'lista de apuestas de gordoprimitiva'}
    elif 'primitiva' in request.POST:
        print('gdhgdjhdjghdg')
        list = {'loteria': 'lista de apuestas de primitiva'}

    return render(request, 'index.html', list)