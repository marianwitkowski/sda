from django import forms
from .models import *

# nasz własny formularz bez podpięcia do modelu
class FindFlatForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)

    price_min = forms.IntegerField(required=False, help_text="Cena min.")
    price_max = forms.IntegerField(required=False, help_text="Cena max.")

    area_min = forms.FloatField(required=False)
    area_max = forms.FloatField(required=False)

    #district = forms.CharField(required=False, max_length=40)
    district = forms.ChoiceField(required=False, choices=[])

    def __init__(self, *args, **kwargs):
        super(FindFlatForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Podaj frazę"
        self.fields['district'].choices = \
        [("","---------")] + list(Flat.objects.all().order_by('district').\
            values_list("district","district").distinct())

    def clean(self):
        cleaned_data = super(FindFlatForm, self).clean()
        title = cleaned_data.get('title')
        price_min = cleaned_data.get('price_min')
        price_max = cleaned_data.get('price_max')
        area_min = cleaned_data.get('area_min')
        area_max = cleaned_data.get('area_max')
        district = cleaned_data.get('district')

        if not title and not price_min and not price_max \
            and not area_min and not area_max \
            and not district:
            raise forms.ValidationError("Podaj przynajmniej jeden warunek")

        if (price_min and price_min<0) or (price_max and price_max<0):
            raise forms.ValidationError("Niepoprawne wartości cen")

