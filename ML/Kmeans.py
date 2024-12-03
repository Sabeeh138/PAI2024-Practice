import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = sns.load_dataset('iris')
print(df)
num_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
sns.scatterplot(data=df, x="sepal_length", y="petal_length")
plt.show()
X = df[num_cols]
print(X)
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)
print(model.cluster_centers_)

predictions = model.predict(X)
print(predictions)

sns.scatterplot(data=X, x="sepal_length", y="petal_length", hue=predictions)
centers_x, centers_y = model.cluster_centers_[:,0], model.cluster_centers_[:,1]
plt.plot(centers_x, centers_y, "xb")
plt.show()
print(model.inertia_)




my_range = range(1, 15)
inertia = []
for n_clusters in my_range:
  my_model = KMeans(n_clusters, random_state=42).fit(X)
  pred = my_model.predict(X)
  inertia.append(my_model.inertia_)
  

plt.plot(my_range, inertia, marker="o")
plt.xlabel("No of Clusters")
plt.ylabel("Inertia")
plt.show()



model2 = KMeans(n_clusters=8, random_state=42).fit(X)
preds = model2.predict(X)
sns.scatterplot(data=X, x="sepal_length", y="petal_length", hue=preds)
plt.show()
print(model2.inertia_)
