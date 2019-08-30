from django.shortcuts import render, redirect

from crud.forms.ProductForm import ProductForm
from var_dump import var_dump 

def home(request):
    return render(request, "pages/products/list.html")


def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        var_dump(request)
        if form.is_valid():
            return redirect('product')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "pages/products/add.html", context)
