from django import forms

class AdopcionFormulario(forms.Form):
    nombre_de_Mascota=forms.CharField(max_length=40)
    edad=forms.FloatField()
    genero = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)
    castracion = forms.CharField(max_length=40)
    nombre_del_Tutelar=forms.CharField(max_length=40)
    telefono=forms.IntegerField()
    mail= forms.EmailField()

class ProvisoriosFormulario(forms.Form):
    nombreProvisorio=forms.CharField(max_length=40)
    tipo=forms.CharField(max_length=40)
    genero= forms.CharField(max_length=40)
    animalesenCasa=forms.CharField(max_length=40)
    telefono=forms.IntegerField()
    mail= forms.EmailField()

class EncontradosFormulario(forms.Form):
    nombreRetiene=forms.CharField(max_length=40)
    telefono=forms.IntegerField()
    mail= forms.EmailField()