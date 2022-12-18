from django.forms import ModelForm
from .models import Attack

from django.core.exceptions import NON_FIELD_ERRORS

class AttackForm(ModelForm):
    class Meta:
        model = Attack
        fields = ['name', 'command']
        error_messages = {
            'name': {
                'max_length': "This attack name is too long.",
            },
            NON_FIELD_ERRORS: {
                'unique_together': "This attack name is already taken.",
            }
        }
