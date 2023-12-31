from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_patient_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.CharField(max_length=50)),
                ('occupied', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_relative_contact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_relative_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bed_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bed'),
        ),
    ]
