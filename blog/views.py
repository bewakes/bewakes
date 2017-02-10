from django.shortcuts import render, get_object_or_404, Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from blog.models import Article, Tag, Comment
from datetime import datetime
import json

# Create your views here.

class Home(View):
    context = {}
    tags = None # for tag cloud

    # def __init__(self): # to populate with the tag clouds
        # recents = Article.objects.filter(publish=True).order_by('-published_date')
        # if len(recents) > 10:
            # recents = recents[10]
    #     self.context['recent_posts'] = recents

    def get(self, request, slug=None):

        filterargs = {'publish':True}
        if request.user.is_superuser:
            filterargs = {}

        article = None
        previous_article = None
        next_article = None
        if not slug: # means the default blog page, get latest article
            try: # in case no articles are there
                articles = Article.objects.filter(**filterargs).order_by('-id')
                article = articles[0]
                if len(articles)>1:
                    previous_article = articles[1]
                next_article = None
            except Exception as e:
                return HttpResponse('no articles present:') 
        else:
            article = get_object_or_404(Article, slug=slug)
            if not article.publish and not request.user.is_superuser: raise Http404
            article.visits+=1
            article.save()
            articles = Article.objects.filter(**filterargs).order_by('-published_date')
            count = articles.count()
            index = list(articles).index(article)

            if index==len(articles)-1:
                previous_article = None
                next_article = None if index-1< 0 else articles[index-1]
            elif index==0:
                next_article = None
                previous_article = None if index+1 >= len(articles) else articles[index+1]
            else:
                next_article = articles[index-1]
                previous_article = articles[index+1]

        self.context['next_article'] = next_article
        self.context['previous_article'] = previous_article
        article_tags = Tag.objects.filter(article=article)
        self.context['article_tags'] = article_tags
        self.context['article'] = article
        self.context['tags'] = self.tags
        comments = Comment.objects.filter(article=article)
        self.context['comments'] = comments

        return render(request, 'blog/index.html', self.context)

class CommentProcess(View):
    def post(self, request):
        user = request.POST.get('name', '')
        comment = request.POST.get('comment', '')
        slug = request.POST.get('slug', '')
        if user!='' and comment!='' and slug!='':
            article = get_object_or_404(Article, slug=slug)
            Comment.objects.create(username=user, text=comment, comment_date=datetime.now(), article=article)
        return HttpResponseRedirect(reverse('home', args=(slug,)))

    def get(self, request):
        return HttpResponse('ulala')

class About(View):
    def get(self, request):
        return render(request, 'blog/about.html', {})

class Contact(View):
    def get(self, request):
        return render(request, 'blog/contact.html', {})

class Posts(View):
    def get(self, request):
        tagname = request.GET.get('tag', '')
        query = request.GET.get('q', '')

        filterpublish = {'publish':True}
        if request.user.is_superuser: filterpublish = {}

        context = {}

        search = False
        if tagname or query:
            search = True


        articles = []
        if tagname:
            context['searchtext'] = 'for tag "{}"'.format(tagname)
            if len(tagname) > 3:
                articles = Article.objects.filter(**filterpublish).\
                    filter(tag__name__icontains=tagname).\
                    order_by('-published_date')
        elif query:
            context['searchtext'] = 'for query "{}"'.format(query)
            if len(query)>=5:
                articles = Article.objects.filter(**filterpublish).\
                    filter(publish=True, title__icontains=query).\
                    order_by('-published_date')

        if not search:
            articles = Article.objects.filter(**filterpublish)
        context['articles'] = articles

        return render(request, 'blog/search-list.html', context)

@csrf_exempt
def searchresult(request):
    # assumption is that method is post
    context = {}
    context['data']=[]
    query = request.GET.get('query','')
    if query=='':
        return HttpResponse(json.dumps(context))
    articles = Article.objects.filter(title__contains=query)
    if len(articles)!=0:
        art_list = []
        for article in articles:
            art = {}
            art['title'] = article.title
            art['slug'] = article.slug
            art_list.append(art)
        context['data'] = art_list
    jsontxt = json.dumps(context)
    return HttpResponse(jsontxt)
