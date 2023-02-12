import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score

''' Визуализация метрик кластеризации  для разбиения на кластеры от 2 до 9:

          - inertia: коэфициент "инерции";
          
          - silhouette: коэффициент "силуэта";
          
          - calinski_harabasz: коэфициент Калински-Харабаса;
          
          - davis_bouldin: коэффициент Дэвиса-Болдина
'''
def plot_metrics(df):
    
    inertia = []
    silhouette = []
    calinski_harabasz = []
    davis_bouldin = []
    
    for n_clusters in range(2, 9):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(df)
    
        inertia.append(kmeans.inertia_)
        silhouette.append(silhouette_score(df, kmeans.labels_))
        calinski_harabasz.append(calinski_harabasz_score(df, kmeans.labels_))
        davis_bouldin.append(davies_bouldin_score(df, kmeans.labels_))
        
    fig, ax = plt.subplots(1, 4, figsize=(24,5))
    
    ax[0].plot(range(2, 9), inertia, 's-', label='inertia')
    ax[1].plot(range(2, 9), silhouette, 's-', label='silhouette')
    ax[2].plot(range(2, 9), calinski_harabasz, 's-', label='calinski-harabasz')
    ax[3].plot(range(2, 9), davis_bouldin, 's-', label='davis-bouldin')
    ax[0].legend(prop={'size': 16})
    ax[1].legend(prop={'size': 16})
    ax[2].legend(prop={'size': 16})
    ax[3].legend(prop={'size': 16});
    fig.supxlabel('n clusters')

def plot_coef(df, labels, flag=True,):
  
    # визуализация проекции признакового пространства  на плоскость  
    tsne = TSNE(n_components=2, perplexity=50, init='pca',
                learning_rate='auto', random_state=42)
    df_tsne = pd.DataFrame(tsne.fit_transform(df))
    df_tsne['Кластер'] = labels
    fig = plt.figure()
    sns.scatterplot(x=df_tsne[0],
                  y=df_tsne[1],
                  hue=df_tsne['Кластер'],
                  palette='bright')
    fig.suptitle('Визуализация проекции признакового пространства  на плоскость', fontsize=14);
  
    score_list=[]
    
    silhouette = silhouette_score(df, labels)  
    calinski_harabasz = calinski_harabasz_score(df, labels)  
    davies_bouldin = davies_bouldin_score(df, labels)
    
    if flag == True:
        print('Коэфициент силуэта: %.3f' % silhouette)
        print('Коэфициент Калински-Харабаса: %.3f' % calinski_harabasz)
        print('Коэфициент Дэвиса-Болдина: %.3f' % davies_bouldin)
    
    


silhouette=[] # список коэффициентов "силуэта" моделей
calinski_harabasz=[] # список коэффициентов Калински-Харабаса моделей
davies_bouldin=[] # список коэффициентов Дэвиса_Болдина моделей

def make_metrics_tabl(df,labels):    
    coef_silhouette = silhouette_score(df, labels)  
    coef_calinski_harabasz = calinski_harabasz_score(df, labels)  
    coef_davies_bouldin = davies_bouldin_score(df, labels)
    
    silhouette.append(coef_silhouette)
    calinski_harabasz.append(coef_calinski_harabasz)
    davies_bouldin.append(coef_davies_bouldin)
    
    
    
    
    
    
