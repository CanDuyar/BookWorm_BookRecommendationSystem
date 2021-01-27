import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import joblib
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/home/canberk/Desktop/data.csv")

'''
# Dataframedeki virgulleri silme kodu
for i in df.columns:
	for j in range(0,len(df.index)):
		if(isinstance(df[i][j],str) == 1):
			df[i][j] = df[i][j].replace(',', '')
df.to_csv("data.csv")
'''

# print(df.Genres)

'''
labelenc = LabelEncoder()
df.Genres = labelenc.fit_transform(df.Genres)
df.to_csv("data.csv")
'''

df_pivot = df.pivot(index="index", columns="Genres", values="rating").fillna(0)

# print(df.head())
matrix = csr_matrix(df_pivot.values)

knn = joblib.load('knn.h5')

# knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
knn.fit(matrix)
joblib.dump(knn, 'knn.h5')

query_index = np.random.choice(df_pivot.shape[0])
distances, indices = knn.kneighbors(df_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors=6)

for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {}:\n'.format(df.title[df.title.index[query_index]]))
    else:
        print('{}: {}'.format(i, df.title[df.title.index[indices.flatten()[i]]]))
