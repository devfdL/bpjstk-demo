from django import forms
from django.forms import formset_factory

class userForm(forms.Form):
    nik    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'nik-inpt',
                'placeholder':''
            }
        )
    )

    alamat    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'alamat-inpt',
                'placeholder':''
            }
        )
    )


    ttl    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'ttl-inpt',
                'placeholder':''
            }
        )
    )

    pekerjaan    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'pekerjaan-inpt',
                'placeholder':''
            }
        )
    )

    user_signature    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'user_signature-inpt',
                'placeholder':''
            }
        )
    )

    hp_number    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'hp_number-inpt',
                'placeholder':''
            }
        )
    )

class walletForm(forms.Form):
    username    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'username-inpt',
                'placeholder':''
            }
        )
    )

    wallet    = forms.CharField(
        max_length=100,
        label = '',
        widget = forms.TextInput(
            attrs={
                'class':'wallet-inpt',
                'placeholder':''
            }
        )
    )


    point    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'point-inpt',
                'placeholder':'nominal'
            }
        )
    )

    last_transaction    = forms.CharField(
        max_length=50,
        label = '',
         widget = forms.TextInput(
            attrs={
                'class':'last_transaction-inpt',
                'placeholder':'date'
            }
        )
    )