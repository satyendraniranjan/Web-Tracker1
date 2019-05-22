# Generated by Django 2.0.13 on 2019-05-22 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ericsson', '0006_auto_20190520_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSATracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cascade', models.CharField(blank=True, default='', max_length=255)),
                ('Technology', models.CharField(blank=True, choices=[('800 CDMA', '800 CDMA'), ('1900 CDMA', '1900 CDMA'), ('800 FDD', '800 FDD'), ('1900 FDD', '1900 FDD'), ('2.5 TDD', '2.5 TDD'), ('1900 800 CDMA', '1900/800 CDMA'), ('1900 800 FDD', '1900/800 FDD'), ('1900 700 CDMA', '1900/700 CDMA'), ('700 FDD', '700 FDD'), ('800 FDD CDMA', '800 FDD/CDMA')], max_length=255)),
                ('Type', models.CharField(blank=True, choices=[('CDU10', 'CDU10'), ('CDU20', 'CDU20'), ('CDU30', 'CDU30'), ('NA', 'NA')], max_length=255)),
                ('Bandwidth_Checked_From_LSM', models.CharField(blank=True, choices=[('3Mhz', '3Mhz'), ('5Mhz', '5Mhz'), ('10Mhz', '10Mhz'), ('20Mhz', '20Mhz'), ('5+10Mhz 5Mhz', '5+10Mhz/5Mhz'), ('5+10Mhz 3Mhz', '5+10Mhz/3Mhz'), ('10+5Mhz 5Mhz', '10+5Mhz/5Mhz'), ('10+5Mhz 3Mhz', '10+5Mhz/3Mhz'), ('NA', 'NA')], max_length=255)),
                ('Market', models.CharField(blank=True, choices=[('Kansas', 'Kansas'), ('Alaska', 'Alaska'), ('PR / VI', 'PR / VI'), ('DFW', 'DFW'), ('East Texas', 'East Texas'), ('Inland Northwest', 'Inland Northwest'), ('Albuquerque', 'Albuquerque'), ('Jacksonville', 'Jacksonville'), ('Nashville', 'Nashville'), ('West Texas', 'West Texas'), ('Washington DC', 'Washington DC'), ('East Iowa', 'East Iowa'), ('MT / WY', 'MT / WY'), ('South Carolina', 'South Carolina'), ('Riverside / San Bernardino', 'Riverside / San Bernardino'), ('East Kentucky', 'East Kentucky'), ('Alabama', 'Alabama'), ('West Kentucky', 'West Kentucky'), ('Dakotas', 'Dakotas'), ('Orlando', 'Orlando'), ('Central Iowa', 'Central Iowa'), ('Georgia', 'Georgia'), ('Missouri', 'Missouri'), ('Lower Central Valley', 'Lower Central Valley'), ('Atlanta / Athens', 'Atlanta / Athens'), ('Southern Jersey', 'Southern Jersey'), ('Idaho', 'Idaho'), ('LA Metro', 'LA Metro'), ('West Washington', 'West Washington'), ('Orange County', 'Orange County'), ('Oregon / SW Washington', 'Oregon / SW Washington'), ('Mississippi', 'Mississippi'), ('South Texas', 'South Texas'), ('San Antonio', 'San Antonio'), ('Milwaukee', 'Milwaukee'), ('Cincinnati', 'Cincinnati'), ('North Wisconsin', 'North Wisconsin'), ('Rochester', 'Rochester'), ('Houston', 'Houston'), ('Norfolk', 'Norfolk'), ('Miami / West Palm', 'Miami / West Palm'), ('Las Vegas', 'Las Vegas'), ('Cleveland', 'Cleveland'), ('East Michigan', 'East Michigan'), ('Chicago', 'Chicago'), ('SF Bay', 'SF Bay'), ('GA/SC Coast', 'GA/SC Coast'), ('Delaware', 'Delaware'), ('Phoenix', 'Phoenix'), ('West Iowa / Nebraska', 'West Iowa / Nebraska'), ('Pittsburgh', 'Pittsburgh'), ('Austin', 'Austin'), ('Tampa', 'Tampa'), ('Louisiana', 'Louisiana'), ('Gulf Coast', 'Gulf Coast'), ('Long Island', 'Long Island'), ('Charlotte', 'Charlotte'), ('Toledo', 'Toledo'), ('Minnesota', 'Minnesota'), ('Columbus', 'Columbus'), ('Philadelphia Metro', 'Philadelphia Metro'), ('Colorado', 'Colorado'), ('Oklahoma', 'Oklahoma'), ('Upper Central Valley', 'Upper Central Valley'), ('Ft. Wayne / South Bend', 'Ft. Wayne / South Bend'), ('Boston', 'Boston'), ('Raleigh / Durham', 'Raleigh / Durham'), ('Winston / Salem', 'Winston / Salem'), ('Arkansas', 'Arkansas'), ('San Diego', 'San Diego'), ('Myrtle Beach', 'Myrtle Beach'), ('Upstate NY East', 'Upstate NY East'), ('Central Illinois', 'Central Illinois'), ('Northern Jersey', 'Northern Jersey'), ('Central Pennsylvania', 'Central Pennsylvania'), ('The Panhandle', 'The Panhandle'), ('Providence', 'Providence'), ('Upstate NY Central', 'Upstate NY Central'), ('West Michigan', 'West Michigan'), ('Utah', 'Utah'), ('Tucson / Yuma', 'Tucson / Yuma'), ('New York City', 'New York City'), ('VT / NH / ME', 'VT / NH / ME'), ('Hawaii', 'Hawaii'), ('Northern Connecticut', 'Northern Connecticut'), ('Richmond', 'Richmond'), ('Western Pennsylvania', 'Western Pennsylvania'), ('Southern Virginia', 'Southern Virginia'), ('Memphis', 'Memphis'), ('Baltimore', 'Baltimore'), ('Southern Connecticut', 'Southern Connecticut'), ('Indianapolis', 'Indianapolis'), ('New Orleans', 'New Orleans'), ('Buffalo', 'Buffalo'), ('South West Florida', 'South West Florida'), ('North LA', 'North LA'), ('South Bay', 'South Bay'), ('West Virginia', 'West Virginia')], max_length=255)),
                ('Assignee', models.CharField(blank=True, default='', max_length=255)),
                ('eNB', models.CharField(blank=True, default='', max_length=255)),
                ('LSM', models.CharField(blank=True, default='', max_length=255)),
                ('SiteType', models.CharField(blank=True, default='', max_length=255)),
                ('Schedule_Name', models.CharField(blank=True, default='', max_length=255)),
                ('Fail', models.CharField(blank=True, default='', max_length=255)),
                ('Fail_Reason', models.CharField(blank=True, default='', max_length=255)),
                ('RTRV_SON_SO_status', models.CharField(blank=True, choices=[('\xa0121000;121000;66000;66000', '\xa0121000;121000;66000;66000'), ('121000;121000', '121000;121000'), ('66000;66000', '66000;66000'), ('NA', 'NA')], default='', max_length=255)),
                ('Ticket_Raised_For_Issue', models.CharField(blank=True, choices=[('PRTS', 'PRTS'), ('TRAMS', 'TRAMS'), ('NIMS', 'NIMS'), ('NEO', 'NEO'), ('PATROL', 'PATROL')], default='', max_length=255)),
                ('Ticket_no', models.CharField(blank=True, default='', max_length=255)),
                ('TVW_Available', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Yes but incomplete data', 'Yes but incomplete data')], default='', max_length=255)),
                ('TVW_Available_FMCC_Database', models.CharField(blank=True, choices=[('TVW Available in West Extract Database', 'TVW Available in West Extract Database'), ('Yes', 'Yes'), ('No', 'No'), ('Rural Roaming Site. TVW not required.', 'Rural Roaming Site. TVW not required.'), ('NA', 'NA')], default='', max_length=255)),
                ('Acd_Status', models.CharField(blank=True, choices=[('Task 3105 is Actualized', 'Task 3105 is Actualized'), ('ACD Accepted', 'ACD Accepted'), ('TVW Received from WEST', 'TVW Received from WEST'), ('Ready for drive test', 'Ready for drive test'), ('ACD Error', 'ACD Error'), ('ACD Rejected', 'ACD Rejected'), ('ACD Created', 'ACD Created'), ('ACD Sent', 'ACD Sent'), ('Blank', 'Blank'), ('Rural Roaming Site. ACD not required.', 'Rural Roaming Site. ACD not required.')], default='', max_length=255)),
                ('TVW_Related_Remarks', models.CharField(blank=True, choices=[('TVW Related Remarks', 'TVW Related Remarks'), ('informational only, no action required', 'informational only, no action required'), ('send completed ACD/TVW to West', 'send completed ACD/TVW to West'), ('Upload Complete TVW file to SV', 'Upload Complete TVW file to SV')], default='', max_length=255)),
                ('Other_Remarks', models.CharField(blank=True, default='', max_length=255)),
                ('SV_Actualization', models.CharField(blank=True, default='', max_length=255)),
                ('CSMS', models.CharField(blank=True, default='', max_length=255)),
                ('FE_Name', models.CharField(blank=True, default='', max_length=255)),
                ('Site_Status_pre_Activity', models.CharField(blank=True, choices=[('Lock', 'Lock'), ('Unlock', 'Unlock'), ('NA', 'N/A')], max_length=255)),
                ('Site_Status_post_Activity', models.CharField(blank=True, choices=[('Lock', 'Lock'), ('Unlock', 'Unlock'), ('NA', 'N/A')], max_length=255)),
                ('RET', models.CharField(blank=True, choices=[('Defined in LSM', 'Defined in LSM'), ('Defined in BSM', 'Defined in BSM'), ('NA', 'NA')], max_length=255)),
                ('OAR_Date', models.DateField(blank=True, null=True)),
                ('OAC_Date', models.DateField(blank=True, null=True)),
                ('Lock_Unlock_Verified_By', models.CharField(blank=True, default='', max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('admin', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ericssonrsaadmin', to=settings.AUTH_USER_MODEL)),
                ('ericrsa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ericssonrsa', to='ericsson.Ericsson_Count')),
            ],
        ),
    ]