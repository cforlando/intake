# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-24 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0041_enforce_unique_slugs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationnote',
            options={'ordering': ['-created'], 'permissions': (('view_application_note', 'Can read the contents of notes from followups'),)},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='application',
            name='form_submission',
            field=models.ForeignKey(db_column='formsubmission_id', on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='intake.FormSubmission'),
        ),
        migrations.AlterField(
            model_name='application',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='user_accounts.Organization'),
        ),
        migrations.AlterField(
            model_name='nextstep',
            name='help_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='nextstep',
            name='template',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='statustype',
            name='help_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='statustype',
            name='template',
            field=models.TextField(blank=True),
        ),
    ]
