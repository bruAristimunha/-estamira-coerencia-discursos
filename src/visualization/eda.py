from collections import Counter
from numpy import isin
from pandas import read_csv, DataFrame
from matplotlib.pylab import subplots, tight_layout, savefig
from seaborn import swarmplot, boxplot

from nltk.tokenize import TweetTokenizer
from wordcloud import WordCloud

def filter_list(lista, filter_item):
    """ Function to remove punctuation from the legends."""
    return [item.lower() for item in lista if ~isin(item, filter_item)]

def counter_words(speeches):
    """ Function for counting words on the dataframe."""
    tokenizer = TweetTokenizer()
    tokens = speeches["Fala"].map(tokenizer.tokenize).sum()
    punctuation = [",", ".", "?", "!", "\"", "-", ":"]
    counter = Counter(filter_list(tokens, punctuation))
    return counter

def wordcloud(counter, axes):
    """Encapsulador da biblioteca Wordcloud para matplot
    adaptado de: 
    https://medium.com/@datanizing/modern-text-mining-with-python-part-2-of-5-data-exploration-with-pandas-ee3456cf6a4
    """
    word_cloud = WordCloud(background_color="white", max_words=50)
    word_cloud.generate_from_frequencies(counter)
   
    axes.imshow(word_cloud, interpolation="bilinear")
    axes.axis("off")
    tight_layout(pad=1.0)
    
    return axes

def eda(path_dataset, path_save):

    speeches = read_csv(path_dataset, sep="|")
    fig, axes = subplots(nrows=2, ncols=2, figsize=(20, 10))

    #Falas de Estamira
    speeches['Classe'] = speeches['Classe'].replace(
        1, "Estamira")

    #Falas mistas de Estamira e sua Família
    speeches['Classe'] = speeches['Classe'].replace(
        0, "Família de Estamira")

    #Falas da Família
    speeches['Classe'] = speeches['Classe'].replace(
        -1, "Família de Estamira")

    for ind, speech in speeches.groupby("Classe"):
        speech.hist(ax=axes[0][0], column="comprimento", alpha=0.5)

    axes[0][0].set_ylabel("Quantidade de caracteres nas falas.")
    axes[0][0].set_xlabel("Comprimento das falas.")
    axes[0][0].set_title("Histograma com comprimento das falas.")
    axes[0][0].legend(
        ['Falas de Estamira', 'Falas da Família\ncom e sem Estamira'])

    swarmplot(x='Classe', y='comprimento', data=speeches, 
              orient="v", color=".25", ax=axes[0][1])
    boxplot(x='Classe', y='comprimento', data=speeches, 
            orient="v", ax=axes[0][1])

    axes[0][1].set_ylabel("Quantidade de caracteres nas falas.")
    axes[0][1].set_xlabel("Comprimento das falas.")
    axes[0][1].set_title("Diagrama de Caixa com comprimento das falas.")

    for ind, (rotulo, speech) in enumerate(speeches.groupby("Classe")):
        counter = counter_words(speech)
        wordcloud(counter, axes[1][ind])
        axes[1][ind].set_title("Nuvem de palavras da {}".format(rotulo))
        
    savefig("{}/exploratory_data_analysis.pdf".format(path_save), 
            bbox_inches="tight", dpi=600)
    
    return fig
    