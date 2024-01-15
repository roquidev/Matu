from django import forms
from .models import Agency, UserProfile, TravelPackage
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'user_type']


class AgencyForm(forms.ModelForm):

    class Meta:
        model = Agency
        fields = ['name', 'description', 'phone_number']
        labels = {
            'name': 'Nombre de la Agencia',
            'description': 'Descripcion de la agencia',
            'phone_number': 'Numero de telefono Agencia'
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de tu agencia (Peru Travel)',
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control text-areea',
                'placeholder': 'Cuéntanos sobre tu agencia...'
                }),
            'phone_number': PhoneNumberPrefixWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono (+51987654321)'
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el mensaje de error para el campo 'name'
        self.fields['name'].error_messages['unique'] = 'Ya existe una agencia con este nombre. Por favor, elige un nombre diferente.'  # noqa: E501


class TravelPackageForm(forms.ModelForm):
    class Meta:
        model = TravelPackage
        fields = '__all__'
        labels = {
            'name': 'Nombre del Paquete',
            'package_description': 'Descripcion del paquete',
            'children': 'Cantidad de niños',
            'adults': 'Cantidad de adultos',
            'check_in': 'Fecha de entrada',
            'check_out': 'Fecha de salida',
            'base_price': 'Precio base (USD)',
            'discount': 'Descuento (%)',
            'available_slots': 'Cupos disponibles',
            'comments': 'Comentarios',
            # 'SCORES_TO_CHOOSE': '',
            # 'score': '',
            'agency': 'Nombre de la agencia',
        }
