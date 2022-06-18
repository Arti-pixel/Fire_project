from django.forms import DateInput, DateTimeInput, ModelForm
from .models import *


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

class GeneralDataFormFilter(GeneralDataForm):
    def __init__(self, *args, **kwargs):
        super(GeneralDataFormFilter, self).__init__(*args, **kwargs)
        self.fields["settlement"].required = False
        self.fields["locality_type"].required = False
        self.fields["address"].required = False
        self.fields["point_of_contact"].required = False
        self.fields["fire_object"].required = False
        self.fields["floors_number"].required = False
        self.fields["degree_of_fireres"].required = False
        self.fields["object_charact"].required = False

class FireManagerForm(ModelForm):
    class Meta:
        model = FireManager
        fields = [
            "manager",
            "full_name",
        ]


class FireConseqBuildingForm(ModelForm):
    class Meta:
        model = FireConseqBuilding
        exclude = [
            "card_id",            
        ]


class FireConseqPeopleForm(ModelForm):
    class Meta:
        model = FireConseqPeople
        exclude = [
            "card_id",            
        ]
        widgets = {            
            "first_deceased_detect": DateTimeInput(attrs={'type': 'datetime-local'}),
            "last_deceased_detect": DateTimeInput(attrs={'type': 'datetime-local'})
        }




class FireDescrForm(ModelForm):
    class Meta:
        model = FireDescr
        exclude = [
            "card_id",            
        ]


class FireEquipForm(ModelForm):
    class Meta:
        model = FireEquip
        exclude = [
            "card_id",            
        ]


class FireExtingAgentsForm(ModelForm):
    class Meta:
        model = FireExtingAgents
        exclude = [
            "card_id",            
        ]


class FireExtingAgentsConsumForm(ModelForm):
    class Meta:
        model = FireExtingAgentsConsum
        exclude = [
            "card_id",            
        ]


class FireServicesForm(ModelForm):
    class Meta:
        model = FireServices
        exclude = [
            "card_id",            
        ]
        widgets = {
            "divis_date": DateTimeInput(attrs={'type': 'datetime-local'})
        }


class FirefightCardAuthForm(ModelForm):
    class Meta:
        model = FirefightCardAuth
        exclude = [
            "card_id",            
        ]


class OthFireServicesForm(ModelForm):
    class Meta:
        model = OthFireServices
        exclude = [
            "card_id",            
        ]
        widgets = {
            "oth_divis_date": DateTimeInput(attrs={'type': 'datetime-local'})
        }

class OthServicesForm(ModelForm):
    class Meta:
        model = OthServices
        exclude = [
            "card_id",            
        ]        
        widgets = {
            "oth_serv_date": DateTimeInput(attrs={'type': 'datetime-local'})
        }        


class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        exclude = [
            "card_id",            
        ]


class PrimFireExtingMeansForm(ModelForm):
    class Meta:
        model = PrimFireExtingMeans
        exclude = [
            "card_id",            
        ]


class SpecFireEquipForm(ModelForm):
    class Meta:
        model = SpecFireEquip
        exclude = [
            "card_id",            
        ]


class TimeIndicatorsForm(ModelForm):
    class Meta:
        model = TimeIndicators
        exclude = [
            "card_id",            
        ]
        widgets = {
            "oth_divis_date": DateTimeInput(attrs={'type': 'datetime-local'}),
            "fire_detection": DateTimeInput(attrs={'type': 'datetime-local'}),
            "fire_report": DateTimeInput(attrs={'type': 'datetime-local'}),
            "departure_to_fire": DateTimeInput(attrs={'type': 'datetime-local'}),
            "first_arrival": DateTimeInput(attrs={'type': 'datetime-local'}),
            "first_barrel": DateTimeInput(attrs={'type': 'datetime-local'}),
            "localiz_date": DateTimeInput(attrs={'type': 'datetime-local'}),
            "open_fire_elim": DateTimeInput(attrs={'type': 'datetime-local'}),
            "fire_conseq_elim": DateTimeInput(attrs={'type': 'datetime-local'}),
            "firestation_return_date": DateTimeInput(attrs={'type': 'datetime-local'}),
            }





class TrunksToExtingFireForm(ModelForm):
    class Meta:
        model = TrunksToExtingFire
        exclude = [
            "card_id",            
        ]


class WaterSupplyOnFireForm(ModelForm):
    class Meta:
        model = WaterSupplyOnFire
        exclude = [
            "card_id",            
        ]

