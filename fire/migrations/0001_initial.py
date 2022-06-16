# Generated by Django 4.0 on 2022-06-15 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralData',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('settlement', models.CharField(choices=[('murmansk', 'Мурманск')], max_length=300)),
                ('locality_type', models.CharField(choices=[('town', 'город'), ('village', 'село'), ('township', 'поселок'), ('station', 'станция'), ('siding', 'разъезд'), ('oth_locals', 'иные населённые пункты')], max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('point_of_contact', models.CharField(choices=[('fs_1', '1 ПСЧ'), ('fs_2', '2 ПСЧ')], max_length=300)),
                ('fire_object', models.CharField(max_length=300)),
                ('floors_number', models.IntegerField(blank=True, null=True)),
                ('degree_of_fireres', models.IntegerField(blank=True, choices=[(1, '|'), (2, '||'), (3, '|||')], null=True)),
                ('object_charact', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FireConseqBuilding',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('build_destr', models.IntegerField()),
                ('build_destr_sq', models.FloatField()),
                ('build_damag', models.IntegerField()),
                ('build_damag_sq', models.FloatField()),
                ('destr_tech', models.IntegerField()),
                ('saved_tech', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FireConseqPeople',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('peop_died', models.IntegerField()),
                ('dead_child', models.IntegerField()),
                ('first_deceased_detect', models.DateTimeField(blank=True, null=True)),
                ('last_deceased_detect', models.DateTimeField(blank=True, null=True)),
                ('traum_people', models.IntegerField()),
                ('traum_child', models.IntegerField()),
                ('evac_people', models.IntegerField()),
                ('evac_child', models.IntegerField()),
                ('saved_people', models.IntegerField()),
                ('saved_child', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FireDescr',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('fire_grade', models.CharField(choices=[('fire_rank_1', 'пожар №1'), ('fire_rank_2', 'пожар №2')], max_length=300)),
                ('exting_forces', models.CharField(choices=[('federal fire service', 'федеральная противопопожарная служба')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FireEquip',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('fire_tank_truck', models.IntegerField()),
                ('fire_tank_truck_lad', models.IntegerField()),
                ('powder_exting_vehicl', models.IntegerField()),
                ('foam_exting_vehicl', models.IntegerField()),
                ('fire_truck_pump_stat', models.IntegerField()),
                ('first_aid_vehicl', models.IntegerField()),
                ('pump_bag_car', models.IntegerField()),
                ('fire_eng_pump', models.IntegerField()),
                ('oth_fire_equip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FireExtingAgents',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('compact_and_sprayed_water', models.BooleanField()),
                ('wetting_agent', models.BooleanField()),
                ('gas', models.BooleanField()),
                ('powder', models.BooleanField()),
                ('gas_aerosol', models.BooleanField()),
                ('air_mech_foam_low', models.BooleanField()),
                ('air_mech_foam_med', models.BooleanField()),
                ('air_mech_foam_high', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FireExtingAgentsConsum',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('water_consum', models.IntegerField()),
                ('foam_agent_consum', models.IntegerField()),
                ('powder_agent_consum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FirefightCardAuth',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('division_auth', models.CharField(max_length=300)),
                ('post', models.CharField(max_length=300)),
                ('full_name_auth', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FireManager',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('manager', models.CharField(max_length=300)),
                ('full_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FireServices',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('divis', models.CharField(max_length=300)),
                ('divis_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OthFireServices',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('oth_divis', models.CharField(max_length=300)),
                ('oth_divis_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OthServices',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('oth_serv_name', models.CharField(max_length=300)),
                ('oth_serv_date', models.DateTimeField(blank=True, null=True)),
                ('oth_serv_personnel', models.IntegerField(blank=True, null=True)),
                ('oth_serv_tech', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('fed_fire_serv', models.IntegerField()),
                ('reg_fire_serv', models.IntegerField()),
                ('volunt_fire_serv', models.IntegerField()),
                ('depart_fire_serv', models.IntegerField()),
                ('munic_fire_serv', models.IntegerField()),
                ('priv_fire_serv', models.IntegerField()),
                ('org_fire_brig', models.IntegerField()),
                ('work_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PrimFireExtingMeans',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('water_sup_by_improvised_means', models.BooleanField()),
                ('water_from_internal_plumbing', models.BooleanField()),
                ('air_foam_fire_exting', models.BooleanField()),
                ('carbon_dioxide_fire_exting', models.BooleanField()),
                ('powder_fire_exting', models.BooleanField()),
                ('refrigerat_fire_exting', models.BooleanField()),
                ('comb_fire_exting', models.BooleanField()),
                ('gas_aerosol_fire_exting', models.BooleanField()),
                ('fire_cloth', models.BooleanField()),
                ('sand', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecFireEquip',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('fire_truck_lad', models.IntegerField()),
                ('fire_truck_lift', models.IntegerField()),
                ('fire_hose_truck', models.IntegerField()),
                ('gas_protect_serv_vehicl', models.IntegerField()),
                ('gas_protect_serv_fire_truck', models.IntegerField()),
                ('fire_headq_vehicl', models.IntegerField()),
                ('multi_purp_fire_truck', models.IntegerField()),
                ('fire_test_lab', models.IntegerField()),
                ('fire_resc_vehicle', models.IntegerField()),
                ('mob_compr_stat', models.IntegerField()),
                ('fire_truck_trailer', models.IntegerField()),
                ('fire_crane', models.IntegerField()),
                ('oth_spec_fire_equip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrunksToExtingFire',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('trunk_a', models.IntegerField()),
                ('trunk_b', models.IntegerField()),
                ('gun_carriage_barrel', models.IntegerField()),
                ('foam_barrel', models.IntegerField()),
                ('powder_barrel', models.IntegerField()),
                ('wat_barrel', models.IntegerField()),
                ('high_pres_barrel', models.IntegerField()),
                ('satchel_fire_exting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WaterSupplyOnFire',
            fields=[
                ('card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fire.generaldata')),
                ('from_fire_tanker_truck', models.BooleanField()),
                ('from_fire_crane', models.BooleanField()),
                ('fire_hydrant_main_line', models.BooleanField()),
                ('fire_hydrant_water_deliv', models.BooleanField()),
                ('fire_hydrant_in_pump', models.BooleanField()),
                ('fire_tower_main_line', models.BooleanField()),
                ('fire_tower_water_deliv', models.BooleanField()),
                ('fire_tower_in_pump', models.BooleanField()),
                ('fire_pier_main_line', models.BooleanField()),
                ('fire_truck_trailer_deliv', models.BooleanField()),
                ('fire_truck_trailer_in_pump', models.BooleanField()),
                ('hydr_elev', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_detection', models.DateTimeField()),
                ('fire_report', models.DateTimeField()),
                ('departure_to_fire', models.DateTimeField()),
                ('departure_circum', models.CharField(max_length=300)),
                ('fire_obj_dist', models.FloatField()),
                ('first_arrival', models.DateTimeField()),
                ('first_arrival_s', models.IntegerField()),
                ('first_barrel', models.DateTimeField()),
                ('first_barrel_s', models.IntegerField()),
                ('localiz_date', models.DateTimeField()),
                ('localization_date_s', models.IntegerField()),
                ('open_fire_elim', models.DateTimeField()),
                ('fire_conseq_elim', models.DateTimeField()),
                ('firestation_return_date', models.DateTimeField()),
                ('ref_card_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fire.generaldata')),
            ],
        ),
    ]