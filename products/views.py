from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from products.models import CategoryModel, ProductModel


def home_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='index.html', context=context)


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')