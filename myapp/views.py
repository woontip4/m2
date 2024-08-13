from django.shortcuts import render
from .models import CategoryModel
# Create your views here.

def category_list(request):
          categories = CategoryModel.objects.all()
          return render(request, 'category_list.html', {'categories': categories})
