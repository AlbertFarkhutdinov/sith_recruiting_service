"""Common constants and functions used in the project."""


def get_items(model, value=None, parameter=None):
    """Return filtered queryset of model instances."""
    all_objects = model.objects
    if value and parameter:
        filter_arg = {parameter: value}
        return all_objects.filter(**filter_arg).select_related()
    return all_objects.all().select_related()


def get_item(model, value, parameter='pk'):
    """Return the instance with specified parameter."""
    filter_arg = {parameter: value}
    return model.objects.filter(**filter_arg).select_related().first()


def set_attributes(field):
    """Set attributes for form fields."""
    field.widget.attrs['class'] = 'form-control'
    field.help_text = ''


QUESTIONS_NUMBER_IN_SET = 3
SHADOW_HANDS_MAX_NUMBER = 3
