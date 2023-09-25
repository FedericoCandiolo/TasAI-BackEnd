import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv (r'total.csv', encoding= 'unicode_escape', low_memory=False)
df = pd.DataFrame(data)

#for i in df:
#  print(i)

table = pd.DataFrame()
table[['metros', 'ambientes', 'banio', 'cochera', 'dormitorios', 'ciudad', 'precioxLocalidad', 'parrilla', 'patio',
         'lavadero', 'toilette', 'A/C', 'balcon', 'pileta', 'precio']] = df[ ['metros', 'ambientes', 'banio', 'cochera',
        'dormitorios', 'ciudad', 'precioxLocalidad', 'parrilla', 'patio', 'lavadero', 'toilette', 'A/C', 'balcon', 'pileta', 'precio']]

table = table.fillna(0)

table = table.astype({'metros': 'int', 'ambientes': 'int', 'banio': 'int', 'cochera': 'int', 'dormitorios': 'int',
                        'precioxLocalidad': 'int', 'parrilla': 'int', 'patio': 'int', 'lavadero': 'int', 'toilette': 'int',
                        'A/C': 'int', 'balcon': 'int', 'pileta': 'int', 'precio': 'int'})

#print(table)

X = table[['metros', 'ambientes', 'banio', 'cochera', 'dormitorios', 'precioxLocalidad', 'parrilla', 'patio', 'lavadero',
           'toilette', 'A/C', 'balcon', 'pileta',]]
y = table['precio']

regr = linear_model.LinearRegression()
regr.fit(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

forest = RandomForestRegressor()
forest.fit(X_train_scaled, y_train)
print("Score: " + str(forest.score(X_test_scaled, y_test)))

y_pred = forest.predict(X_test_scaled)

var = [ 200, 6, 3, 0, 4, 1478, 0, 0, 0, 0, 0, 0, 0]
resul = forest.predict([var])

print("Result: " + str(resul))

joblib.dump(forest, "my_forest_regression.joblib")
