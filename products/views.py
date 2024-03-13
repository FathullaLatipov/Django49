from django.shortcuts import render

from products.models import CategoryModel


def home_page(request):
    categories = CategoryModel.objects.all()
    context = {'categories': categories}
    return render(request, template_name='index.html', context=context)
