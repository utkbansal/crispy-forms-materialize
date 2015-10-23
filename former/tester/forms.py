from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from crispy_forms_materialize.layout import Submit, Div
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
    interests2 = forms.ChoiceField(choices=choices)
    comment = forms.CharField(widget=forms.Textarea)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            'married',
            'name',
            'bithday',
            'date_time',
            'email',
            # 'file',
            'photo',
            # 'interests',
            'interests2',
            'comment',
            'sex',
            Div(
                Submit('submit', 'Go!', 'send', 'right',
                       css_class='waves-effect')
                , css_class='col s12'
            ),
            # Button('Bhej Do!', 'send', 'right', css_class='waves-effect'),

        )
