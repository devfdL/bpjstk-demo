from django import forms
from django.forms import formset_factory

PAYMENT_CHOICES = (
    (' ', ' '),
    ('Pay with Whatsapp Verification', 'Pay with Whatsapp Verification'),
    ('Pay with face Verification', 'Pay with face Verification'),
)

class payForm(forms.Form):
    target    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'target-inpt',
                'placeholder':''
            }
        )
    )

    amount    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'amount-inpt',
                'placeholder':''
            }
        )
    )

    paymentchoice = forms.ChoiceField(choices = PAYMENT_CHOICES) 

class payVer(forms.Form):
    payver    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'payver-inpt',
                'placeholder':''
            }
        )
    )