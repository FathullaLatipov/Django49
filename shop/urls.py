from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from products.views import HomePage, MyLoginView, logout_view, search, product_page, category_page, \
    add_products_to_user_cart, user_cart, delete_user_cart

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', MyLoginView.as_view()),
    path('logout/', logout_view),
    path('search', search),
    path('products/<int:pk>', product_page),
    path('category/<int:pk>', category_page),
    path('add_to_cart/<int:pk>', add_products_to_user_cart),
    path('user_cart/', user_cart),
    path('delete_cart/<int:pk>', delete_user_cart),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
