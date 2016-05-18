# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20160330_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualite',
            name='categorie',
            field=models.CharField(choices=[('P', 'Politique'), ('S', 'Societe'), ('E', 'Economie'), ('C', 'Culture'), ('O', 'Sport'), ('I', 'Interview'), ('N', 'En image'), ('L', 'Lu pour vous')], max_length=3),
        ),
    ]
