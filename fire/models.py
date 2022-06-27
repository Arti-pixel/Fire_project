from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    sub_end_date = models.DateField(null=True, blank=True)

    @property
    def sub_is_active(self):
        now = datetime.now().date()
        if self.sub_end_date:
            if self.sub_end_date > now:
                return True
            else:
                return False
        else:
            return False


class GeneralData(models.Model):
    sattelment_choices = [("murmansk", "Мурманск")]

    locality_type_choices = [
        ("town", "город"),
        ("village", "село"),
        ("township", "поселок"),
        ("station", "станция"),
        ("siding", "разъезд"),
        ("oth_locals", "иные населённые пункты"),
    ]

    pof_choices = [("fs_1", "1 ПСЧ"), ("fs_2", "2 ПСЧ")]
    dof_choices = [
        (1, "|"),
        (2, "||"),
        (3, "|||"),
    ]

    card_id = models.AutoField(primary_key=True)

    settlement = models.CharField(
        max_length=300, null=False, blank=False, choices=sattelment_choices
    )
    locality_type = models.CharField(
        max_length=300, null=False, blank=False, choices=locality_type_choices
    )

    address = models.CharField(max_length=300, null=False, blank=False)
    point_of_contact = models.CharField(
        max_length=300, null=False, blank=False, choices=pof_choices
    )
    fire_object = models.CharField(max_length=300, null=False, blank=False)
    floors_number = models.IntegerField(null=True, blank=True)
    degree_of_fireres = models.IntegerField(null=True, blank=True, choices=dof_choices)
    object_charact = models.TextField(null=False, blank=False)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)


