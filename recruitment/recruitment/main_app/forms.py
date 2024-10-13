"""Forms for main_app."""
from django.contrib.auth.forms import AuthenticationForm

from recruitment.common import set_attributes
from recruitment.main_app.models import CustomUser


class UserLoginForm(AuthenticationForm):
    """Class for user login form."""

    class Meta:
        """
        Class determines, which fields of model will be represented in form.

        """

        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Adding of attributes to fields."""
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            set_attributes(field)
