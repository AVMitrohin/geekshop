from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from mainapp.models import ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from authapp.models import ShopUser


class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


# @method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryListView(IsSuperUserView, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class ProductCategoryCreateView(IsSuperUserView, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class ProductCategoryUpdateView(IsSuperUserView, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Обновление категории'
        return context


class ProductCategoryDeleteView(IsSuperUserView, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Удаление категории'
        context['action_type'] = 'delete'
        return context


class UserListView(IsSuperUserView, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context


class UsersCreateView(IsSuperUserView, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание пользователя'
        return context


class UsersUpdateView(IsSuperUserView, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super(UsersUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        return context


class UsersDeleteView(IsSuperUserView, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super(UsersDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Удаление пользователя'
        # context['action_type'] = 'delete'
        return context

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(ShopUser, pk=kwargs['pk'])
        user.is_active = False
        user.save()
        return HttpResponseRedirect(self.success_url)

