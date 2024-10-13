from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from bus.forms import BusForm, EditBusForm
from bus.models import Bus
from route.models import Route


@login_required
def buses(request):
    routes = Route.objects.all()
    busses = Bus.objects.all()

    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/buses')  # Redirecciona a la lista de buses después de guardar
    else:
        form = BusForm()

    return render(request, 'pages/buses.html', {'form': form, 'buses': busses, 'routes': routes})


@login_required
def edit(request, id):
    bus = get_object_or_404(Bus, pk=id)
    routes = Route.objects.all()

    if request.method == 'POST':
        form = EditBusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('/buses')
    else:
        form = EditBusForm(instance=bus)
    return render(request, 'pages/form-edit-bus.html', {'form': form, 'bus': bus, 'routes': routes})


@login_required
def delete(request, id):
    bus = Bus.objects.get(id=id)
    bus.delete()
    return redirect('/buses')
