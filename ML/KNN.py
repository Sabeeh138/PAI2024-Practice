import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = sns.load_dataset('iris')
print(df)
X = df.drop("species", axis=1)
Y = df.species

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
model = KNeighborsClassifier()
model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))
