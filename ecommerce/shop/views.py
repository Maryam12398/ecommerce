from django.shortcuts import render,redirect
from .form import SignUpForm
from .models import Customer_user
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    # This looks inside your 'templates' folder automatically
    # Replace 'index.html' with the actual name of your main HTML file
    return render(request, 'index.html')
@login_required
def my_account(request):
    # This looks inside your 'templates' folder automatically
    # Replace 'index.html' with the actual name of your main HTML file
    return render(request, 'my_account.html')

# def logout_view(request):
#     logout(request)
#     return redirect('home_page')
# def Sign_up(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect("home_page")
#     else:
#         form = SignUpForm()

#     return render(request, "sign_up.html", {'form': form})

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
                phone=form.cleaned_data['phone']
            )

            login(request, user)
            return redirect("my_account")
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {'form': form})