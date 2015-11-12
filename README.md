# crispy-forms-materialize

 Introduction
============

This is a [Django](https://www.djangoproject.com/) application to add [django-crispy-forms](https://github.com/maraujop/django-crispy-forms) template pack for [Materializecss](http://materializecss.com/).

The main goal of this project is to reduce the time spent by developers on styling forms. Since most of the time we are using a css framework,
the work done in styling different forms is quite redundant and boring. This library aims at reducing this redundancy by automatically 
sytling your forms using the Materializecss framework.

How To Use
===========

Add the following code to settings.py to specify which template pack to use

```python
    
    CRISPY_TEMPLATE_PACK = 'materialize'

```

Create a form in forms.py and override its __init__ to add FormHelper as the helper.
```python

class TestForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
```

Associate it with a view

```python
class RegisterView(FormView):
    form_class = TestForm
    template_name = 'test.html'

```

And finally the template

```html
{% load crispy_forms_tags %}
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <!--Add materialize libraries -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.1/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.1/js/materialize.min.js"></script>

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
          rel="stylesheet">

</head>
<body>
<div class="row">
    <div class="card-panel col m6 offset-m3">
        <!-- Only one line -->
        {% crispy form %}
    </div>
</div>

</body>
</html>
```

Which finally leads into something like this - 

![Screenshot of rendered HTML]
(https://raw.githubusercontent.com/utkbansal/crispy-forms-materialize/master/Screenshot.png)

Note - We did not have to write any css to style the form. It was auto-generated from the form class.