from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from til.models import TIL
from blog.models import Tag
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

class TILHome(View):

    def get(self, request):
        context = {}
        context['authenticated'] = False
        if request.user.is_authenticated():
            context['authenticated'] = True
        return render(request, 'til/index.html', context)

    def post(self, request):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=403)
        try:
            title = request.POST.get('title', '').strip()
            if not title: raise Exception('title')
            tags = request.POST.get('tags')
            tags = list(map(lambda x:x.strip(), tags.split(',')))
            tiltags = []
            for tag in tags:
                try:
                    t = Tag.objects.get(name__iexact=tag)
                    tiltags.append(t)
                except:
                    pass
            if not tiltags:
                raise Exception('tags')
            content = request.POST.get('content', '').strip()
            if not content: raise Exception('content')

            til = TIL.objects.create(title=title, content=content)
            til.tags.add(*tiltags)
            return JsonResponse({})
        except Exception as e:
            resp = {'message': 'Missing or invalid value for "{}" field'.format(e.args[0])}
            return JsonResponse(resp, status=400)

RESULTSIZE = 10
def get_til(request):
    # first check for tag filter
    retobjs = []
    filtercrit = {}
    try:
        offset = int(request.GET.get('offset'))
    except:
        offset = 0
    tagname = request.GET.get('tag')
    try:
        tag = Tag.objects.get(name_iexact=tagname)
        filtercrit['tag'] = tag
    except:
        pass

    resp = {'more':False}
    resp['items'] = []

    rand = request.GET.get('random')
    if rand:
        import random
        count = TIL.objects.count()
        r = random.randrange(1, count+1)
        til = TIL.objects.get(id=r)
        retobjs.append(til)
    else:
        tils = TIL.objects.filter(**filtercrit)[offset*RESULTSIZE:(offset+1)*RESULTSIZE]
        if not tils:
            resp['more'] = False
        else:
            resp['more'] = True

    for til in tils:
        resp['items'].append({'id':til.id,'title':til.title,'content':til.content,
                'tags':list(map(lambda x: x.name, til.tags.all()))
            })
    return JsonResponse(resp)
