from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def book_list(request):
    book = Book.objects.all()
    return render(request, 'blog_posts/post_list.html', {'object_list': book})


def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'blog_posts/post_form.html', {'object': book})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'blog_posts/post_form2.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'blog_posts/post_delete.html', {'object': book})
