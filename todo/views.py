from django.shortcuts import render
from .models import Item
#from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
  item = Item(request, 'todo/todo_list.html')
  items = Item.objects.all()
  context = {
        'items': items
}

  return render(request, 'todo/todo_list.html', context)

  def add_item(request):
    if request.method == 'POST':
    
 # return redirect('get_movie_list')
   # form = ItemForm()
    #context = {
     #   'form': form
    #}
    #return render(request, 'todo/add_item.html', 
    #context)