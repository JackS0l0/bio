from django.shortcuts import render
from .models import Books, İnfo
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# @login_required
def home(request):
    data={
        'title': 'Biologiya - Quliyeva Suqra',
        'books': Books.objects.all(),
    }
    return render(request,'home.html',data)
# @method_decorator(login_required, name='dispatch')  # Apply login_required to the class-based view
class DetailBook(DetailView):
    model = Books
    context_object_name = 'books'
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        data=super(DetailBook,self).get_context_data()
        data['title']=Books.objects.get(pk=self.kwargs['pk'])
        data['books']=Books.objects.all()
        return data