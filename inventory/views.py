from django.shortcuts import render


def products(request):
    context={"breadcrumb":{"parent":"Inventory","child":"Products"}}
    return render(request, 'inventory/product/products.html', context=context)


def product_create(request):
    context={"breadcrumb":{"parent":"Inventory","child":"Product Create"}}
    return render(request, 'inventory/product/products.html', context=context)
