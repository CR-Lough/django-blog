from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Post.objects.filter(publisher=self.publisher)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        context = {"object": post}
        return render(request, "blogging/detail.html", context)