from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
@login_required
def search(request):
    query=""
    products=None
    if(request.method=="POST"):
        query=request.POST['q']
        #print("query",query)
        if query:
            products=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'search.html',{'query':query,'p':products})
