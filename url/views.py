from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy

from .models import Bookmark


class Home(CreateView):
    model = Bookmark
    template_name = 'url/home.html'
    fields = ('description', 'endpoint', 'user')
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        bookmarks = Bookmark.objects.all()
        context['bookmarks'] = list(bookmarks)
        return context


class Redirect(View):
    def get(self, request, short_name):
        bookmark = get_object_or_404(Bookmark, short_name=short_name)
        return redirect(bookmark.endpoint)
