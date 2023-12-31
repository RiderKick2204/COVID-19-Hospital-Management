from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_patient_symptoms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Fever', 'Fever'), ('Dry cough', 'Dry cough'), ('Tiredness', 'Tiredness'), ('Aches and pains', 'Aches and pains'), ('Sore throat', 'Sore throat'), ('Diarrhoea', 'Diarrhoea'), ('Loss of taste or smell', 'Loss of taste or smell'), ('Difficulty in breathing or shortness of breath', 'Difficulty in breathing or shortness of breath'), ('Chest pain or pressure', 'Chest pain or pressure'), ('Loss of speech or movement', 'Loss of speech or movement')], max_length=183, null=True),
        ),
    ]
