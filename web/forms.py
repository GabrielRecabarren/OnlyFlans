from django import forms
from .models import ContactForm, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['flan', 'rating']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(0, 6)])
        }
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name','message']
