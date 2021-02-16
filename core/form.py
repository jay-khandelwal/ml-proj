from django import forms

class mlform(forms.Form):
	
	sepal_len = forms.FloatField()
	sepal_width = forms.FloatField()
	petal_len = forms.FloatField()
	petal_width = forms.FloatField()
	
	
	
	
	