# Generated by Django 2.1.1 on 2018-12-04 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadFollowupHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followup_date', models.DateTimeField(auto_created=True)),
                ('activity', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(null=True)),
                ('next_activity_date', models.DateTimeField(null=True)),
                ('followup_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeadMaster',
            fields=[
                ('lead_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lead_title', models.CharField(max_length=500, null=True)),
                ('lead_description', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('official_email', models.EmailField(max_length=254, null=True)),
                ('official_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.URLField(null=True)),
                ('address_line1', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=250, null=True)),
                ('address_city', models.CharField(blank=True, max_length=200, null=True)),
                ('address_state', models.CharField(blank=True, max_length=50, null=True)),
                ('address_country', models.CharField(blank=True, max_length=50, null=True)),
                ('address_zip', models.CharField(blank=True, max_length=20, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('privacy', models.CharField(blank=True, max_length=250, null=True)),
                ('custom_fields', models.CharField(blank=True, max_length=250, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('product', models.CharField(blank=True, max_length=250, null=True)),
                ('value', models.DecimalField(decimal_places=3, default=0, max_digits=30, null=True)),
                ('created_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_owner', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='leadfollowuphistory',
            name='lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_master', to='DjangoClassicLeads.LeadMaster'),
        ),
    ]