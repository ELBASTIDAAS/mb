from django.views.generic import ListView
from .models import Post
# Create your views here.


class PostListView(ListView):
    template_name = "posts/home.html"
    model = Post
