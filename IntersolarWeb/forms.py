from django import forms

class DateForm(forms.Form):
    Date_from = forms.CharField(label='From', max_length=100)
    Date_to = forms.CharField(label='To', max_length=100)
    CHOICES= (('1','Thermal'),('2','Electrical'),)
    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    #Measurement = forms.CharField(label='Meas', max_length=100)
# your_name = forms.DateField(
#        widget=forms.DateInput(format=('%d-%m-%Y'), 
#                               attrs={'class':'myDateClass', 
#                               'placeholder':'Select a date'}))
#class MyForm(forms.Form):    
#    CHOICES= (('1','ME'),('2','YOU'),('3','WE'),)
#    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
#    
#    							<select id="measurement_setup" name="measurement_setup" placeholder="large-4.columns">
#								<option value="1">Electrical</option><option value="2">Thermal</option> </select>