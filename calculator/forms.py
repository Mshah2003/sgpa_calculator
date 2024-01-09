from django import forms

class SGPAForm(forms.Form):
    GRADE_CHOICES = [
        ('A++', 'A++'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('E+', 'E+'),
        ('E', 'E'),
        ('F', 'F'),
    ]

    EM = forms.ChoiceField(choices=GRADE_CHOICES, label="Engineering Mathematics")
    BEE = forms.ChoiceField(choices=GRADE_CHOICES, label="Basic Electrical Engg / Basic Civil Engg")
    EC = forms.ChoiceField(choices=GRADE_CHOICES, label="Engg Chemistry / Engg Physics")
    BME = forms.ChoiceField(choices=GRADE_CHOICES, label="Basic Mechanical Engineering / PPS")
    CS = forms.ChoiceField(choices=GRADE_CHOICES, label="Communication Skills / Human Values")
    LL = forms.ChoiceField(choices=GRADE_CHOICES, label="Language Lab / Human Values Lab")
    MPW = forms.ChoiceField(choices=GRADE_CHOICES, label="Manufacturing Practices Workshop / Computer prog. Lab")
    CL = forms.ChoiceField(choices=GRADE_CHOICES, label="Chemistry Lab / Physics Lab")
    BEEL = forms.ChoiceField(choices=GRADE_CHOICES, label="Basic Electrical Engineering Lab / Civil lab")
    CAED = forms.ChoiceField(choices=GRADE_CHOICES, label="Computer Aided Machine Drawing / Engg graphics")
    DECA = forms.ChoiceField(choices=GRADE_CHOICES, label="DECA")
