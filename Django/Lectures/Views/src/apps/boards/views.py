from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from apps.boards.models import Comment


class CreateCommentView(generic.CreateView):
    model = Comment
    fields = ["message"]

    template_name = 'boards/create_comment_form.html'
    success_url = reverse_lazy('home:home-page')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.task = self.request.user.tasks.last()
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteComment(generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('home:home-page')
    template_name = 'boards/delete_comments.html'

    def get_queryset(self):
        return super(DeleteComment, self).get_queryset().filter(created_by=self.request.user)
