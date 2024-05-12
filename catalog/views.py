from django.shortcuts import render
from catalog.models import Product
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView



class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def post(self, request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         print(f'{name} {phone} {message}')
#
#     return render(request, 'catalog/contacts.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')





