from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from products.models import ProductCategory
from products.forms import CategoryModelForm
from products.models import Product
from django.shortcuts import render, get_object_or_404


class ProductListView(ListView):
    model = Product
    template_name = 'categories/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все продукты'
        return context


class CategoryList(ListView):
    model = ProductCategory
    template_name = 'categories/index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('id')
        context['title'] = 'Категории'
        context['link_list'] = ['']
        context['menu'] = ProductCategory.objects.all()
        context['categories'] = ProductCategory.objects.all()  # Ensure categories are passed
        return context


class CategoryDetail(DetailView):
    model = ProductCategory
    template_name = 'categories/detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.object.category.all().order_by('name')
        paginator = Paginator(products, 10)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context['page_object'] = page_object
        context['categories'] = True  # Ensure this line is included
        return context


class CategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ProductCategory
    success_url = reverse_lazy('categories:main')
    login_url = reverse_lazy('accounts:login')

    form_class = CategoryModelForm
    template_name = 'categories/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser


class CategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('categories:main')
    login_url = reverse_lazy('accounts:login')

    form_class = CategoryModelForm
    template_name = 'categories/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение категории'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('categories:main')
    login_url = reverse_lazy('accounts:login')

    template_name = 'categories/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление категории'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser
