from django.db import migrations

def add_indian_states(apps, schema_editor):
    State = apps.get_model('Profile_app', 'State')
    Country = apps.get_model('Profile_app', 'Country')

    try:
        india = Country.objects.get(id=1)  # Or use country_name="INDIA" if safer
    except Country.DoesNotExist:
        return  # Skip if country doesn't exist

    state_data = [
        {"state_name": "Andhra Pradesh", "state_code": "AP", "iso_code": "IN-AP"},
        {"state_name": "Arunachal Pradesh", "state_code": "AR", "iso_code": "IN-AR"},
        {"state_name": "Assam", "state_code": "AS", "iso_code": "IN-AS"},
        {"state_name": "Bihar", "state_code": "BR", "iso_code": "IN-BR"},
        {"state_name": "Chhattisgarh", "state_code": "CT", "iso_code": "IN-CT"},
        {"state_name": "Goa", "state_code": "GA", "iso_code": "IN-GA"},
        {"state_name": "Gujarat", "state_code": "GJ", "iso_code": "IN-GJ"},
        {"state_name": "Haryana", "state_code": "HR", "iso_code": "IN-HR"},
        {"state_name": "Himachal Pradesh", "state_code": "HP", "iso_code": "IN-HP"},
        {"state_name": "Jharkhand", "state_code": "JH", "iso_code": "IN-JH"},
        {"state_name": "Karnataka", "state_code": "KA", "iso_code": "IN-KA"},
        {"state_name": "Kerala", "state_code": "KL", "iso_code": "IN-KL"},
        {"state_name": "Madhya Pradesh", "state_code": "MP", "iso_code": "IN-MP"},
        {"state_name": "Maharashtra", "state_code": "MH", "iso_code": "IN-MH"},
        {"state_name": "Manipur", "state_code": "MN", "iso_code": "IN-MN"},
        {"state_name": "Meghalaya", "state_code": "ML", "iso_code": "IN-ML"},
        {"state_name": "Mizoram", "state_code": "MZ", "iso_code": "IN-MZ"},
        {"state_name": "Nagaland", "state_code": "NL", "iso_code": "IN-NL"},
        {"state_name": "Odisha", "state_code": "OR", "iso_code": "IN-OR"},
        {"state_name": "Punjab", "state_code": "PB", "iso_code": "IN-PB"},
        {"state_name": "Rajasthan", "state_code": "RJ", "iso_code": "IN-RJ"},
        {"state_name": "Sikkim", "state_code": "SK", "iso_code": "IN-SK"},
        {"state_name": "Tamil Nadu", "state_code": "TN", "iso_code": "IN-TN"},
        {"state_name": "Telangana", "state_code": "TG", "iso_code": "IN-TG"},
        {"state_name": "Tripura", "state_code": "TR", "iso_code": "IN-TR"},
        {"state_name": "Uttarakhand", "state_code": "UT", "iso_code": "IN-UT"},
        {"state_name": "Uttar Pradesh", "state_code": "UP", "iso_code": "IN-UP"},
        {"state_name": "West Bengal", "state_code": "WB", "iso_code": "IN-WB"},
    ]

    for state in state_data:
        State.objects.update_or_create(
            iso_code=state["iso_code"],
            defaults={
                "state_name": state["state_name"],
                "state_code": state["state_code"],
                "country": india
            }
        )

class Migration(migrations.Migration):

    dependencies = [
        ('Profile_app', '0007_alter_communication_primary_phone_and_more'),
    ]

    operations = [
        migrations.RunPython(add_indian_states),
    ]
