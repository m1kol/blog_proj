from django.views import generic

from .models import Comment


class CommentCreate(generic.CreateView):

    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.post = self.request.post_id
        return super(CommentCreate, self).form_valid(form)
