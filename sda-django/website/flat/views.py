from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import  HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.
def test_response(request):
    return HttpResponse("Hello from FLAT app")

def find_response(request):
    result = None
    if request.method=="POST":
        form_obj = FindFlatForm(request.POST)
        if form_obj.is_valid():
            data = form_obj.cleaned_data
            data["title"] = data["title"] or ""
            data["price_min"] = data["price_min"] or 0.0
            data["price_max"] = data["price_max"] or 0.0
            data["area_min"] = data["area_min"] or 0.0
            data["area_max"] = data["area_max"] or 0.0
            data["district"] = data["district"] or ""

            result = Flat.objects.all()
            if data["price_min"]>0:
                result = result.filter(price__gte=data["price_min"])
            if data["price_max"]>0:
                result = result.filter(price__lte=data["price_max"])
            if len(data["district"]):
                result = result.filter(district__contains=data["district"])
            result = result.order_by('price')
    else:
        form_obj = FindFlatForm()
    return render(request, "form.html",
                  { "form" : form_obj, "result": result  } )