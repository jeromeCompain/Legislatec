# -*- coding: utf-8 -*-
import re
import matplotlib.pyplot as plt
from pyspark.sql import *
from pyspark.ml.feature import PCA
from pyspark.mllib.linalg import Vectors

# On charge le fichier iris.data
irisFile = sc.textFile("file:///home/cloudera/iris.data")

# On traite les données
# pour obtenir une liste d'exemples exploitable.
irisRDD = irisFile.map(lambda line: re.split(',', line))
iris = irisRDD.collect()

# Séparons les exemples pour avoir les données d'un côté et
# les labels de l'autre
irisData, irisLabels = [x[0:3] for x in iris], [x[-1] for x in iris]

# On formate les données pour qu'elle soient au format
# requis par la fonction PCA
irisData = ([(Vectors.dense([float(el) for el in line]),) for line in irisData[0:-1]])


# On effectue la PCA comme dans l'exemple de la doc spark
# https://spark.apache.org/docs/1.6.1/api/python/pyspark.ml.html#pyspark.ml.feature.PCA
df = sqlContext.createDataFrame(irisData, ["features"])
pca = PCA(k=2, inputCol="features", outputCol="pcaFeatures")
model = pca.fit(df)
result = model.transform(df).select("pcaFeatures")
result.show(truncate=False)

# La PCA nous donne une liste de couple de variables
# On veut deux listes X et Y correspondant à des coordonnées pour les ploter
res = result.collect()
xValue = []
yValue = []
for tup in res:
    xValue.append(tup.pcaFeatures[0])
    yValue.append(tup.pcaFeatures[1])

# Plot les données 
#(il y a trois classes et chacune contient 50 elements)

plt.xlabel('x')
plt.ylabel('y')
plt.title('iris PCA')

plt.plot(xValue[0:50],yValue[0:50],'b.')
plt.plot(xValue[50:100],yValue[50:100],'r.')
plt.plot(xValue[100:150],yValue[100:150],'g.')

plt.show()
