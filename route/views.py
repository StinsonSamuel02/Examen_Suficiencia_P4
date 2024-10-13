from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from route.models import Route


# Create your views here.
@login_required
def routes(request):
    response = Route.objects.all()
    return render(request, 'pages/routes.html', {'routes': response})


@login_required
def create(request):
    name = request.POST.get('name')
    origin = request.POST.get('origin')
    destination = request.POST.get('destination')

    Route.objects.create(name=name, origin=origin, destination=destination)
    return redirect('/routes')


@login_required
def edit(request, id):
    route = Route.objects.get(id=id)
    return render(request, 'pages/form-edit-route.html', {'route': route})


@login_required
def edit_route(request, id):
    route = Route.objects.get(id=id)

    route.name = request.POST.get('name')
    route.origin = request.POST.get('origin')
    route.destination = request.POST.get('destination')

    route.save()
    return redirect('/routes')


@login_required
def delete(request, id):
    route = Route.objects.get(id=id)
    route.delete()
    return redirect('/routes')
