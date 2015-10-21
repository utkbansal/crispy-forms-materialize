from django.views.generic import FormView
from  .forms import RegisterForm

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'test.html'
