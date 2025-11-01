"""Forms for sith_app."""
from django import forms


class SithForm(forms.Form):
    """Class for sith form."""

    choice = forms.ModelMultipleChoiceField(queryset=None, label=None)

    def __init__(self, queryset, label, *args, **kwargs):
        """Adding fields."""
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = queryset
        self.fields['choice'].label = label
