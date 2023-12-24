# Estrutura do Código e objetivos

A ideia principal desse projeto era fazer um programa 100% autonomo que avaliaria as odds de uma lista de sites que tenho conta para poder colocar bets automaticamente

### Códigos
* Scrapper Selenium:
           A ideia desse é fazer funcs especilizadas para cada tipo de site de modo a ter um comparativo
  * Apos coletado os dados o principio para saber se existe uma possibilidade de **arbitragem** é uma simples conta
    
| Time 1 | Empate | Time 2 |
|----------|----------|----------|
| Bet365 | Betway | Rivalry |
| 2| 3,1 | 6 |

Aplicando a seguinte formula para o caso exemplo acima:

$$
\sum_{i=1}^{n} \frac{1}{\text{odds}_{i}} ( eq 1)
$$


$$
\sum_{i=1}^{3} \frac{1}{\text{odds}_{i}} \cong 0,9892
$$

Com esse resultado em mãos temos que a seguinte situação é **favoravel** para arbitragem ( já que o resultado é <0 ), porém quanto temos que apostar em cada possibilidade para termos lucros?

Vamos ver o seguinte exemplo: Tenho R$ 1.000,00 separados entre as contas e vejo o cenario de odds da tabela acima, e apos o calculo percebo que é favoravel a arbitragem, quanto tenho que apostas no time 1:

$$
Aposta_i = \frac{1000}{(eq1)*odd_i}
$$


$$
Aposta_1 = \frac{1000}{\sum_{i=1}^{n} \frac{1}{\text{odds}_{i}}*odd_i} = 505,43
$$

Então percebemos que se apostarmos 505,43 no time 1; 326,08 no empate; 168,49 no time 2. Teremos resultado de aproximadamente 1010,87 reais. 

Logo ganhamos independente do resultado 10 reais 1% sem ter risco direcional. 


