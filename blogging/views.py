from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    queryset = Post.objects.exclude(published_date__exact=None)

    def post(self, request, pk):
        try:
            post = self.get_object(queryset=queryset)
        except Post.DoesNotExist:
            raise Http404
        context = {'object': post}
        return render(request, 'blogging/detail.html', context)


def detail_view(request, post_id):

    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)