from django import forms
from .models import Agency, Profile, Package, Tourist
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'user_type']


class AgencyForm(forms.ModelForm):

    class Meta:
        model = Agency
        fields = ['name', 'description', 'banner_image', 'phone_number']
        labels = {
            'name': 'Nombre de la Agencia',
            'description': 'Descripcion de la agencia',
            'phone_number': 'Numero de telefono Agencia',
            'banner_image': 'Banner de la agencia'
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
            'banner_image': forms.ClearableFileInput(attrs={
                'class': 'form-control ',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el mensaje de error para el campo 'name'
        self.fields['name'].error_messages['unique'] = 'Ya existe una agencia con este nombre. Por favor, elige un nombre diferente.'  # noqa: E501


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package_name', 'package_description',
                  'children', 'adults', 'check_in', 'check_out',
                  'base_price', 'discount', 'available_slots',
                  'comments', 'score']
        labels = {
            'package_name': 'Nombre del Paquete',
            'package_description': 'Descripcion del paquete',
            'children': 'Cantidad de niños',
            'adults': 'Cantidad de adultos',
            'check_in': 'Fecha de entrada',
            'check_out': 'Fecha de salida',
            'base_price': 'Precio base (USD)',
            'discount': 'Descuento (%)',
            'available_slots': 'Cupos disponibles',
            'comments': 'Comentarios',
            # 'score': '',
            'agency': 'Nombre de la agencia',
        }
        # widgets
        widgets = {
            'package_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de tu agencia (Peru Travel)',
                }),
            'package_description': forms.Textarea(attrs={
                'class': 'form-control text-areea',
                'placeholder': 'Cuéntanos sobre tu agencia...'
                }),
            'adults': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Cantidad de adultos (1)'
                }),
            'children': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Cantidad de niños (0)'
                }),
            'check_in': forms.DateTimeInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Fecha entrada'
                }),
            # 'check_out': DateTimePickerInput(attrs={
            #     'class': 'form-control text-center',
            #     'placeholder': 'Fecha salida'
            #     }, options={"format": "MM/DD/YYYY"}),
            'check_out': forms.DateTimeInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Fecha salida'
                }),
            'base_price': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Precio base (USD)'
                }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Cantidad de niños (0)'
                }),
            'available_slots': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Cantidad de niños (0)'
                }),
            'comments': forms.Textarea(attrs={
                'class': 'form-control text-areea',
                'placeholder': 'Algun comentario adicional...'
                }),
            'score': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'placeholder': 'Calificacion del paquete (1)'
                }),
            'banner_image': forms.ClearableFileInput(attrs={
                'class': 'form-control ',
            }),
        }


class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = ['profile', 'bio', 'image']
