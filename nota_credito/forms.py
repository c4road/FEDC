import OpenSSL.crypto

from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from .models import *
from conectores.models import Compania


class FormNotaCredito(ModelForm):

    # pass_certificado = CharField(widget=PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = notaCredito
        fields = ['status','compania','ref_factura','numero_factura','senores','direccion','transporte','despachar','observaciones',
                    'giro','condicion_venta','vencimiento','vendedor','rut','fecha','guia','orden_compra','nota_venta',
                    'productos','monto_palabra','neto','excento','iva','total','track_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].required = False
        self.fields['status'].disabled = True
        self.fields['compania'].widget.attrs.update({'class': 'form-control'})
        self.fields['compania'].required = False
        self.fields['compania'].disabled = True
        self.fields['ref_factura'].widget.attrs.update({'class': 'form-control'})
        self.fields['ref_factura'].required = False
        self.fields['ref_factura'].disabled = True
        self.fields['numero_factura'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_factura'].required = False
        self.fields['numero_factura'].disabled = True
        self.fields['senores'].widget.attrs.update({'class': 'form-control'})
        self.fields['senores'].required = False
        self.fields['senores'].disabled = True
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].required = False
        self.fields['direccion'].disabled = True
        self.fields['transporte'].widget.attrs.update({'class': 'form-control'})
        self.fields['transporte'].required = False
        self.fields['transporte'].disabled = True
        self.fields['despachar'].widget.attrs.update({'class': 'form-control'})
        self.fields['despachar'].required = False
        self.fields['despachar'].disabled = True
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].required = False
        self.fields['observaciones'].disabled = True
        self.fields['giro'].widget.attrs.update({'class': 'form-control'})
        self.fields['giro'].required = False
        self.fields['giro'].disabled = True
        self.fields['condicion_venta'].widget.attrs.update({'class': 'form-control'})
        self.fields['condicion_venta'].required = False
        self.fields['condicion_venta'].disabled = True
        self.fields['vencimiento'].widget.attrs.update({'class': 'form-control'})
        self.fields['vencimiento'].required = False
        self.fields['vencimiento'].disabled = True
        self.fields['vendedor'].widget.attrs.update({'class': 'form-control'})
        self.fields['vendedor'].required = False
        self.fields['vendedor'].disabled = True
        self.fields['rut'].widget.attrs.update({'class': 'form-control'})
        self.fields['rut'].required = False
        self.fields['rut'].disabled = True
        self.fields['fecha'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha'].required = False
        self.fields['fecha'].disabled = True
        self.fields['guia'].widget.attrs.update({'class': 'form-control'})
        self.fields['guia'].required = False
        self.fields['guia'].disabled = True
        self.fields['orden_compra'].widget.attrs.update({'class': 'form-control'})
        self.fields['orden_compra'].required = False
        self.fields['orden_compra'].disabled = True
        self.fields['nota_venta'].widget.attrs.update({'class': 'form-control'})
        self.fields['nota_venta'].required = False
        self.fields['nota_venta'].disabled = True
        self.fields['productos'].widget.attrs.update({'class': 'form-control'})
        self.fields['productos'].required = False
        self.fields['productos'].disabled = True
        self.fields['monto_palabra'].widget.attrs.update({'class': 'form-control'})
        self.fields['monto_palabra'].required = False
        self.fields['monto_palabra'].disabled = True
        self.fields['neto'].widget.attrs.update({'class': 'form-control'})
        self.fields['neto'].required = False
        self.fields['neto'].disabled = True
        self.fields['excento'].widget.attrs.update({'class': 'form-control'})
        self.fields['excento'].required = False
        self.fields['excento'].disabled = True
        self.fields['iva'].widget.attrs.update({'class': 'form-control'})
        self.fields['iva'].required = False
        self.fields['iva'].disabled = True
        self.fields['total'].widget.attrs.update({'class': 'form-control'})
        self.fields['total'].required = False
        self.fields['total'].disabled = True
        self.fields['track_id'].required = False

class FormCreateNotaCredito(ModelForm):

    class Meta:
        model = notaCredito
        fields = ['numero_factura','senores','transporte','despachar','observaciones',
                    'giro','rut','fecha','guia','orden_compra','nota_venta',
                    'productos','monto_palabra','ciudad_receptora','comuna', 'region']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_factura'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_factura'].required = True
        self.fields['senores'].widget.attrs.update({'class': 'form-control'})
        self.fields['senores'].required = True
        self.fields['transporte'].widget.attrs.update({'class': 'form-control'})
        self.fields['transporte'].required = False
        self.fields['despachar'].widget.attrs.update({'class': 'form-control'})
        self.fields['despachar'].required = False
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].required = False
        self.fields['giro'].widget.attrs.update({'class': 'form-control'})
        self.fields['giro'].required = True
        self.fields['rut'].widget.attrs.update({'class': 'form-control'})
        self.fields['rut'].required = True
        self.fields['fecha'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha'].required = True
        self.fields['guia'].widget.attrs.update({'class': 'form-control'})
        self.fields['guia'].required = False
        self.fields['orden_compra'].widget.attrs.update({'class': 'form-control'})
        self.fields['orden_compra'].required = False
        self.fields['nota_venta'].widget.attrs.update({'class': 'form-control'})
        self.fields['nota_venta'].required = False
        self.fields['productos'].widget.attrs.update({'class': 'form-control'})
        self.fields['productos'].required = True
        self.fields['ciudad_receptora'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad_receptora'].required = True
        self.fields['comuna'].widget.attrs.update({'class': 'form-control'})
        self.fields['comuna'].required = True
        self.fields['region'].widget.attrs.update({'class': 'form-control'})
        self.fields['region'].required = True