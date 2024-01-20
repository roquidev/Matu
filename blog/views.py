from django.shortcuts import render, get_object_or_404
from .models import Post


# Renderiza todas las publicaciones o posts
def render_post(request):
    posts = Post.objects.all()
    # posts = get_object_or_404(Post, profile=request.user.id)
    return render(
        request=request,
        template_name="homepage/blog.html",
        context={
            "posts": posts,
        }
    )


# Renderiza cada una de las publicaciones o un post específico
def render_post_detail(request, post_id):
    post = get_object_or_404(Post,  id=post_id)

    return render(
        request=request,
        template_name="homepage/post_detail.html",
        context={
            "post": post
        }
    )
