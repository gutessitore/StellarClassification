# StellarClassification
Projeto para classificar estrelas, galáxias e quasares ( ***quasi-stellar radio source*** , ***quasi-stellar object*** ou um núcleo galáctico ativo).

## Pré-requisitos

1. Oferecer uma contextualização do contexto do negócio e da necessidade da solução
que seu grupo irá propor.
2. Estabelecer claramente o objetivo do trabalho.
3. Implementar o projeto.
4. Analisar como a implementação atende ao objetivo proposto.
5. Conclusão.

**Composição dos grupos**

Cada grupo deve ter entre 2 e 6 alun@s. Trabalhos individuais não são permitidos.


## Requisitos do projeto:

Os projetos devem utilizar as mesmas técnicas apresentadas durante o curso
para cumprir os requisitos.

**Machine Learning**
1. Utilizar um ou mais datasets (não pode ser toy) para o treinamento dos
classificadores. O dataset deve conter múltiplas dimensőes e ter classes
desbalanceadas.
2. Realizar uma análise exploratória do dataset por meio de um caderno Jupyter.
Utilize gráficos na análise.
3. Treinar um classificador Naive Bayes (Multinomial, Bernoulli ou Gaussian).
4. Treinar um classificador Support Vector Machine (SVM).
5. Treinar um classificador de Árvore de Decisão ou Floresta Aleatória.
6. Reduzir a dimensionalidade com Principal Component Analysis (PCA) e
interpretar os resultados.
7. Todos os classificadores devem ser avaliados com validação cruzada,
utilizando as métricas Fβ, acurácia, revocação (recall), precisão. Além disso, utilizem a
matriz de confusão para a visualização do desempenho.
8. Todos os classificadores devem ser persisitidos (joblib, pickle) antes de serem
entregues e publicados no GitHub.
9. O projeto-final de contar com um modelo por integrante do grupo,
possivelmente além dos modelos exigidos nesta especificação.
10. Aplicar PySpark (opcional).
