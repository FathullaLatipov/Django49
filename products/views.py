from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from products.models import CategoryModel, ProductModel
from products.forms import SearchForm


def home_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    form = SearchForm
    context = {'categories': categories, 'products': products, 'form': form}
    return render(request, template_name='index.html', context=context)


class HomePage(ListView):
    form = SearchForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["products"] = ProductModel.objects.all()
        return context


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def search(request):
    if request.method == "POST":
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(product_title__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('/')


def product_page(request, pk):
    product = ProductModel.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product.html', context)


def category_page(request, pk):
    category = CategoryModel.objects.get(id=pk)
    current_products = ProductModel.objects.filter(product_category=category)
    context = {'product': current_products}
    return render(request, 'category.html', context)
