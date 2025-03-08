from django.urls import path
# from book.views import home,store_book,edit_book,delete_book
from . import views
urlpatterns = [
    path('',views.MyTemplateView.as_view(template_name='home.html')),
    path('store_new_book/',views.store_book,name='storebook'),
    # path('show_books/',show_books,name='show_books'),
    path('show_books/',views.BookListView.as_view(),name='show_books'),
    path('book_details/<int:id>',views.BookDetailsView.as_view(),name='book_details'),
    path('edit_book/<int:id>',views.edit_book,name='edit_book'),
    path('delete_book/<int:id>',views.delete_book,name='delete_book'),
]