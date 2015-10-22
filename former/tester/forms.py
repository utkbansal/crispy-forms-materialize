from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from crispy_forms_materialize.layout import Card, Submit
from django import forms

choices = (('a', 'a'), ('s', 's'))


class RegisterForm(forms.Form):
    married = forms.BooleanField()
    name = forms.CharField()

    # Problem with materialize select when using js to initialize
    # occupation = forms.ChoiceField(choices=(('a', 'a'), ('b', 'b')))
    bithday = forms.DateField()
    date_time = forms.DateTimeField()
    decimal_number = forms.DecimalField()
    email = forms.EmailField()
    # Problems in rendering
    photo = forms.FileField()
    # No support in materializecss
    interests = forms.MultipleChoiceField(choices=choices)
    comment = forms.CharField(widget=forms.Textarea)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Card(
                'married',
                'name',
                'bithday',
                'file',
                # 'interests',
                'comment',
                # 'sex',
                Submit('submit', 'Go!', 'send', 'right',
                       css_class='waves-effect'),
                # Button('Bhej Do!', 'send', 'right', css_class='waves-effect'),
                css_class='col m6 offset-m3'
            )
        )
