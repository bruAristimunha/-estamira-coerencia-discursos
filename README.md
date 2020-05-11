<h1 align="center">
  <br> [ERAMIA 2020] Quem é Estamira? Uma análise da coerência dos discursos através de combinação de medidas para classificação de texto
  <br>
</h1>
<p align="center">
   • <a href="http://lattes.cnpq.br/7474686706879869">Bruno Aristimunha<sup>1</sup></a> 
</p>

> <sup>1</sup> Centro de Matemática, Computação e Cognição (CMCC), Universidade Federal do ABC (UFABC), Rua Arcturus, 03. Jardim Antares, São Bernardo do Campo, CEP 09606-070, SP, Brasil.

<p align="center">
<img src="https://github.com/bruAristimunha/estamira-coerencia-discursos/raw/master/reports/figures/poster-estamira.jpg"> 
</p>

<p align="center">
  Cartaz de Divulgação: Estamira (2004).
</p>

![pipeline](https://github.com/bruAristimunha/estamira-coerencia-discursos/raw/master/reports/figures/pipeline.png)


## Esse repostitório é a implementação oficial do artigo apresentado no evento.  [[Artigo]](https://github.com/bruAristimunha/estamira-coerencia-discursos/blob/master/reports/ERAMIA_SP_2020.pdf) [[Citação]](#citação) [[Avaliação]](https://github.com/bruAristimunha/estamira-coerencia-discursos/blob/master/Reviews.md)


> **Abstract:** This article investigates disorders in natural speech through natural language processing techniques. We analyze the possible incoherent/schizophrenic speech using the Latent Semantic Analysis method and connectivity measures of the co-occurrence graph. Using these measures as attributes, we selected 4 classifiers to distinguish illogical speech patterns. The chosen __corpus__ comes from the lines of characters from the film Estamira (2004), which tells the life of a garbage collector from Rio de Janeiro. This choice is justified by the fact that the narrative is anchored in complex talks of its main character, Estamira, who for long periods conducts obscure dialogues. There is also a discursive clash between the character's lines and the eloquence of her family.
> 
> **Resumo:** Este artigo investiga os distúrbios no discurso natural através de técnicas de processamento de linguagem natural. O discurso incoerente é um sintoma cardinal associado a condições psiquiátricas e neurológicas, e. g., esquizofrenia e bipolar. Essa categoria de distúrbio afeta a comunicação verbal tornando o discurso vago, confuso e ilógico. Analisamos o discurso incoerente/esquizofrênico através do método de Análise Semântica Latente e de medidas de conectividade do grafo de co-ocorrência. Combinando essas medidas como atributos, empregamos 4 classificadores para distinguir padrões de fala ilógicos. O __corpus__ escolhido é oriundo das falas de personagens do filme Estamira (2004), que conta a vida de uma catadora de lixo do Rio de Janeiro. A escolha da obra justifica-se por uma narrativa ancorada em discursos complexos de sua personagem principal, Estamira, que durante longos períodos conduz diálogos abstrusos. Há, também, choque discursivo entre as falas da personagem e a lógica na eloquência de seus familiares.

--------------------

## Pré-requisito para Reprodução

Clone esse repositório

```shell
!git clone https://github.com/bruAristimunha/estamira-coerencia-discursos
```

Instale a biblioteca Conda, recomendamos o [tutorial](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Crie uma variável de sistema no conda, conforme instruções abaixo:

```shell
conda create --name estamira python=3.7 pip --yes
conda activate estamira
```

Instale os pacotes necessários:

```shell
pip install -r requirements.txt
```
----

## Treino e Avaliação

Você pode avaliar os resultados reportados seguindo o tutorial disponível no [jupyter-notebook](https://github.com/bruAristimunha/estamira-coerencia-discursos/blob/master/notebooks/Quem%20%C3%A9%20Estamira_%20Uma%20an%C3%A1lise%20da%20coer%C3%AAncia%20dos%20discursos%20atrav%C3%A9s%20de%20combina%C3%A7%C3%A3o%20de%20algoritmos%20para%20classifica%C3%A7%C3%A3o%20de%20texto.ipynb), ou então, empregar a ferramenta colab para reprodução em uma máquina virtual gratuita.

Além do formato em jupyter-artigo, você também pode reproduzir via linha de comando cada das etapas: análise exploratória do conjunto de dados, extração de atributos, classificação e avaliação dos resultados. Ou então, executar toda a avaliação.

```
python src/eda.py 
python src/feature_extract.py 
python src/classification.py 
python src/eval.py 
python src/complete_proce.py
```

# Licença
Este trabalho está licenciado com [CC-BY-NC 1.0](LICENSE).

## Citação

Em formato plano:

Aristimunha, Bruno. Quem é Estamira? Coerência dos discursos através de combinação de medidas para classificação de texto. Em: **Anais da 1ª Escola Regional de Aprendizado de Máquina e Inteligência Artificial de São Paulo (ERAMIA-SP)**, 2020, São Paulo. v. 1. p. 1-4. 

Em formato latex:

```bibtex
@InProceedings{aristimunha:2020,
 author   = {Aristimunha, Bruno},
 booktitle = {1ª Escola Regional de Aprendizado de Máquina e Inteligência Artificial de São Paulo (ERAMIA-SP)},
 title    = {Quem é Estamira? Coerência dos discursos através de combinação de medidas para classificação de texto},
 year     = {2020},
 note     = {[para aparecer]},
}
```
## Passos Futuros
- [ ] Avaliar a importância do que os classificadores estão aprendendo, visando um melhor entendimento dos padrões do discurso. 
- [ ] Extração de atributos, com modelos de linguagem, \textit{e. g.}, BERT e FastText. 
- [ ] Avaliar o contexto da detecção de anomalia, com classificação de uma classe. 
- [ ] Incluir de atributos mais relacionados às características da doença, como contagem de pronomes e análise de sentimentos. 
- [ ] Recorte de fala diferente, como o reconhecimento por timbre/imagem, 

