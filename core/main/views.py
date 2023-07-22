from django.shortcuts import render, redirect
from .models import *
from .forms import ReservationModelForm, ContactMessageModelForm, SubscribeModelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        form2 = ContactMessageModelForm(request.POST)
        form3 = SubscribeModelForm(request.POST)

        if form.is_valid():
            Reservation.objects.create(**form.cleaned_data)
            return redirect('index')
        
        if form2.is_valid():
            ContactMessage.objects.create(**form2.cleaned_data)
            return redirect('index')
        
        if form3.is_valid():
            Subscribe.objects.create(**form3.cleaned_data)
            return redirect('index')
    else:
        form = ReservationModelForm()
        form2 = ContactMessageModelForm()
        form2 = SubscribeModelForm()

    header_sidebar = Header_Sidebar.objects.all()[0]
    homepage = Homepage.objects.all()[0]
    about = About.objects.all()[0]
    about_content = AboutContent.objects.all()
    titles = Title.objects.all()[0]
    reasons = Reason.objects.all()
    menu = Menu.objects.all()
    menu_content = MenuContent.objects.all()
    specials = Special.objects.all()
    event = Event.objects.all()[0]
    event_slides = EventSlide.objects.all()
    reservation = ReservationContent.objects.all()[0]
    gallery = Gallery.objects.all()[0]
    chefs = Chef.objects.all()
    contact = Contact.objects.all()[0]
    contact_info = ContactInfo.objects.all()

    return render(request, 'index.html', context={
        'header_sidebar':header_sidebar,
        'homepage':homepage,
        'about':about,
        'about_content':about_content,
        'titles':titles,
        'reasons':reasons,
        'menu':menu,
        'menu_content':menu_content,
        'specials':specials,
        'event':event,
        'event_slides':event_slides,
        'reservation':reservation,
        'gallery':gallery,
        'chefs':chefs,
        'contact':contact,
        'contact_info':contact_info,
    })