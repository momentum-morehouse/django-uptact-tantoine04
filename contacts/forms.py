from django import forms
from .models import Contact
from .models import Note


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]


class NoteForm(forms.Form):
    class Meta:
        model = Note
        fields =[
            'note'
        ]
    # new_noteform = forms.Textarea(label='Note', max_length=250)


widgets = {
    'birthday':
        forms.DateInput(
        format=('%m/%d/%Y'),
        attrs={
            'class': 'form-control',
            'placeholder': 'Select a date',
            'type': 'date'
        }),
}
