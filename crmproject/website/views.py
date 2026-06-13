from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import CustomerForm
from .models import Customer


def landing(request):
    return render(request, 'landing.html')


def register(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration Successful!"
            )

            return redirect('landing')

        else:

            messages.error(
                request,
                "Invalid Details!"
            )

    else:
        form = CustomerForm()

    return render(request, 'register.html', {'form': form})


def home(request):

    customers = Customer.objects.all()

    return render(
        request,
        'home.html',
        {'customers': customers}
    )


def create_customer(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Customer Added Successfully!"
            )

            return redirect('home')

    else:
        form = CustomerForm()

    return render(
        request,
        'create.html',
        {'form': form}
    )


def update_customer(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    if request.method == "POST":

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Customer Updated Successfully!"
            )

            return redirect('home')

    else:

        form = CustomerForm(instance=customer)

    return render(
        request,
        'update.html',
        {'form': form}
    )


def delete_customer(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    customer.delete()

    messages.success(
        request,
        "Customer Deleted Successfully!"
    )

    return redirect('home')