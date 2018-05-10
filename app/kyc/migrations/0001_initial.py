# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 21:07
from __future__ import unicode_literals

import app.core.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrespondanceAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('use_poa_for_local_address', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True, verbose_name=b'Correspondence Address')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name=b'City / Town / Village')),
                ('district', models.CharField(blank=True, max_length=30, verbose_name=b'District')),
                ('indian_state', models.CharField(blank=True, choices=[(b'AS', b'Assam'), (b'BR', b'Bihar'), (b'KA', b'Karnataka'), (b'KL', b'Kerala'), (b'XX', b'Others')], max_length=2, verbose_name=b'State')),
                ('zipcode', models.CharField(blank=True, max_length=7, verbose_name=b'State')),
                ('country', models.CharField(blank=True, choices=[(b'AF', b'AFGANISTAN'), (b'BE', b'BELGIUM'), (b'BT', b'BHUTAN'), (b'CN', b'CHINA'), (b'IN', b'INDIA'), (b'IL', b'ISRAEL'), (b'SE', b'SWEDEN'), (b'ZW', b'ZIMBAWE')], default=b'IN', max_length=2, verbose_name=b'Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kyc_correspondance_address',
                'verbose_name': 'Correspondance Address',
            },
            bases=(models.Model, app.core.models.ModelHelperMixin),
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RelatedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('related_person_type', models.IntegerField(choices=[(1, b'Guardian'), (2, b'Assignee'), (3, b'Authorized Representative')], verbose_name=b'Related Person Type')),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Last Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name=b'Middle Name')),
                ('prefix', models.IntegerField(choices=[(1, b'Mr'), (2, b'Mrs'), (3, b'Miss'), (4, b'Dr')], verbose_name=b'Prefix')),
                ('poi_type', models.IntegerField(blank=True, choices=[(1, b'Passport'), (2, b'Voters Id'), (3, b'Driving License'), (4, b'Aadhaar'), (5, b'Nrega Job Card'), (6, b'Others')], null=True, verbose_name=b'Proof Of Identity Type')),
                ('poi_number', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'Proof Of Identity Identity Number')),
                ('passport_expiry_date', models.DateField(blank=True, null=True, verbose_name=b'Passport Expiry Date')),
                ('dl_expiry_date', models.DateField(blank=True, null=True, verbose_name=b'Driver License Expiry Date')),
                ('other_poi_name', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Other Identity Document Name')),
                ('poi_document', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], verbose_name=b'Proof of Identity Document')),
            ],
            options={
                'db_table': 'kyc_related_person',
                'verbose_name': 'KYC Related Person',
            },
            bases=(models.Model, app.core.models.ModelHelperMixin),
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserKYC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('photo', django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name=b'Photo')),
                ('is_pan_excempt', models.BooleanField(default=False, verbose_name=b'Are You PAN Excempt Investor')),
                ('pan_number', models.CharField(blank=True, max_length=14, verbose_name=b'PAN Number')),
                ('pan_document', django.contrib.postgres.fields.jsonb.JSONField(default=[], verbose_name=b'PAN Document')),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Last Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name=b'Middle Name')),
                ('prefix', models.IntegerField(choices=[(1, b'Mr'), (2, b'Mrs'), (3, b'Miss'), (4, b'Dr')], verbose_name=b'Prefix')),
                ('maiden_first_name', models.CharField(blank=True, max_length=100, verbose_name=b'Maiden First Name')),
                ('maiden_last_name', models.CharField(blank=True, max_length=50, verbose_name=b'Maiden Last Name')),
                ('maiden_middle_name', models.CharField(blank=True, max_length=50, verbose_name=b'Maiden Middle Name')),
                ('maiden_prefix', models.IntegerField(blank=True, choices=[(1, b'Mr'), (2, b'Mrs'), (3, b'Miss'), (4, b'Dr')], null=True, verbose_name=b'Prefix')),
                ('guardian_first_name', models.CharField(max_length=100, verbose_name=b'Father/Spouse First Name')),
                ('guardian_last_name', models.CharField(max_length=50, verbose_name=b'Father/Spouse Last Name')),
                ('guardian_middle_name', models.CharField(blank=True, max_length=50, verbose_name=b'Father/Spouse Middle Name')),
                ('guardian_prefix', models.IntegerField(choices=[(1, b'Mr'), (2, b'Mrs'), (3, b'Miss'), (4, b'Dr')], verbose_name=b'Prefix')),
                ('mother_first_name', models.CharField(max_length=100, verbose_name=b'Mother First Name')),
                ('mother_last_name', models.CharField(max_length=50, verbose_name=b'Mother Last Name')),
                ('mother_middle_name', models.CharField(blank=True, max_length=50, verbose_name=b'Mother Middle Name')),
                ('mother_prefix', models.IntegerField(choices=[(1, b'Mr'), (2, b'Mrs'), (3, b'Miss'), (4, b'Dr')], default=2, verbose_name=b'Prefix')),
                ('birth_date', models.DateField(verbose_name=b'Date Of Birth')),
                ('gender', models.IntegerField(choices=[(1, b'Male'), (2, b'Female'), (3, b'Transgender')], verbose_name=b'Gender')),
                ('marital_status', models.IntegerField(choices=[(1, b'Married'), (2, b'Unmarried'), (3, b'Others')], verbose_name=b'Marital Status')),
                ('citizen', models.CharField(choices=[(b'AF', b'AFGANISTAN'), (b'BE', b'BELGIUM'), (b'BT', b'BHUTAN'), (b'CN', b'CHINA'), (b'IN', b'INDIA'), (b'IL', b'ISRAEL'), (b'SE', b'SWEDEN'), (b'ZW', b'ZIMBAWE')], default=b'IN', max_length=2, verbose_name=b'Citizenship')),
                ('residential_status', models.IntegerField(choices=[(1, b'Resident Individual'), (2, b'Non Resident Individual'), (3, b'Foriegn National'), (4, b'Person Of Indian Origin')], verbose_name=b'Residential Status')),
                ('occupation_type', models.IntegerField(choices=[(1, b'Services'), (2, b'Private Sector'), (3, b'Public Sector'), (4, b'Government Sector'), (5, b'Professional'), (6, b'Self Employeed'), (7, b'Retired'), (8, b'House Wife'), (9, b'Student'), (10, b'Business'), (11, b'Others'), (12, b'Not Categorised')], verbose_name=b'Occupation Type')),
                ('poi_type', models.IntegerField(blank=True, choices=[(1, b'Passport'), (2, b'Voters Id'), (3, b'Driving License'), (4, b'Aadhaar'), (5, b'Nrega Job Card'), (6, b'Others')], null=True, verbose_name=b'Proof Of Identity Type')),
                ('poi_number', models.CharField(blank=True, max_length=20, verbose_name=b'Proof Of Identity Number')),
                ('passport_expiry_date', models.DateField(blank=True, null=True, verbose_name=b'Passport Expiry Date')),
                ('dl_expiry_date', models.DateField(blank=True, null=True, verbose_name=b'Driver License Expiry Date')),
                ('other_poi_name', models.CharField(blank=True, max_length=30, verbose_name=b'Other Identity Document Name')),
                ('poi_document', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], verbose_name=b'Proof of Identity Document')),
                ('address', models.TextField(verbose_name=b'Current / Permanent / Overseas Address')),
                ('city', models.CharField(max_length=30, verbose_name=b'City / Town / Village')),
                ('district', models.CharField(max_length=30, verbose_name=b'District')),
                ('indian_state', models.CharField(blank=True, choices=[(b'AS', b'Assam'), (b'BR', b'Bihar'), (b'KA', b'Karnataka'), (b'KL', b'Kerala'), (b'XX', b'Others')], max_length=2, verbose_name=b'State')),
                ('zipcode', models.CharField(blank=True, max_length=7, verbose_name=b'Postal Code')),
                ('country', models.CharField(choices=[(b'AF', b'AFGANISTAN'), (b'BE', b'BELGIUM'), (b'BT', b'BHUTAN'), (b'CN', b'CHINA'), (b'IN', b'INDIA'), (b'IL', b'ISRAEL'), (b'SE', b'SWEDEN'), (b'ZW', b'ZIMBAWE')], default=b'IN', max_length=2, verbose_name=b'Country')),
                ('address_type', models.IntegerField(choices=[(1, b'Residence'), (2, b'Business'), (3, b'Registered Office'), (4, b'Residence / Business'), (5, b'Unspecified')], verbose_name=b'Address type')),
                ('poa_type', models.IntegerField(choices=[(1, b'Passport'), (2, b'Voters Id'), (3, b'Driving License'), (4, b'Aadhaar'), (5, b'Nrega Job Card'), (6, b'Others')], verbose_name=b'Proof Of Address Type')),
                ('poa_number', models.CharField(max_length=20, verbose_name=b'Proof Of Address Identity Number')),
                ('poa_passport_expiry_date', models.DateField(blank=True, null=True, verbose_name=b'Passport Expiry Date')),
                ('poa_dl_expiry_date', models.DateField(blank=True, null=True, verbose_name=b'Driver License Expiry Date')),
                ('poa_other_poi_name', models.CharField(blank=True, max_length=30, verbose_name=b'Other Identity Document Name')),
                ('poa_document', django.contrib.postgres.fields.jsonb.JSONField(default=[], verbose_name=b'Proof of Address Document')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email Address')),
                ('mobile_country_code', models.PositiveIntegerField(verbose_name=b'Mobile Country Code')),
                ('mobile', models.PositiveIntegerField(verbose_name=b'Mobile')),
                ('office_tel_prefix', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'STD Code')),
                ('office_telephone', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Office Telephone Number')),
                ('home_tel_prefix', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'STD Code')),
                ('home_telephone', models.PositiveIntegerField(blank=True, null=True, verbose_name=b'Home Telephone Number')),
                ('is_fatca_applicable', models.BooleanField(default=False)),
                ('fatca_country_judistriction', models.CharField(blank=True, choices=[(b'AF', b'AFGANISTAN'), (b'BE', b'BELGIUM'), (b'BT', b'BHUTAN'), (b'CN', b'CHINA'), (b'IN', b'INDIA'), (b'IL', b'ISRAEL'), (b'SE', b'SWEDEN'), (b'ZW', b'ZIMBAWE')], max_length=2, verbose_name=b'Country of Jurisdiction of Residence')),
                ('fatca_tin_number', models.CharField(blank=True, max_length=20, verbose_name=b'Tax Identification Number')),
                ('fatca_place_of_birth', models.CharField(blank=True, max_length=30, verbose_name=b'Place of Birth')),
                ('fatca_country_of_birth', models.CharField(blank=True, choices=[(b'AF', b'AFGANISTAN'), (b'BE', b'BELGIUM'), (b'BT', b'BHUTAN'), (b'CN', b'CHINA'), (b'IN', b'INDIA'), (b'IL', b'ISRAEL'), (b'SE', b'SWEDEN'), (b'ZW', b'ZIMBAWE')], default=b'IN', max_length=2, verbose_name=b'Country of Birth')),
                ('fatca_address', models.TextField(blank=True, verbose_name=b'Address')),
                ('fatca_city', models.CharField(blank=True, max_length=30, verbose_name=b'City / Town / Village')),
                ('fatca_district', models.CharField(blank=True, max_length=30, verbose_name=b'District')),
                ('fatca_indian_state', models.CharField(blank=True, choices=[(b'AS', b'Assam'), (b'BR', b'Bihar'), (b'KA', b'Karnataka'), (b'KL', b'Kerala'), (b'XX', b'Others')], max_length=2, verbose_name=b'State')),
                ('fatca_zipcode', models.CharField(blank=True, max_length=7, verbose_name=b'Zipcode')),
                ('fatca_country', models.CharField(blank=True, choices=[(b'AF', b'AFGANISTAN'), (b'BE', b'BELGIUM'), (b'BT', b'BHUTAN'), (b'CN', b'CHINA'), (b'IN', b'INDIA'), (b'IL', b'ISRAEL'), (b'SE', b'SWEDEN'), (b'ZW', b'ZIMBAWE')], default=b'IN', max_length=2, verbose_name=b'Country')),
                ('remarks', models.TextField(blank=True)),
                ('kyc_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message=b'KYC Number must be a 12 digit number', regex=b'^\\d{12}$')])),
                ('application_forms', models.ManyToManyField(related_name='kyc_related_persons', to='eform.ApplicationForm')),
                ('correspondance_addresses', models.ManyToManyField(related_name='kyc_corresponding_address', to='kyc.CorrespondanceAddress')),
                ('related_persons', models.ManyToManyField(related_name='kyc_related_persons', to='kyc.RelatedPerson')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kyc_user_kyc_info',
                'verbose_name': 'User KYC',
            },
            bases=(models.Model, app.core.models.ModelHelperMixin),
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
