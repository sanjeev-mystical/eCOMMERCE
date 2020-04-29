from django.shortcuts import render, redirect
from . import forms
from .forms import ContactForm
from django.http import JsonResponse, HttpResponse

def home_page(request):
    # print(request.session.get('first_name'))  #get
    return render(request, "home_page.html", {})


def about_page(request):
    return render(request, "home_page.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact",
        "form": contact_form,
        "brand": 'new brand name'
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": 'Thank You For Your Submission'})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400,content_type = 'application/json')

    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
