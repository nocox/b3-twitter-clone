from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class Signup(generic.FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = '/accounts/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Thanks(generic.TemplateView):
    template_name = 'registration/thanks.html'