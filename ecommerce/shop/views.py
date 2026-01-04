from django.shortcuts import render,redirect
from .form import SignUpForm,UserUpdateForm,ProfileUpdateForm
from .models import Customer_user,Product
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

@login_required
def my_account(request):
    return render(request, 'my_account.html')


def about_us(request):
    return render(request, 'about_us.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products':products})

def product_detail(request):
    return render(request, 'product_detail.html')

def checkout_cart(request):
    return render(request, 'checkout_cart.html')

def checkout_complete(request):
    return render(request, 'checkout_complete.html')

def checkout_info(request):
    return render(request, 'checkout_info.html')

def checkout_payment(request):
    return render(request, 'checkout_payment.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def faq(request):
    return render(request, 'faq.html')

def index_fixed_header(request):
    return render(request, 'index_fixed_header.html')

def index_inverse_header(request):
    return render(request, 'index_inverse_header.html')

def search_results(request):
    return render(request, 'search_results.html')


def Sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # create customer profile
            Customer_user.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                image = form.cleaned_data['image']
            )

            login(request, user)
            return redirect("my_account")
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {'form': form})

@login_required
def profile_update(request):
    customer, created = Customer_user.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=customer)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # Yahan check karein: messages (plural) hona chahiye
            messages.success(request, f'Your account has been updated!') 
            return redirect('my_account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=customer)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile_update.html', context)

