from numpy import mean, std, shape
from sklearn.decomposition import TruncatedSVD
from gensim.utils import simple_preprocess
from pandas import read_csv, DataFrame
from glove import Corpus
from networkx import (
    Graph, 
    average_clustering,
    average_shortest_path_length,
)

def feature_extract(path_dataset):
    feature_extract_dataset = []
    speeches = read_csv(path_dataset, sep="|")
    speeches['Classe'] = speeches['Classe'].replace(
        1, 1)
    #Falas mistas de Estamira e sua Família
    speeches['Classe'] = speeches['Classe'].replace(
        0, -1)

    # Para cada fala 
    for indice, fala in enumerate(speeches.Fala):
        #inicialização do método para pegar co-ocorrência
        dataset = Corpus()
        grafo = Graph()
        lsa = TruncatedSVD(n_components=1)
        
        tolkenizado = [simple_preprocess(str(fala), deacc=True)]

        quantas_palavras = shape(tolkenizado)[1]

        dataset.fit(tolkenizado, window=79)


        graph = Graph(dataset.matrix)
        values_lsa = lsa.fit_transform(dataset.matrix) 

        values_mean = mean(values_lsa,axis=0)
        values_std = std(values_lsa, axis=0)

        feature_extract_dataset.append([average_clustering(G=graph), 
                  average_shortest_path_length(G=graph),
                  speeches.comprimento[indice], 
                  values_mean.item(), 
                  values_std.item(), 
                  quantas_palavras])

    return DataFrame(feature_extract_dataset), speeches['Classe'].values