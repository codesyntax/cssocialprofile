from django import forms
from django.contrib.auth.models import User
from cssocialprofile.models import CSSocialProfile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = CSSocialProfile
        fields = ('fullname','bio',)
        
class ProfilePhotoForm(forms.Form):
    """ """
    argazkia  = forms.ImageField(label='Zure argazkia',help_text='Sartu zeu agertzen zaren argazki bat, mesedez. Onartutako formatuak: jpg, png, gif.')
    
    def clean_argazkia(self):
        """ """
        argazkia = self.cleaned_data['argazkia']
        name = argazkia.name
        try:
            name.encode('ascii')
        except:
            raise forms.ValidationError(u'Argazkiaren izenak (%s) karaktere arraroren bat du eta errorea ematen du. Aldatu argazkiari izena, mesedez!' % name)            

        format = name.split('.')[-1]
        if format.lower().strip()==u'bmp':
            raise forms.ValidationError(u'Argazkiaren formatua ez da egokia. Ez dugu BMP fitxategirik onartzen. Aldatu formatua, mesedez!')        
         