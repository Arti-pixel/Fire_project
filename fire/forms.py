from django.forms import DateInput, DateTimeInput, ModelForm
from .models import *

from django import forms


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    username = forms.CharField(
        label="Логин",
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )
    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label="Логин",
        error_messages={"required": "Пользователь с таким Логином уже существует"},
    )
    first_name = forms.CharField(label="Имя")
    email = forms.EmailField(label="Ваш e-mail")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают.")
        return cd["password2"]


class FormControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})

class GeneralDataForm(ModelForm):
    class Meta:
        model = GeneralData
        fields = [
            "settlement",
            "locality_type",
            "address",
            "point_of_contact",
            "fire_object",
            "floors_number",
            "degree_of_fireres",
            "object_charact",
        ]

        labels = {
            "settlement": "Населённый пункт",
            "locality_type": "Вид населённого пункта",
            "address": "Адрес места пожара",
            "point_of_contact": "Район выезда ПЧ",
            "fire_object": "Объект пожара",
            "floors_number": "Этажность объекта",
            "degree_of_fireres": "Степень огнестойкости",
            "object_charact": "Описание",
        }


class GeneralDataFormFilter(GeneralDataForm):
    def __init__(self, *args, **kwargs):
        super(GeneralDataFormFilter, self).__init__(*args, **kwargs)
        self.fields["settlement"].required = False
        self.fields["settlement"].widget.attrs.update({"class":"form-control"})
        self.fields["locality_type"].required = False
        self.fields["locality_type"].widget.attrs.update({"class":"form-control"})
        self.fields["address"].required = False
        self.fields["address"].widget.attrs.update({"class":"form-control"})
        self.fields["point_of_contact"].required = False
        self.fields["point_of_contact"].widget.attrs.update({"class":"form-control"})
        self.fields["fire_object"].required = False
        self.fields["fire_object"].widget.attrs.update({"class":"form-control"})
        self.fields["floors_number"].required = False
        self.fields["floors_number"].widget.attrs.update({"class":"form-control"})
        self.fields["degree_of_fireres"].required = False
        self.fields["degree_of_fireres"].widget.attrs.update({"class":"form-control"})
        self.fields["object_charact"].required = False
        self.fields["object_charact"].widget.attrs.update({"class":"form-control"})


class FireManagerForm(ModelForm):
    class Meta:
        model = FireManager
        fields = [
            "manager",
            "full_name",
        ]


class FireConseqBuildingForm(ModelForm, FormControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})

    class Meta:
        model = FireConseqBuilding
        exclude = [
            "card_id",
        ]


class FireConseqPeopleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FireConseqPeople
        exclude = [
            "card_id",
        ]
        widgets = {
            "first_deceased_detect": DateTimeInput(attrs={"type": "datetime-local"}),
            "last_deceased_detect": DateTimeInput(attrs={"type": "datetime-local"}),
        }


class FireDescrForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FireDescr
        exclude = [
            "card_id",
        ]


class FireEquipForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FireEquip
        exclude = [
            "card_id",
        ]


class FireExtingAgentsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FireExtingAgents
        exclude = [
            "card_id",
        ]


class FireExtingAgentsConsumForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FireExtingAgentsConsum
        exclude = [
            "card_id",
        ]



class FireServicesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FireServices
        exclude = [
            "card_id",
        ]
        widgets = {"divis_date": DateTimeInput(attrs={"type": "datetime-local"})}


class FirefightCardAuthForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = FirefightCardAuth
        exclude = [
            "card_id",
        ]


class OthFireServicesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = OthFireServices
        exclude = [
            "card_id",
        ]
        widgets = {"oth_divis_date": DateTimeInput(attrs={"type": "datetime-local"})}


class OthServicesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = OthServices
        exclude = [
            "card_id",
        ]
        widgets = {"oth_serv_date": DateTimeInput(attrs={"type": "datetime-local"})}


class PersonnelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = Personnel
        exclude = [
            "card_id",
        ]


class PrimFireExtingMeansForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = PrimFireExtingMeans
        exclude = [
            "card_id",
        ]


class SpecFireEquipForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = SpecFireEquip
        exclude = [
            "card_id",
        ]


class TimeIndicatorsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = TimeIndicators
        exclude = [
            "card_id",
        ]
        widgets = {
            "oth_divis_date": DateTimeInput(attrs={"type": "datetime-local"}),
            "fire_detection": DateTimeInput(attrs={"type": "datetime-local"}),
            "fire_report": DateTimeInput(attrs={"type": "datetime-local"}),
            "departure_to_fire": DateTimeInput(attrs={"type": "datetime-local"}),
            "first_arrival": DateTimeInput(attrs={"type": "datetime-local"}),
            "first_barrel": DateTimeInput(attrs={"type": "datetime-local"}),
            "localiz_date": DateTimeInput(attrs={"type": "datetime-local"}),
            "open_fire_elim": DateTimeInput(attrs={"type": "datetime-local"}),
            "fire_conseq_elim": DateTimeInput(attrs={"type": "datetime-local"}),
            "firestation_return_date": DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TrunksToExtingFireForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = TrunksToExtingFire
        exclude = [
            "card_id",
        ]


class WaterSupplyOnFireForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.keys():
            self.fields[f].widget.attrs.update({"class":"form-control"})    
    class Meta:
        model = WaterSupplyOnFire
        exclude = [
            "card_id",
        ]
