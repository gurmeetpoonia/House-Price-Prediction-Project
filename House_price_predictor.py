<<<<<<< HEAD
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error
import joblib
df=pd.read_csv("Housing.csv")
print(df.head())
print(df.info())
print(df.isnull())
print(df.isnull().sum())
df["mainroad"]=df["mainroad"].map({"yes":1,"no":0})
df["guestroom"]=df["guestroom"].map({"yes":1,"no":0})
df["hotwaterheating"]=df["hotwaterheating"].map({"yes":1,"no":0})
df["airconditioning"]=df["airconditioning"].map({"yes":1,"no":0})
df["basement"]=df["basement"].map({"yes":1,"no":0})
df["prefarea"]=df["prefarea"].map({"yes":1,"no":0})
df["furnishingstatus"]=df["furnishingstatus"].map({"unfurnished":0,"semi-furnished":1,"furnished":2})
#print(df.info())
X=df[["area","bedrooms","bathrooms","stories","parking","mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]]
y=df["price"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
#print(model.score(X_test, y_test))
#print(df.corr()["price"].sort_values(ascending=False))

#y_pred=model.predict(X_test)

#accurany=mean_absolute_error(y_test,y_pred)
#print(accurany)

joblib.dump(model,"house_price_model.pkl")
=======
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error
import joblib
df=pd.read_csv("Housing.csv")
print(df.head())
print(df.info())
print(df.isnull())
print(df.isnull().sum())
df["mainroad"]=df["mainroad"].map({"yes":1,"no":0})
df["guestroom"]=df["guestroom"].map({"yes":1,"no":0})
df["hotwaterheating"]=df["hotwaterheating"].map({"yes":1,"no":0})
df["airconditioning"]=df["airconditioning"].map({"yes":1,"no":0})
df["basement"]=df["basement"].map({"yes":1,"no":0})
df["prefarea"]=df["prefarea"].map({"yes":1,"no":0})
df["furnishingstatus"]=df["furnishingstatus"].map({"unfurnished":0,"semi-furnished":1,"furnished":2})
#print(df.info())
X=df[["area","bedrooms","bathrooms","stories","parking","mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]]
y=df["price"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
#print(model.score(X_test, y_test))
#print(df.corr()["price"].sort_values(ascending=False))

#y_pred=model.predict(X_test)

#accurany=mean_absolute_error(y_test,y_pred)
#print(accurany)

joblib.dump(model,"house_price_model.pkl")
>>>>>>> f545ffe56256d4c4150ce4bebb018672f51d0e2c
print("model successfully saved") 