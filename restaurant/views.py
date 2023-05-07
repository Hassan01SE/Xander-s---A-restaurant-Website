from django.http import HttpResponse, Http404
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


# Create your views here.

def handler404(request, exception):
    print("404 Error")
    return render(request, '404.html', status=404)


def home(request):
    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            guestcount = form.cleaned_data['guest_number']
            comment = form.cleaned_data['comment']
            date = form.cleaned_data['reservation_date']
            data = {
                'name': name,
                'lastname': lastname,
                'count': guestcount,
                'comment': comment,
                'date': date,
            }
            return render(request, 'successBooking.html', data)

    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):

    menu_data = Menu.objects.all().order_by('name')

    main_data = {
        "menu": menu_data
    }
    return render(request, 'menu.html', main_data)


def display_menu_item(request, pk='none'):
    """ if pk:
        menu_item = Menu.objects.get(pk=pk)
        if Menu.DoesNotExist:
            return render(request, '404.html', {})
    else:
        menu_item = ""

    return render(request, 'menu_item.html', {"menu_item": menu_item}) """

    try:
        menu_item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return render(request, '404.html', {})
    return render(request, 'menu_item.html', {"menu_item": menu_item})
