from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    book = Book.objects.all()
    return render(request, 'blog_posts/post_list.html', {'object_list': book})


def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'blog_posts/post_form.html', {'object': book})
