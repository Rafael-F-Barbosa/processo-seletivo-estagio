# Processo seletivo para estágio na Polícia Federal, 11/2021

O problema escolhido foi o Mesa Redonda, disponível em https://olimpiada.ic.unicamp.br/pratique/pu/2019/f3/mesa/. É um problema da Fase 3 das olimpíadas da Unicamp de 2019.

## O problema

Ana, Beatriz e Carolina sempre saem juntas para tomar café numa padaria onde as mesas são circulares e têm três cadeiras numeradas 0, 1 e 2, no sentido anti-horário, como ilustrado na figura ao lado.

Elas gostam de decidir quem vai sentar em qual cadeira com uma brincadeira gerando números aleatórios nos seus celulares. Primeiro Ana sorteia um número inteiro A e, começando da cadeira 1, seguindo no sentido anti-horário, conta A cadeiras e senta na cadeira em que a contagem terminar. Depois Beatriz sorteia um número B e faz a mesma coisa: começando da cadeira 1, no sentido anti-horário, conta B cadeiras. Se a cadeira final estiver livre, Beatriz senta nela. Caso seja a cadeira onde Ana está sentada, então Beatriz senta na próxima cadeira no sentido anti-horário. Claro, ao final, Carolina senta na cadeira que estiver livre.


![Alt ou título da imagem](/images/mesa_redonda.jpg)

### Entrada
A primeira linha da entrada contém um inteiro A representando o número sorteado por Ana. A segunda linha da entrada contém um inteiro B representando o número sorteado por Beatriz.

### Saída
Seu programa deve imprimir uma linha contendo um número inteiro indicando a cadeira onde Carolina vai sentar.

## Solução
Foi utilizada a linguagem de programação python e a solução foi pensada da seguinte forma:

- Foi criada uma lista circular, assim ficaria fácil de percorrer as cadeiras e também seria fácil alterar o programa caso a quantidade de mesas fosse alterada.
- Para cada amiga, é percorrida a lista circular de acordo com o número passado como argumento.
  - Se a cadeira está desocupada esta amiga passa a ocupá-la, senão a próxima cadeira é ocupada
- Por fim percorre-se a lista até encontrar a cadeira desocupada e a última amiga ocupa esta cadeira