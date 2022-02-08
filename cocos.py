import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Binary response for presence of 2c4a gene in DNA sequence
def CAPresence(dnaSequence):
	CALocation = dnaSequence.find('2c4a')
	if CALocation != -1:
		return 1
	else:
		return 0

#Binary response for presence of 3d2b gene in DNA sequence
def DBPresence(dnaSequence):
	DBLocation = dnaSequence.find('3d2b')
	if DBLocation != -1:
		return 1
	else:
		return 0

#Binary response for presence of of both genes in row
def Interaction(CABinary, DBBinary):
	if CABinary == 1 and DBBinary == 1:
		return 1
	else:
		return 0

#reads text file, converts json data into pandas dataframe
f = open('test_data.json.txt', 'r')
readfile = f.read()
jsonlines = [json.loads(jsonline) for jsonline in readfile.splitlines()]
f.close()
chocco_df = pd.read_json(json.dumps(jsonlines))

#creates 3 additional columns in pandas for presence of each gene and interaction
chocco_df['2c4a Present'] = chocco_df.apply(lambda row : CAPresence(row['gene_sequence']), axis = 1)
chocco_df['3d2b Present'] = chocco_df.apply(lambda row : DBPresence(row['gene_sequence']), axis = 1)
chocco_df['Interaction'] = chocco_df.apply(lambda row : Interaction(row['2c4a Present'], row['3d2b Present']), axis = 1)

#converts the data into a usable format for linear regression model
x = []
y = []
def createXandY(CABinary, DBBinary, Interaction, chocProduction):
	x.append([CABinary, DBBinary, Interaction])
	y.append(chocProduction)
chocco_df.apply(lambda row : createXandY(row['2c4a Present'], row['3d2b Present'], row['Interaction'], row['chocolate_production']), axis = 1)

#creates a model to predict chocolate production based on presence of each gene and interaction
model = LinearRegression().fit(x,y)

#print(chocco_df.head())
#print(chocco_df.tail())

#prediction of chocolate production for different realistic scenarios
#x_new = [[0,0,0],[1,0,0],[0,1,0],[1,1,1]]
#print(model.predict(x_new))
#magnitude of effects for the 3 gene attributes
#print(model.coef_)
#print(model.intercept_)


#A more informational linear regression model than the one implemented above
import statsmodels.api as sm
#Add a constant column
X = sm.add_constant(x)
#create Linear Regression model
est = sm.OLS(y,X).fit()
print(est.summary())


import matplotlib.pyplot as plt
#create histogram of chocolate production
plt.hist(chocco_df['chocolate_production'].tolist(), bins=20)
#bar chart of gene distribution among CoCos
numberOf2c4a = len([x for x in chocco_df['2c4a Present'].tolist() if x==1])
numberOf3d2b = len([x for x in chocco_df['3d2b Present'].tolist() if x==1])
data = {'Neither Gene': len(chocco_df['Interaction'].tolist())-(numberOf3d2b+numberOf2c4a), '2c4a Gene': numberOf2c4a, '3d2b Gene': numberOf3d2b, 'Both Genes': len([x for x in chocco_df['Interaction'].tolist() if x==1])}
names = list(data.keys())
values = list(data.values())
plt.bar(names, values)
plt.show()



#Bonus

#New cocos DF of only cocos with both genes
elite_coco_df = chocco_df[(chocco_df['Interaction']==1)]
#IDs of best cocos
elite_coco_IDs = elite_coco_df['coco_id'].tolist()
#Months to produce flock of 10000 if doubling every 6 months
time_to_produce_flock = 6 * np.log2([(10000/len(elite_coco_IDs))])[0]
#Chocolate production in grams per day when a full flock
chocco_production = str(elite_coco_df['chocolate_production'].mean(axis = 0) * 10000) + ' grams per day'
print(len(elite_coco_IDs), time_to_produce_flock)
print(chocco_production)
print(elite_coco_IDs)
print(elite_coco_df['chocolate_production'].mean(axis = 0))

