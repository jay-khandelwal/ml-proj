#import pickle

#pickle_in = open('iris.pkl','rb')
#clf = pickle.load(pickle_in)
#y = clf.predict({'sepal_len':[ 1.7], 'sepal_width': [8.5], 'petal_len': [4.5], 'petal_width':[6.1]})
#print(y)
#return HttpResponse('predicted class :' ,y)


import pickle 
import pandas as pd

pickle_in = open('iris.pkl', 'rb')
clf = pickle.load(pickle_in)


test_x = pd.DataFrame({'sepal length':[4.9], 'sepal width': [3.0],'petal length':[1.4], 'petal width':[0.2]})
predicted_y = clf.predict(test_x)

print('predicted_y :', predicted_y)
	