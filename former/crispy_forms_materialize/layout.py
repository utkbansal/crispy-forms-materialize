from crispy_forms.layout import TemplateNameMixin
from crispy_forms.compatibility import text_type
from crispy_forms.utils import render_field, flatatt
from crispy_forms import layout as crispy_forms_layout

from django.conf import settings
from django.template import Template
from django.template.loader import render_to_string

TEMPLATE_PACK = getattr(settings,
                        'CRISPY_TEMPLATE_PACK',
                        'materialize')


class Layout(crispy_forms_layout.Layout):
    pass


class UneditableField(crispy_forms_layout.HTML):
    pass


class HTML(crispy_forms_layout.HTML):
    pass


class MultiWidgetField(crispy_forms_layout.MultiWidgetField):
    pass


class Div(crispy_forms_layout.Div):
    template = "{0}/layout/div.html".format(TEMPLATE_PACK)


class Row(Div):
    css_class = 'row'


class Column(Div):
    css_class = 'col'

    def __init__(self, field, *args, **kwargs):
        self.field = field
        if 'css_class' not in kwargs:
            kwargs['css_class'] = 's12'

        super(Column, self).__init__(field, *args, **kwargs)


################ CUSTOM MATERIALIZE BUTTON ###################

class Button(TemplateNameMixin):
    template = "%s/layout/button.html"

    def __init__(self, value, icon=None, position=None, **kwargs):
        self.value = value
        self.icon = icon
        self.position = position
        self.id = kwargs.pop('css_id', '')
        self.attrs = {}
        self.field_classes = ''

        if 'css_class' in kwargs:
            self.field_classes += kwargs.pop('css_class')

        self.template = kwargs.pop('template', self.template)
        self.flat_attrs = flatatt(kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK,
               **kwargs):
        self.value = Template(text_type(self.value)).render(context)
        template = self.get_template_name(template_pack)
        return render_to_string(template, {'button': self}, context)


class Submit(TemplateNameMixin):
    template = "%s/layout/submit.html"

    def __init__(self, name, value, icon=None, position=None, **kwargs):
        self.name = name
        self.value = value
        self.id = kwargs.pop('css_id', '')
        self.attrs = {}
        self.icon = icon
        self.position = position
        self.field_classes = ''

        if 'css_class' in kwargs:
            self.field_classes += kwargs.pop('css_class')

        self.template = kwargs.pop('template', self.template)
        self.flat_attrs = flatatt(kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK,
               **kwargs):
        """
        Renders an `<input />` if container is used as a Layout object.
        Input button value can be a variable in context.
        """
        self.value = Template(text_type(self.value)).render(context)
        template = self.get_template_name(template_pack)
        return render_to_string(template, {'submit': self}, context)


############## CUSTOM CARD ####################

# Not rendering properly

class Card(Div):
    css_class = 'card-panel'
    template = "{0}/layout/card.html".format(TEMPLATE_PACK)


class Field(crispy_forms_layout.Field, Div):
    template = "{0}/field.html".format(TEMPLATE_PACK)


################# This is useless #########################
# class FileField(Field):
#     """
#     Field that exposes a file upload button in the materialize way
#     """
#     def __init__(self, field, *args, **kwargs):
#         self.field = field
#         if 'css_class' not in kwargs:
#             kwargs['css_class'] = 'file-path validate'
#
#         super(FileField, self).__init__(field, *args, **kwargs)

# template = "{0}/field.file.html".format(TEMPLATE_PACK)


class MultiField(crispy_forms_layout.MultiField):
    """
    MultiField container. Renders to a MultiField
    """
    template = "{0}/layout/multifield.html".format(TEMPLATE_PACK)
    field_template = "{0}/multifield.html".format(TEMPLATE_PACK)


class InlineField(Field):
    """
    Layout object for rendering an inline field with Materialize
    Example:
    .. sourcecode:: python
        InlineField('field_name')
    Or:
    .. sourcecode:: python
        InlineField('field_name', label_column='large-8',
        input_column='large-4', label_class='')
    ``label_column``, ``input_column``, ``label_class``, are optional argument.
    """
    template = "{0}/layout/inline_field.html".format(TEMPLATE_PACK)

    def __init__(self, field, label_column='large-3', input_column='large-9',
                 label_class='', *args, **kwargs):
        self.field = field
        self.label_column = label_column + ' columns'
        self.input_column = input_column + ' columns'
        self.label_class = label_class

        super(InlineField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['label_column'] = self.label_column
        context['input_column'] = self.input_column
        context['label_class'] = self.label_class

        html = ''
        for field in self.fields:
            html += render_field(field, form, form_style, context,
                                 template=self.template, attrs=self.attrs,
                                 template_pack=template_pack)
        return html


################### USELESS NON MATERIALIZE BUTTON #######################
#
# class Button(crispy_forms_layout.Button):
#     """
#     Used to create a Submit input descriptor for the {% crispy %} template tag:
#     .. sourcecode:: python
#         button = Button('Button 1', 'Press Me!')
#     .. note:: The first argument is also slugified and turned into the
#     id for the button.
#     """
#     input_type = 'button'
#     field_classes = 'btn waves-effect waves-light'


########################3 USELESS SUBMIT BUTTON #############################
#
# class Submit(crispy_forms_layout.Submit):
#     """
#     Used to create a Submit button descriptor for the {% crispy %}
#     template tag:
#     .. sourcecode:: python
#         submit = Submit('Search the Site', 'search this site')
#     .. note:: The first argument is also slugified and turned into the id for the submit button.
#     """
#     input_type = 'submit'
#     field_classes = 'btn waves-effect waves-light'


class Hidden(crispy_forms_layout.Hidden):
    """
    Used to create a Hidden input descriptor for the {% crispy %} template tag.
    """
    input_type = 'hidden'
    field_classes = 'hidden'

# class Switch(Field):
#     template = '{0}/switch.html'.format(TEMPLATE_PACK)
