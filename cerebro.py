import pandas as pd
file ='weather_test.csv'
df_test = pd.read_csv(file)
y= df_test.iloc[:,-1:]
df_test_features =[ 
       'Global CMP22 (vent/cor) [W/m^2]','Direct sNIP [W/m^2]','Azimuth Angle [degrees]', 'Tower Dry Bulb Temp [deg C]',
       'Tower Wet Bulb Temp [deg C]', 'Tower Dew Point Temp [deg C]',
       'Tower RH [%]', 'Peak Wind Speed @ 6ft [m/s]',
       'Avg Wind Direction @ 6ft [deg from N]', 'Station Pressure [mBar]',
       'Precipitation (Accumulated) [mm]', 'Moisture', 'Albedo (CMP11)',
        'Solar Zenith Angle']
X = df_test[df_test_features]
X.describe()
X.head(2999)


from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
train_X, valid_X, train_y, valid_y = train_test_split(X, y,train_size=0.6, test_size=0.4, random_state = 2)
from sklearn.impute import SimpleImputer

# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(train_X))
imputed_X_valid = pd.DataFrame(my_imputer.transform(valid_X))

# Imputation removed column names; put them back
imputed_X_train.columns = train_X.columns
imputed_X_valid.columns = valid_X.columns

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X_scaled = sc_X.fit_transform(imputed_X_train)
y_scaled = sc_y.fit_transform(train_y)
from sklearn.svm import SVR
df= SVR(kernel = 'rbf', gamma = 'scale')
df.fit(X_scaled, y_scaled.ravel())
val_predictions = df.predict(valid_X)
print(mean_absolute_error(valid_y, val_predictions))
df = pd.DataFrame(df.predict(X.head(2999)),columns=["Snow Depth [cm]"])
df.head(2999)
