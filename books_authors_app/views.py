from django.shortcuts import redirect, render
from .models import Book, Author

def index(request):
  print('\n --- index ---')
  # display all the books
  context = {
    'all_books' : Book.objects.all()
  }
  return render(request, 'index.html', context)

def authors_index(request):
  # display all the authors
  context = {
    'all_authors': Author.objects.all()
  }
  return render(request, 'authors_index.html', context)

def authors(request, id):
  # basically view author and add book to them but ¯\_(ツ)_/¯
  # display this author
  print('\n=====> ', id)
  context = {
    'this_author' : Author.objects.get(id=id),
    'all_the_books': Book.objects.all()
  }
  return render(request, 'authors.html', context)

def add_book(request):
  if request.method == "POST":
    if request.POST.get('title') and request.POST.get('desc'):
      print(request.POST)
      # altway
      book = Book()
      book.title = request.POST['title']
      book.desc = request.POST['desc']
      book.save()
  return redirect('/')

def add_author(request):
  if request.method == "POST":
    if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('notes'):
      print(request.POST)
      author_fn = request.POST['first_name']
      author_ln = request.POST['last_name']
      notes = request.POST['notes']
      
      Author.objects.create(first_name=author_fn, last_name=author_ln, notes=notes)
  return redirect('/authors_index')

def books(request, id):
  context = {
    'this_book' : Book.objects.get(id=id),
    'all_the_authors': Author.objects.all()
  }
  return render(request, 'books.html', context)

def add_author_to_curent_book(request):
  if request.method == "POST":
    if request.POST.get('author_to_add_id') and request.POST.get('from_book_id'):
      print('\n-'*20)
      print(request.POST)
      print(request.POST['author_to_add_id'], request.POST['from_book_id'])
      from_book_id = request.POST['from_book_id']
      author_to_add_id = request.POST['author_to_add_id']
      
      this_book_to_add_author = Book.objects.get(id=from_book_id)
      this_author_to_add = Author.objects.get(id=author_to_add_id)
      this_book_to_add_author.authors.add(this_author_to_add)
      
      print(f"Book.object.get(id=from_book_id).id->  {this_book_to_add_author}")
  return redirect(f"/books/{from_book_id}")
  # return redirect(f"/books/{request.POST['from_book_id']}")
  
def add_book_to_current_author(request):
  print(request.POST)
  if request.method == "POST":
    if request.POST.get('book_to_add_id') and request.POST.get('from_author_id'):
      from_author_id = request.POST['from_author_id']
      book_to_add_id = request.POST['book_to_add_id']
      
      this_author_to_add = Author.objects.get(id=from_author_id)
      this_book_to_add = Book.objects.get(id=book_to_add_id)
      this_author_to_add.books.add(this_book_to_add)
      
    
  return redirect(f'/authors/{from_author_id}')