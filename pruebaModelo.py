import joblib
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

var = [ 200, 6, 3, 0, 4, 1478, 0, 0, 0, 0, 0, 0, 0]
loaded_rf = joblib.load("my_forest_regression.joblib")
resul = loaded_rf.predict([var])
print(resul)
