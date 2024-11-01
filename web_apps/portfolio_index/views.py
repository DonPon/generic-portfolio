# index/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView  # Import LoginView
from django.contrib import messages
from .models import PortfolioItem, PersonalDetails
from .forms import ContactForm, CustomLoginForm
from dotenv import load_dotenv
from django.core.mail import send_mail
import os
import textwrap
# Load environment variables from .env file
load_dotenv()

class CustomLoginView(LoginView):
    template_name = 'portfolio_index/login.html'  # Specify your custom login template
    authentication_form = CustomLoginForm  # Use the custom login form if you've created one

    def get_success_url(self):
        return reverse_lazy('portfolio')  # Redirect to the portfolio page after login

class CoreSettingsView(TemplateView):
    template_name = 'portfolio_index/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = PortfolioItem.objects.all()  # Fetch portfolio items
        context['personal_details'] = PersonalDetails.objects.first()  # Fetch first PersonalDetails entry
        return context

class PersonalDetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = PersonalDetails
    fields = ['name', 'title', 'bio']
    template_name = 'portfolio_index/edit_personal_details_form.html'
    success_url = reverse_lazy('core_settings')  # Redirect to the core settings page after update

    def get_object(self, queryset=None):
        # Fetch the first object for simplicity
        return PersonalDetails.objects.first()  # Adjust if you have specific logic to fetch a specific record

class PortfolioListView(ListView):
    model = PortfolioItem
    template_name = 'portfolio_index/portfolio.html'  # Specify your own template name/location
    context_object_name = 'items'  # Default is 'object_list', we change it to 'items'

class ProjectDetailView(DetailView):
    model = PortfolioItem
    template_name = 'portfolio_index/project_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

class PortfolioItemDeleteView(LoginRequiredMixin, DeleteView):
    model = PortfolioItem
    template_name = 'portfolio_index/portfolio_confirm_delete.html'  # Optional: use a template if needed
    success_url = reverse_lazy('portfolio')  # Redirect to the portfolio list after deletion
    pk_url_kwarg = 'id'  # This should match the URL pattern parameter

    def get_object(self, queryset=None):
        # Override to provide custom logic for retrieving the object
        return super().get_object(queryset)

class PortfolioItemCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioItem
    template_name = 'portfolio_index/portfolio_form.html'
    fields = ['title', 'description', 'image', 'url', 'details']
    success_url = reverse_lazy('portfolio')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Add New Project'
        return context

class PortfolioItemUpdateView(LoginRequiredMixin, UpdateView):
    model = PortfolioItem
    template_name = 'portfolio_index/portfolio_form.html'
    fields = ['title', 'description', 'image', 'url', 'details']
    success_url = reverse_lazy('portfolio')
    pk_url_kwarg = 'id'  # This tells Django to look up by 'id' from the URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Update Project'
        return context

class ContactFormView(FormView):
    template_name = 'portfolio_index/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')  # Redirects to the same page on success

    def form_valid(self, form):
        # Save the form data to the database
        form.save()

        # Get the submitted data
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        # Prepare the email content
        email_subject = 'New Contact Form Submission'
        email_body = f"""
        You have received a new message from your settings website contact form:

        Name: {name}
        Email: {email}
        Message: 
        {message}
        """

        # Get email credentials from environment variables
        email_host_user = os.getenv('EMAIL_HOST_USER')
        recipient_email = os.getenv('RECIPIENT_EMAIL')

        # Send the email
        send_mail(
            subject=email_subject,
            message=textwrap.dedent(email_body),
            from_email=email_host_user,
            recipient_list=[recipient_email],
            fail_silently=False,
        )

        # Display a success message on the website
        messages.success(self.request, "Your message has been sent!")

        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle form errors
        messages.error(self.request, "There was an error with your submission.")
        return super().form_invalid(form)