from django.shortcuts import render,redirect
from django.http import HttpResponse
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
# Create your views here.


#function based view
# def home(request):
#     return render(request, 'store_book.html')

class MyTemplateView(TemplateView):
    template_name ='home.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context = {'title': 'Home Page'}
        return context
    


# def store_book(request):
#   if request.method == 'POST':
#     book = BookStoreForm(request.POST)
#     if book.is_valid():
#         book.save()
#         print(book.cleaned_data)
#         redirect('show_books')
#     return render(request, 'store_book.html', {'form': book})
        
#   else:
#     book = BookStoreForm()
#     return render(request, 'store_book.html',{'form':book})



class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
 
    
    
    
    


# def show_books(request):
#     book = BookStoreModel.objects.all()
#     for item in book:
#         print(item.first_pub)
#     print(book)
#     return render(request, 'show_book.html', {'data': book})

class BookListView(ListView):
    model = BookStoreModel
    template_name ='show_book.html'
    context_object_name = 'booklist' 
    
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author_name='Humayun')
    
    # def get_context_data(self, **kwargs):
    #    context =  super().get_context_data(**kwargs)
    #    context = {'Rahim':BookStoreModel.objects.all().order_by('author_name') }
    #    return context
    
    ordering = ['id']  # desecnding ordering
    
   
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    
    
    
    

def edit_book(request,id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == 'POST':
     form = BookStoreForm(request.POST,instance = book)
     if form.is_valid():
        form.save()
        return redirect('show_books')
    
    
    return render(request, 'store_book.html',{'form':form})




def delete_book(request,id):
    book = BookStoreModel.objects.get(pk = id).delete()

    return redirect('show_books')
    
    
   
    
    
    