from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import Postform

# Create your views here.


def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = Postform(request.POST)
        # if the form is valid
        if form.is_valid():
            # Yes, save
            form.save()
            # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all the post, limit 20.
    post = Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html', {'posts': post})


# Delete function
def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