class FireManager(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    manager = models.CharField(max_length=300, null=False, blank=False)
    full_name = models.CharField(max_length=300, null=False, blank=False)


class FireConseqBuilding(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    build_destr = models.IntegerField(null=False, blank=False)
    build_destr_sq = models.FloatField(null=False, blank=False)
    build_damag = models.IntegerField(null=False, blank=False)
    build_damag_sq = models.FloatField(null=False, blank=False)
    destr_tech = models.IntegerField(null=False, blank=False)
    saved_tech = models.IntegerField(null=False, blank=False)


class FireConseqPeople(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    peop_died = models.IntegerField(null=False, blank=False)
    dead_child = models.IntegerField(null=False, blank=False)
    first_deceased_detect = models.DateTimeField(null=True, blank=True)
    last_deceased_detect = models.DateTimeField(null=True, blank=True)
    traum_people = models.IntegerField(null=False, blank=False)
    traum_child = models.IntegerField(null=False, blank=False)
    evac_people = models.IntegerField(null=False, blank=False)
    evac_child = models.IntegerField(null=False, blank=False)
    saved_people = models.IntegerField(null=False, blank=False)
    saved_child = models.IntegerField(null=False, blank=False)


class FireDescr(models.Model):
    fire_choices = [
        ("fire_rank_1", "пожар №1"),
        ("fire_rank_2", "пожар №2"),
    ]
    exting_forces_choices = [(
        "federal fire service",
        "федеральная противопопожарная служба",
        )
    ]

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    fire_grade = models.CharField(
        max_length=300, null=False, blank=False, choices=fire_choices
    )
    exting_forces = models.CharField(
        max_length=300, null=False, blank=False, choices=exting_forces_choices
    )


class FireEquip(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    fire_tank_truck = models.IntegerField(null=False, blank=False)
    fire_tank_truck_lad = models.IntegerField(null=False, blank=False)
    powder_exting_vehicl = models.IntegerField(null=False, blank=False)
    foam_exting_vehicl = models.IntegerField(null=False, blank=False)
    fire_truck_pump_stat = models.IntegerField(null=False, blank=False)
    first_aid_vehicl = models.IntegerField(null=False, blank=False)
    pump_bag_car = models.IntegerField(null=False, blank=False)
    fire_eng_pump = models.IntegerField(null=False, blank=False)
    oth_fire_equip = models.IntegerField(null=False, blank=False)


class FireExtingAgents(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    compact_and_sprayed_water = models.BooleanField(null=False, blank=False)
    wetting_agent = models.BooleanField(null=False, blank=False)
    gas = models.BooleanField(null=False, blank=False)
    powder = models.BooleanField(null=False, blank=False)
    gas_aerosol = models.BooleanField(null=False, blank=False)
    air_mech_foam_low = models.BooleanField(null=False, blank=False)
    air_mech_foam_med = models.BooleanField(null=False, blank=False)
    air_mech_foam_high = models.BooleanField(null=False, blank=False)


class FireExtingAgentsConsum(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    water_consum = models.IntegerField(null=False, blank=False)
    foam_agent_consum = models.IntegerField(null=False, blank=False)
    powder_agent_consum = models.IntegerField(null=False, blank=False)


class FireServices(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    divis = models.CharField(max_length=300, null=False, blank=False)
    divis_date = models.DateTimeField(null=True, blank=True)


class FirefightCardAuth(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    division_auth = models.CharField(max_length=300, null=False, blank=False)
    post = models.CharField(max_length=300, null=False, blank=False)
    full_name_auth = models.CharField(max_length=300, null=False, blank=False)


class OthFireServices(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    oth_divis = models.CharField(max_length=300, null=False, blank=False)
    oth_divis_date = models.DateTimeField(null=True, blank=True)


class OthServices(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    oth_serv_name = models.CharField(max_length=300, null=False, blank=False)
    oth_serv_date = models.DateTimeField(null=True, blank=True)
    oth_serv_personnel = models.IntegerField(null=True, blank=True)
    oth_serv_tech = models.IntegerField(null=True, blank=True)


class Personnel(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    fed_fire_serv = models.IntegerField(null=False, blank=False)
    reg_fire_serv = models.IntegerField(null=False, blank=False)
    volunt_fire_serv = models.IntegerField(null=False, blank=False)
    depart_fire_serv = models.IntegerField(null=False, blank=False)
    munic_fire_serv = models.IntegerField(null=False, blank=False)
    priv_fire_serv = models.IntegerField(null=False, blank=False)
    org_fire_brig = models.IntegerField(null=False, blank=False)
    work_time = models.IntegerField(null=False, blank=False)


class PrimFireExtingMeans(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    water_sup_by_improvised_means = models.BooleanField(null=False, blank=False)
    water_from_internal_plumbing = models.BooleanField(null=False, blank=False)
    air_foam_fire_exting = models.BooleanField(null=False, blank=False)
    carbon_dioxide_fire_exting = models.BooleanField(null=False, blank=False)
    powder_fire_exting = models.BooleanField(null=False, blank=False)
    refrigerat_fire_exting = models.BooleanField(null=False, blank=False)
    comb_fire_exting = models.BooleanField(null=False, blank=False)
    gas_aerosol_fire_exting = models.BooleanField(null=False, blank=False)
    fire_cloth = models.BooleanField(null=False, blank=False)
    sand = models.BooleanField(null=False, blank=False)


class SpecFireEquip(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    fire_truck_lad = models.IntegerField(null=False, blank=False)
    fire_truck_lift = models.IntegerField(null=False, blank=False)
    fire_hose_truck = models.IntegerField(null=False, blank=False)
    gas_protect_serv_vehicl = models.IntegerField(null=False, blank=False)
    gas_protect_serv_fire_truck = models.IntegerField(null=False, blank=False)
    fire_headq_vehicl = models.IntegerField(null=False, blank=False)
    multi_purp_fire_truck = models.IntegerField(null=False, blank=False)
    fire_test_lab = models.IntegerField(null=False, blank=False)
    fire_resc_vehicle = models.IntegerField(null=False, blank=False)
    mob_compr_stat = models.IntegerField(null=False, blank=False)
    fire_truck_trailer = models.IntegerField(null=False, blank=False)
    fire_crane = models.IntegerField(null=False, blank=False)
    oth_spec_fire_equip = models.IntegerField(null=False, blank=False)


class TimeIndicators(models.Model):
    ref_card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, null=False
    )
    fire_detection = models.DateTimeField(null=False, blank=False)
    fire_report = models.DateTimeField(null=False, blank=False)
    departure_to_fire = models.DateTimeField(null=False, blank=False)
    departure_circum = models.CharField(max_length=300, null=False, blank=False)
    fire_obj_dist = models.FloatField(null=False, blank=False)
    first_arrival = models.DateTimeField(null=False, blank=False)
    first_arrival_s = models.IntegerField(null=False, blank=False)
    first_barrel = models.DateTimeField(null=False, blank=False)
    first_barrel_s = models.IntegerField(null=False, blank=False)
    localiz_date = models.DateTimeField(null=False, blank=False)
    localization_date_s = models.IntegerField(null=False, blank=False)
    open_fire_elim = models.DateTimeField(null=False, blank=False)
    fire_conseq_elim = models.DateTimeField(null=False, blank=False)
    firestation_return_date = models.DateTimeField(null=False, blank=False)


class TrunksToExtingFire(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    trunk_a = models.IntegerField(null=False, blank=False)
    trunk_b = models.IntegerField(null=False, blank=False)
    gun_carriage_barrel = models.IntegerField(null=False, blank=False)
    foam_barrel = models.IntegerField(null=False, blank=False)
    powder_barrel = models.IntegerField(null=False, blank=False)
    wat_barrel = models.IntegerField(null=False, blank=False)
    high_pres_barrel = models.IntegerField(null=False, blank=False)
    satchel_fire_exting = models.IntegerField(null=False, blank=False)


class WaterSupplyOnFire(models.Model):

    card_id = models.OneToOneField(
        GeneralData, on_delete=models.CASCADE, primary_key=True
    )
    from_fire_tanker_truck = models.BooleanField(null=False, blank=False)
    from_fire_crane = models.BooleanField(null=False, blank=False)
    fire_hydrant_main_line = models.BooleanField(null=False, blank=False)
    fire_hydrant_water_deliv = models.BooleanField(null=False, blank=False)
    fire_hydrant_in_pump = models.BooleanField(null=False, blank=False)
    fire_tower_main_line = models.BooleanField(null=False, blank=False)
    fire_tower_water_deliv = models.BooleanField(null=False, blank=False)
    fire_tower_in_pump = models.BooleanField(null=False, blank=False)
    fire_pier_main_line = models.BooleanField(null=False, blank=False)
    fire_truck_trailer_deliv = models.BooleanField(null=False, blank=False)
    fire_truck_trailer_in_pump = models.BooleanField(null=False, blank=False)
    hydr_elev = models.BooleanField(null=False, blank=False)
