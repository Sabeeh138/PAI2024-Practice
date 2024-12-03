import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

df = pd.read_csv("heart.csv")
df['ExerciseAngina'] = df.ExerciseAngina.replace({'N': 0, 'Y': 1})
df['RestingECG'] = df.RestingECG.replace({'Normal': 1, 'ST': 2, 'LVH': 3})
df['ST_Slope'] = df.ST_Slope.replace({'Down': 1, 'Flat': 2, 'Up': 3})
print(df.head())

df.drop("Sex", axis=1, inplace=True)
df.drop("ChestPainType", axis=1, inplace=True)
X = df.drop("HeartDisease", axis=1)

Y = df.HeartDisease

print(df.apply(lambda col: col.unique()))


scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X_Scaled, Y, test_size=0.3, random_state=42)
model = KNeighborsClassifier()

model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))

pca = PCA(0.90)
X_pca = pca.fit_transform(X_Scaled)

X_train_pca, X_test_pca, Y_train, Y_test = train_test_split(X_pca, Y, test_size=0.3, random_state=42)
model2 = KNeighborsClassifier()

model2.fit(X_train_pca, Y_train)
print(model2.score(X_test_pca, Y_test))
