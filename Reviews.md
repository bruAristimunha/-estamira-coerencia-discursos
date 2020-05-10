****

\#204635: Quem é Estamira? Coerência dos discursos através de combinação
de medidas para classificação de texto

Authors

-   [Bruno
    Aristimunha](https://jems.sbc.org.br/jems2/index.php?r=person/view&id=162677)
    (UFABC)

Abstract

Este artigo investiga os distúrbios no discurso natural através de
técnicas de processamento de linguagem natural. O discurso incoerente é
um sintoma cardinal associado a condições psiquiátricas e neurológicas,
e. g., esquizofrenia e bipolar. Essa categoria de distúrbio afeta a
comunicação verbal tornando o discurso vago, confuso e ilógico.
Analisamos o discurso incoerente/esquizofrênico através do método de
Análise Semântica Latente e de medidas de conectividade do grafo de
co-ocorrência. Combinando essas medidas como atributos, empregamos __4__
classificadores para distinguir padrões de fala ilógicos. O *corpus*
escolhido é oriundo das falas de personagens do filme Estamira (2004),
que conta a vida de uma catadora de lixo do Rio de Janeiro. A escolha da
obra justifica-se por uma narrativa ancorada em discursos complexos de
sua personagem principal, Estamira, que durante longos períodos conduz
diálogos abstrusos. Há, também, choque discursivo entre as falas da
personagem e a lógica na eloquência de seus familiares.

Topics

Processamento de Linguagem Natural

Conference

ERAMIA-SP 2020

Track

ERAMIA-SP

Category

Status

accepted

Files

  Description        File name                                                                                          Type   Size        Created
  ------------------ -------------------------------------------------------------------------------------------------- ------ ----------- -------------------------------
  Paper manuscript   [204635.pdf](https://jems.sbc.org.br/jems2/index.php?r=paper/download&p=204635&f=0 "204635.pdf")   pdf    292.95 KB   May 06, 2020 - 10:18 PM (BRT)



**  Reviews

Review 1

**Originalidade author**:\
4) Boa

**Mérito Técnico author**:\
4) Bom

**Clareza/Qualidade do texto author**:\
5) Ótima

**Relevância author**:\
4) Boa

**Avaliação geral author**:\
5) Aceitação forte

+--------------------------------------------------------------------------+

__Comentários para os Autores:Comentários para os Autores do Artigo. Deve conter a contribuição principal, pontos fortes e pontos a serem melhorados, e demais recomendações específicas. (preenchimento obrigatório):__

Os autores utilizaram métodos de classificação de textos para analisar a coerência de discurso. Os atributos foram gerados por meio de matrizes de co-ocorrência, Análise Semântica Latente, bem como modelagens por grafos.


O trabalho é interessante para o ERAMIA. Em especial, determinar distúrbios no discurso podem colaborar na análise de sintomas de esquizofrenia.


Na minha opinião, a etapa crucial da estratégia são as técnicas de extração de atributos. Considero que as técnicas utilizadas são bons baselines, mas existem estratégias melhores na literatura. Em particular, sugiro que os autores explorem modelos de linguagem treinados em grandes datasets externos (existem para português, como o BERT e FastText). Os modelos de linguagens permitem identificar a probabilidade de ocorrência de uma próxima palavra, dada a palavra atual. Como o modelo é treinado em milhões de exemplos, tende a convergir para estruturas coerentes. Assim, um texto não coerente será muito diferente do que o esperado (em probabilidade) por um desses modelos de linguagem; sendo um critério interessante para geração de atributos (no mínimo mais uma medida baseada no estado-da-arte).


Correções para a versão final:
* Adicionar Abstract (Inglês)

+--------------------------------------------------------------------------+

Review 2

**Originalidade author**:\
3) Media

**Mérito Técnico author**:\
4) Bom

**Clareza/Qualidade do texto author**:\
5) Ótima

**Relevância author**:\
4) Boa

**Avaliação geral author**:\
4) Aceitação fraca

+--------------------------------------------------------------------------+

__Comentários para os Autores:Comentários para os Autores do Artigo. Deve conter a contribuição principal, pontos fortes e pontos a serem melhorados, e demais recomendações específicas. (preenchimento obrigatório):__


Primeiramente, parabéns pelo trabalho executado. Além do texto ser muito bem escrito, a metodologia é clara, as escolhas em sua maioria são justificadas. Apenas senti falta na justificativa da escolha dos algoritmos de aprendizado de máquina utilizados pelo autor para a predição das falas. Outra justificativa que poderia aparecer no texto é a escolha do número de vizinhos proposta para o algoritmo knn, pois geralmente, optamos pela escolha de valores ímpares, para evitar empates de classificação. Além disso, para completar a seção de resultados, seria bem vinda uma comparação dos valores de acurácia obtidos pelo autor com abordagens já existentes de detecção de falas esquizofrênicas.


Para auxiliar o desenvolvimento de trabalhos futuros, seria interessante se o autor disponibilizasse os dados e algoritmos utilizados de forma pública, e incluísse essa informação em seu artigo.


Como sugestão, deixo aqui alguns comentários que possam contribuir em trabalhos futuros: Alguns algoritmos poderiam ser testados, como aprendizado baseados em uma única classe, de forma que falas de pessoas esquizofrênicas poderiam ser a classe de interesse, ou algoritmos de detecção de anomalias, de forma que encontrar uma anomalia seria o equivalente a encontrar falas de pessoas esquizofrênicas.


Outra sugestão para trabalhos futuros: de acordo com a fala do autor "Podemos citar algumas características importantes no discurso esquizofrênico: alto uso de pronomes de auto-referencialmente e avolia tendendo aos estados negativos", uma sugestão seria avaliar se a incorporação de algoritmos de análise de sentimentos seria benéfica para o assunto. Ou mesmo testar uma abordagem simples de contagem de pronomes, com bibliotecas que classificam palavras gramaticalmente.

+--------------------------------------------------------------------------+

