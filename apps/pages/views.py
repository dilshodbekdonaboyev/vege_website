from django.shortcuts import render, redirect
from apps.pages.models import Vegatebles, Feedback
# Create your views here.
def home(request):
    vegatebles = Vegatebles.objects.all()
    feedbacks = Feedback.objects.all().filter(is_valid = True)
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        text  = request.POST.get("message")
        Feedback.objects.create(name = name, phone_number = phone_number, email = email, text = text).save()
        return redirect('home')
    context = {
        'vegatebles': vegatebles,
        'first_vegatable': vegatebles.last(),
        'feedbacks' : feedbacks[1:],
        "first_feedback" : feedbacks.first(),
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        text  = request.POST.get("message")
        Feedback.objects.create(name = name, phone_number = phone_number, email = email, text = text).save()
        return redirect('home')
    return render(request, 'contact.html')
def shop(request):
    vegatebles = Vegatebles.objects.all()
    context = {
        'vegatebles': vegatebles,
    }
    return render(request, 'shop.html', context)
def blog(request):
    return render(request, 'blog.html')
def vagetables(request):
    vegatebles = Vegatebles.objects.all()
    context = {
        'vegatebles': vegatebles,
    }
    return render(request, 'vagetables.html', context)
