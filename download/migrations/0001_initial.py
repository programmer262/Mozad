# Generated by Django 3.1.1 on 2020-11-01 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emploi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=2000)),
                ('téléphone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='heure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Matiére',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiére', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('matiére', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.matiére')),
            ],
        ),
        migrations.CreateModel(
            name='Présence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('les_éléves_qui_vont_étre_marqué', models.CharField(max_length=20)),
                ('présence', models.BooleanField(blank=True, default=True, null=True)),
                ('date', models.CharField(max_length=200)),
                ('combien_du_heure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.emploi')),
                ('heure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.heure')),
                ('marqué_la_présence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.etudiant')),
                ('matiére', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.matiére')),
                ('professeur_qui_a_approuvé', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Live_ended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cour', models.CharField(max_length=100)),
                ('partie', models.CharField(max_length=100)),
                ('live', models.FileField(upload_to='')),
                ('matiére', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.matiére')),
                ('professeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
                ('exercice', models.CharField(max_length=200)),
                ('professeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
                ('cour', models.CharField(max_length=200)),
                ('partie', models.CharField(max_length=200)),
                ('professeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Corrigé',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
                ('correction_name', models.CharField(max_length=200)),
                ('professeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien', models.CharField(max_length=2000)),
                ('date', models.CharField(max_length=200)),
                ('heure', models.CharField(max_length=200)),
                ('matiére', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.matiére')),
                ('professeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.professeur')),
            ],
        ),
    ]
