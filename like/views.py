from django.views import generic
from .models import Like


class LikeCreate(generic.CreateView):

    model = Like
    fields = ()
