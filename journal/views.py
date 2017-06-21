from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from journal.models import Journal
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

class JournalHome(View):

    def get(self, request):
        context = {}
        context['authenticated'] = False
        if request.user.is_superuser:
            context['authenticated'] = True
        return render(request, 'journal/index.html', context)

    def post(self, request):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=403)
        try:
            content = request.POST.get('content', '').strip()
            if not content: raise Exception('content')

            journal = Journal.objects.create(content=content)
            return JsonResponse({})
        except Exception as e:
            resp = {'message': 'Missing or invalid value for "{}" field'.format(e.args[0])}
            return JsonResponse(resp, status=400)

RESULTSIZE = 10
def get_journal(request):
    if not request.user.is_superuser:
        return JsonResponse({}, status_code=403)
    filtercrit = {}
    try:
        offset = int(request.GET.get('offset'))
    except:
        offset = 0

    resp = {'more':False}
    resp['items'] = []

    journals = Journal.objects.filter(**filtercrit)[offset*RESULTSIZE:(offset+1)*RESULTSIZE]
    if not journals:
        resp['more'] = False
    else:
        resp['more'] = True

    for journal in journals:
        resp['items'].append({'id':journal.id, 'content':journal.content,
                'created_date': journal.created_date
            })
    return JsonResponse(resp)
