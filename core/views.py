from django.shortcuts import render, HttpResponse
import pickle
from .forms import mlform,svm

# Create your views here.

def index(request):
	
	if request.method == 'POST':
		form = mlform(request.POST)
		if form.is_valid():
			sepal_len = form.cleaned_data['sepal_len']
			sepal_width = form.cleaned_data['sepal_width']
			petal_len = form.cleaned_data['petal_len']
			petal_width = form.cleaned_data['petal_width']
			
			pickle_in = open('iris.pkl','rb')
			clf = pickle.load(pickle_in)
			
			import pandas as pd
			test_x = pd.DataFrame({'sepal_len':[ sepal_len], 'sepal_width': [sepal_width], 'petal_len': [petal_len], 'petal_width':[petal_width]})
			
			predicted_y = int(clf.predict(test_x))
			list = ['Setosa', 'Versicolor', 'Verginica']
			context =( 'Type of leave :', list[predicted_y])
			return HttpResponse(context)
		
	else:
		form = mlform()			
		context= {'form':form}	
		return render(request, 'index.html', context)
		
#['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary', 'Germany', 'Spain', 'Male']
		
def churn(request):
	if request.method == 'POST':
		form = svm(request.POST)
		if form.is_valid():
			CreditScore = form.cleaned_data['CreditScore']
			Age = form.cleaned_data['Age']
			Tenure = form.cleaned_data['Tenure']
			Balance = form.cleaned_data['Balance']
			NumOfProducts = form.cleaned_data['NumOfProducts']
			HasCrCard = form.cleaned_data['HasCrCard']
			IsActiveMember = form.cleaned_data['IsActiveMember']
			EstimatedSalary = form.cleaned_data['EstimatedSalary']
			Germany = form.cleaned_data['Germany']
			Spain = form.cleaned_data['Spain']
			Male = form.cleaned_data['Male']
			
			pickle_in = open('SupportVectorMachineScaler.pkl','rb')
			scaler = pickle.load(pickle_in)
			import pandas as pd
			test_x = pd.DataFrame({
			'CreditScore':[ CreditScore],
			 'Age': [Age],
			 'Tenure': [Tenure], 
			'Balance':[Balance],
			 'Spain':[NumOfProducts],
			  'HasCrCard':[HasCrCard],
			   'IsActiveMember':[IsActiveMember],
			    'EstimatedSalary':[EstimatedSalary],
			     'Germany':[Germany],
			      'Spain':[Spain],
			       'Male':[Male]})
			print('main :',test_x)    
#			test_x = scaler.transform(test_x)
			print('*' *100)
			print('Scaler :',test_x)    
			pickle_in = open('SupportVectorMachine accuracy.pkl','rb')
			clf = pickle.load(pickle_in)
			
			#import pandas as pd
#			test_x = pd.DataFrame({'sepal_len':[ sepal_len], 'sepal_width': [sepal_width], 'petal_len': [petal_len], 'petal_width':[petal_width]})
			
			predicted_y = clf.predict(test_x)
#			list = ['Yes', 'No']
#			context =( 'did person leave ?? :', list[predicted_y])
			return HttpResponse(predicted_y)
		
	else:
		form = svm()			
		context= {'form':form}	
		return render(request, 'index.html', context)