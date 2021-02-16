from django import forms

class mlform(forms.Form):
	
	sepal_len = forms.FloatField()
	sepal_width = forms.FloatField()
	petal_len = forms.FloatField()
	petal_width = forms.FloatField()
	
#['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary', 'Germany', 'Spain', 'Male']
	
class svm(forms.Form):
	CreditScore =forms.FloatField()
	Age = forms.IntegerField()
	Tenure =forms.IntegerField()
	Balance =forms.FloatField()
	NumOfProducts =forms.IntegerField()
	HasCrCard =forms.IntegerField()
	IsActiveMember =forms.IntegerField()
	EstimatedSalary =forms.FloatField()
	Germany =forms.IntegerField()
	Spain =forms.IntegerField()
	Male =forms.IntegerField()
	
	