# Generated by Django 3.1.3 on 2020-12-14 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professeur',
            name='matiére',
        ),
        migrations.RemoveField(
            model_name='présence',
            name='combien_du_heure',
        ),
        migrations.RemoveField(
            model_name='présence',
            name='heure',
        ),
        migrations.RemoveField(
            model_name='présence',
            name='marqué_la_présence',
        ),
        migrations.RemoveField(
            model_name='présence',
            name='matiére',
        ),
        migrations.RemoveField(
            model_name='présence',
            name='professeur_qui_a_approuvé',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='matiére',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='professeur',
        ),
        migrations.RemoveField(
            model_name='corrigé',
            name='professeur',
        ),
        migrations.RemoveField(
            model_name='cour',
            name='professeur',
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='professeur',
        ),
        migrations.RemoveField(
            model_name='live_ended',
            name='professeur',
        ),
        migrations.AddField(
            model_name='classe',
            name='type_of_language',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='corrigé',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cour',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exercice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='live_ended',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='live_ended',
            name='matiére',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='emploi',
        ),
        migrations.DeleteModel(
            name='heure',
        ),
        migrations.DeleteModel(
            name='Matiére',
        ),
        migrations.DeleteModel(
            name='Professeur',
        ),
        migrations.DeleteModel(
            name='Présence',
        ),
    ]
