import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import joblib
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("new_data.csv")

'''
# Dataframedeki virgulleri silme kodu
for i in df.columns:
	for j in range(0,len(df.index)):
		if(isinstance(df[i][j],str) == 1):
			df[i][j] = df[i][j].replace(',', '')
df.to_csv("data.csv")
'''

'''
labelenc = LabelEncoder()
df.genres = labelenc.fit_transform(df.genres)
df.to_csv("lEncodeddata.csv")
'''


df_pivot = df.pivot(index = "book_id", columns = "genres", values = "rating").fillna(0)

#print(df.head())
matrix = csr_matrix(df_pivot.values)

knn = joblib.load('knn.h5')

knn.fit(matrix)


#  sf 18
#  classic 0
#  philosophy 1
#  bio 9
#  yngadlt 3
#  travel 5
#  crime 6
#  science 24
#  horror 4
#  history 21
#  adventure 12
genre = 12   # BURAYA KULLANICININ GIRDIGI KITAP TURU (GENRE) GELECEK (INTEGER OLARAK)
query_index = genre
filter1 = df.genres == genre
ids = df.book_id.where(filter1)
for i in ids:
	if type(i) == float and pd.isna(i):
		pass
	else:
		query_index = int(i)

distances, indices = knn.kneighbors(df_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)
i = 0
print('{}-{}'.format(df.title[df.title.index[indices.flatten()[i]]] ,df.genres[df.title.index[indices.flatten()[i]]]))
