from django import forms

class SGPAForm(forms.Form):
    EM = forms.CharField(label="Engineering Mathematics")
    BEE = forms.CharField(label="Basic Electrical Engg / Basic Civil Engg")
    EC = forms.CharField(label="Engg Chemistry / Engg Physics")
    BME = forms.CharField(label="Basic Mechanical Engineering / PPS")
    CS = forms.CharField(label="Communication Skills / Human Values")
    LL = forms.CharField(label="Language Lab / Human Values Lab")
    MPW = forms.CharField(label="Manufacturing Practices Workshop / Computer prog. Lab")
    CL = forms.CharField(label="Chemistry Lab / Physics Lab")
    BEEL = forms.CharField(label="Basic Electrical Engineering Lab / Civil lab")
    CAED = forms.CharField(label="Computer Aided Machine Drawing / Engg graphics")
    DECA = forms.CharField(label="DECA")