from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.urls import reverse_lazy

# Landing Page View
def landing(request):
    return render(request, 'core/landing.html')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

# Login View (Using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add CSS classes to form fields
        form.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})
        form.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})
        return form

    def get_success_url(self):
        # Check if the user is an admin
        if self.request.user.isAdmin:
            return reverse_lazy('admin_dashboard')  # Redirect to admin dashboard
        else:
            return reverse_lazy('user_dashboard')  # Redirect to user dashboard


# Logout View
def custom_logout(request):
    logout(request)
    return redirect('landing')