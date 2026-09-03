# Explicação do código: Batalha Naval

Este projeto é um jogo de Batalha Naval executado no terminal. O jogador
monta o próprio tabuleiro, o computador monta o tabuleiro dele aleatoriamente,
e os dois fazem ataques alternados.

## Símbolos usados no tabuleiro

- `" ~ "`: água ou uma casa ainda não revelada.
- `" N "`: parte de um navio.
- `" X "`: casa atingida.
- `" O "`: ataque que acertou água.

As posições usam uma letra para a coluna, de `A` a `J`, e um número para a
linha, de `0` a `9`. Por exemplo, `A5` representa a linha 5 e a coluna A.

## `começo_do_jogo/main.py`

Este é o arquivo usado para iniciar o programa.

- **Linha 1:** comentário que informa que a função principal da interface será importada.
- **Linha 2:** importa `abrir_jogo` do módulo `começo_do_jogo.interface`. Assim, este arquivo pode chamar a tela inicial.
- **Linha 3:** linha em branco; serve apenas para organizar o código.
- **Linha 4:** comentário que explica o início do programa.
- **Linha 5:** verifica se este arquivo foi executado diretamente. Em Python, `__name__` recebe o valor `"__main__"` nesse caso.
- **Linha 6:** chama `abrir_jogo()` quando a condição da linha anterior é verdadeira.

Se outro arquivo importar `main.py`, a chamada da linha 6 não acontece
automaticamente, porque o arquivo não está sendo executado diretamente.

## `começo_do_jogo/interface.py`
- **Linha 2:** importa o módulo `time`, usado para fazer pausas com `sleep`.
- **Linha 3:** comentário explicando o próximo import.
- **Linha 4:** importa `abrir_tabuleiro`, que prepara o tabuleiro do jogador.
- **Linhas 5 e 6:** linhas em branco para separar os imports da função.
- **Linha 7:** comentário que identifica a função principal da tela inicial.
- **Linha 8:** define a função `abrir_jogo`, sem parâmetros.
- **Linha 19:** fecha a string e o `print` iniciado na linha 10.
- **Linha 20:** comentário sobre a pausa visual.
- **Linha 21:** espera dois segundos antes de continuar.
- **Linha 22:** imprime uma linha separadora e uma quebra de linha.
- **Linha 23:** mostra a mensagem de boas-vindas.
- **Linha 58:** comentário sobre a resposta negativa.
- **Linha 59:** entra nesse bloco quando a resposta é `não`, `nao` ou `n`.
- **Linhas 60 a 62:** exibem uma mensagem de carregamento.
- **Linha 63:** espera dois segundos.
- **Linha 64:** linha em branco.
- **Linha 90:** linha em branco.
- **Linha 91:** comentário sobre a opção de saída.
- **Linha 92:** testa se a escolha foi `2`.
- **Linhas 93 a 95:** exibem mensagens de encerramento.
- **Linha 96:** espera dois segundos.

## `tabuleiro/tabuleiro.py`

Este módulo cria o tabuleiro do jogador e valida o posicionamento dos navios.

- **Linha 17:** começa uma lista vazia que receberá as linhas do tabuleiro.
- **Linha 18:** linha em branco.
- **Linha 19:** comentário sobre a criação das linhas com água.
- **Linha 20:** repete 10 vezes, usando os valores de 0 a 9.
- **Linha 21:** cria uma linha com dez casas `" ~ "`. A multiplicação da lista repete o conteúdo.
- **Linha 29:** imprime o índice da linha e suas casas unidas por espaços.
- **Linhas 30 e 31:** linha em branco e comentário sobre mostrar o tabuleiro vazio.
- **Linha 32:** exibe o tabuleiro antes de qualquer navio ser colocado.
- **Linha 33:** linha em branco.
- **Linha 34:** percorre a frota, extraindo o nome e o tamanho de cada navio.
- **Linha 50:** encontra o índice da letra dentro de `ABCDEFGHIJ` e guarda-o em `coluna`.
- **Linha 51:** verifica se a linha está no intervalo de 0 a 9.
- **Linha 52:** informa quando a linha está fora do tabuleiro.
- **Linha 53:** repete o posicionamento.
- **Linha 54:** linha em branco.
- **Linha 55:** pede a direção, remove espaços e transforma a resposta em minúsculas.
- **Linha 56:** cria uma lista vazia para guardar as coordenadas ocupadas pelo navio.
- **Linha 57:** linha em branco.
- **Linha 58:** reconhece `horizontal` ou `h` como direção horizontal.
- **Linha 59:** percorre a quantidade de casas do navio.
- **Linha 60:** adiciona coordenadas que mantêm a linha e aumentam a coluna.
- **Linha 61:** reconhece `vertical` ou `v` como direção vertical.
- **Linha 62:** percorre a quantidade de casas do navio na vertical.
- **Linha 63:** adiciona coordenadas que aumentam a linha e mantêm a coluna.
- **Linha 68:** assume inicialmente que o navio cabe no tabuleiro.
- **Linha 69:** percorre cada coordenada calculada.
- **Linha 70:** verifica se a linha ou a coluna ultrapassou o limite 9.
- **Linha 71:** marca que o navio não cabe quando alguma coordenada está fora do tabuleiro.
- **Linha 72:** linha em branco.
- **Linha 73:** testa o resultado da verificação de limite.
- **Linha 74:** avisa que o navio não cabe.
- **Linha 75:** reinicia a tentativa.
- **Linha 76:** linha em branco.
- **Linha 77:** assume que nenhuma casa está ocupada por outro navio.
- **Linha 78:** percorre as coordenadas do navio novamente.
- **Linha 79:** verifica se alguma casa já contém `" N "`.
- **Linha 80:** marca que existe sobreposição.
- **Linha 81:** linha em branco.
- **Linha 82:** testa se houve sobreposição.
- **Linha 83:** informa que navios não podem compartilhar casas.
- **Linha 84:** reinicia a tentativa.
- **Linha 85:** linha em branco.
- **Linha 86:** percorre as casas válidas para finalmente posicionar o navio.
- **Linha 87:** troca o símbolo de cada casa para `" N "`.
- **Linha 88:** mostra o tabuleiro atualizado.
- **Linha 89:** encerra o laço do navio atual; o próximo navio será processado.
- **Linhas 90 e 91:** linha em branco e chamada de `iniciar_partida`, passando o tabuleiro do jogador e a função de exibição.

## `bot/tabuleiro_bot.py`

Este arquivo cria e preenche automaticamente o tabuleiro do computador.

- **Linha 1:** importa `random`, usado para sortear posições e direções.
- **Linhas 2 e 3:** linhas em branco.
- **Linha 4:** define `criar_tabuleiro_bot`.
- **Linha 5:** linha em branco.
- **Linha 6:** começa uma lista vazia.
- **Linha 7:** linha em branco.
- **Linha 8:** repete para criar as 10 linhas.
- **Linha 9:** começa uma linha vazia.
- **Linha 10:** linha em branco.
- **Linha 11:** repete 10 vezes para criar as colunas.
- **Linha 12:** adiciona uma casa de água à linha.
- **Linha 13:** linha em branco.
- **Linha 14:** adiciona a linha completa ao tabuleiro.
- **Linha 15:** linha em branco.
- **Linha 16:** devolve o tabuleiro vazio.
- **Linhas 17 e 18:** linhas em branco.
- **Linha 19:** define `colocar_navio_bot`, recebendo um tabuleiro.
- **Linha 20:** percorre os tamanhos 4, 3 e 2.
- **Linha 21:** repete o sorteio até encontrar uma posição válida.
- **Linha 22:** sorteia uma linha entre 0 e 9.
- **Linha 23:** sorteia uma coluna entre 0 e 9.
- **Linha 24:** sorteia horizontal ou vertical.
- **Linha 25:** linha em branco.
- **Linha 26:** verifica se a direção sorteada é horizontal.
- **Linha 27:** monta as coordenadas mantendo a linha e aumentando a coluna.
- **Linha 28:** caso contrário, trata a direção como vertical.
- **Linha 29:** monta as coordenadas aumentando a linha e mantendo a coluna.
- **Linha 30:** linha em branco.
- **Linhas 31 e 32:** usam `any` para descobrir se alguma coordenada ultrapassa 9. A expressão `for` dentro de `any` percorre todas as casas.
- **Linha 33:** tenta outro sorteio se o navio não couber.
- **Linhas 34 e 35:** verificam, com `any`, se alguma casa já contém navio.
- **Linha 36:** tenta outro sorteio quando existe sobreposição.
- **Linha 37:** linha em branco.
- **Linha 38:** percorre as coordenadas aprovadas.
- **Linha 39:** marca cada uma como parte de navio.
- **Linha 40:** encerra o `while` e passa ao próximo tamanho de navio.
- **Linhas 41 a 42:** linhas em branco.
- **Linha 43:** define `preparar_bot`.
- **Linha 44:** linha em branco.
- **Linha 45:** cria o tabuleiro vazio.
- **Linha 46:** linha em branco.
- **Linha 47:** coloca os três navios aleatoriamente.
- **Linha 48:** linha em branco.
- **Linha 49:** devolve o tabuleiro pronto.

## `ataque/ataque.py`

Este módulo controla a jogada do jogador contra o computador.

- **Linha 1:** define `abrir_ataque`, recebendo o tabuleiro inimigo e uma função para mostrá-lo.
- **Linha 2:** cria a lista das colunas válidas.
- **Linha 3:** linha em branco.
- **Linha 4:** inicia a repetição da validação da coordenada.
- **Linha 5:** imprime uma separação visual.
- **Linha 6:** pede a coordenada do ataque e remove espaços externos.
- **Linha 7:** imprime outra separação.
- **Linhas 8 a 11:** rejeitam entradas com menos de dois caracteres e repetem a pergunta.
- **Linha 13:** extrai e normaliza a letra da coluna.
- **Linha 14:** extrai o restante da entrada como número da linha.
- **Linhas 16 a 18:** rejeitam letras inválidas ou números que não sejam formados apenas por dígitos.
- **Linha 20:** converte a letra para o índice da coluna.
- **Linha 21:** converte o número para inteiro.
- **Linhas 23 a 25:** rejeitam linhas fora do tamanho do tabuleiro.
- **Linhas 27 a 29:** impedem que o jogador ataque novamente uma casa marcada com `X` ou `O`.
- **Linha 31:** encerra a validação quando a coordenada é válida e ainda não foi usada.
- **Linha 33:** verifica se a casa escolhida contém um navio.
- **Linha 34:** marca um acerto com `X`.
- **Linha 35:** imprime uma linha em branco.
- **Linha 36:** exibe o tabuleiro inimigo atualizado.
- **Linha 37:** informa o acerto.
- **Linha 39:** começa o caso em que a casa não contém navio.
- **Linha 40:** imprime uma linha em branco.
- **Linha 41:** marca a casa como água atingida, usando `O`.
- **Linha 42:** exibe o tabuleiro atualizado.
- **Linha 43:** informa que foi água.

## `bot/ataque_bot.py`

Este módulo escolhe uma casa aleatória para o ataque do computador.

- **Linha 1:** importa a biblioteca `random`.
- **Linhas 2 e 3:** linhas em branco.
- **Linha 4:** define `ataque_bot`, recebendo o tabuleiro do jogador e sua função de exibição.
- **Linhas 5 a 7:** iniciam um laço de tentativa contínua.
- **Linha 8:** sorteia uma linha de 0 a 9.
- **Linha 9:** sorteia uma coluna de 0 a 9.
- **Linha 10:** linha em branco.
- **Linha 11:** lê o conteúdo da casa sorteada.
- **Linha 12:** linha em branco.
- **Linha 13:** verifica se o bot encontrou um navio.
- **Linha 14:** linha em branco.
- **Linha 15:** transforma a casa em `X`, registrando o acerto.
- **Linhas 16 a 18:** mostram as mensagens de ataque e acerto.
- **Linha 20:** mostra o tabuleiro do jogador.
- **Linha 22:** retorna da função; o bot termina sua jogada.
- **Linha 24:** verifica se a casa sorteada era água.
- **Linha 25:** linha em branco.
- **Linha 26:** transforma a água em `O`.
- **Linhas 27 a 29:** mostram as mensagens de ataque e água.
- **Linha 31:** mostra o tabuleiro atualizado.
- **Linha 33:** retorna da função.

Se o sorteio cair em uma casa já atacada (`X` ou `O`), nenhum dos dois blocos
é executado. O `while` então sorteia outra casa na próxima repetição.

## `partida/partida.py`

Este é o controlador da partida: ele alterna os turnos e verifica a vitória.

- **Linha 1:** comentário sobre a função de ataque do jogador.
- **Linha 2:** importa `abrir_ataque`.
- **Linha 3:** comentário sobre a criação do tabuleiro do bot.
- **Linha 4:** importa `preparar_bot`.
- **Linha 5:** comentário sobre o ataque do computador.
- **Linha 6:** importa `ataque_bot`.
- **Linhas 7 e 8:** linhas em branco.
- **Linha 9:** comentário sobre esconder os navios do bot.
- **Linha 10:** define `mostrar_tabuleiro_bot`.
- **Linha 11:** imprime os nomes das colunas.
- **Linha 12:** linha em branco.
- **Linha 13:** percorre cada linha do tabuleiro.
- **Linha 14:** começa uma lista temporária para a versão escondida.
- **Linha 15:** linha em branco.
- **Linha 16:** percorre cada casa da linha atual.
- **Linha 17:** verifica se a casa é um navio.
- **Linha 18:** substitui navio por água apenas na lista exibida.
- **Linha 19:** começa o caso das casas que não são navios.
- **Linha 20:** copia o conteúdo original para a lista escondida.
- **Linha 21:** linha em branco.
- **Linha 22:** imprime a linha escondida. O tabuleiro real não é alterado.
- **Linhas 23 e 24:** linhas em branco.
- **Linha 25:** comentário sobre a verificação de vitória.
- **Linha 26:** define `verificar_vitoria`.
- **Linha 27:** percorre todas as linhas recebidas.
- **Linha 28:** procura o símbolo de navio na linha atual.
- **Linha 29:** retorna `False` assim que encontra qualquer navio vivo.
- **Linha 30:** linha em branco.
- **Linha 31:** retorna `True` se terminou o laço sem encontrar navios.
- **Linhas 32 e 33:** linhas em branco.
- **Linha 34:** comentário sobre o começo da partida.
- **Linha 35:** define `iniciar_partida`, recebendo o tabuleiro do jogador e sua função de exibição.
- **Linha 36:** linha em branco.
- **Linha 37:** comentário sobre o tabuleiro do computador.
- **Linha 38:** cria o tabuleiro do bot já com navios aleatórios.
- **Linha 39:** linha em branco.
- **Linha 40:** comentário sobre o laço principal.
- **Linha 41:** começa a partida, que só termina com um `return`.
- **Linha 42:** linha em branco.
- **Linha 43:** anuncia o turno do jogador.
- **Linha 44:** linha em branco.
- **Linha 45:** comentário sobre o ataque do jogador.
- **Linha 46:** permite ao jogador escolher e executar um ataque no tabuleiro do bot.
- **Linha 47:** linha em branco.
- **Linha 48:** comentário sobre verificar se o bot perdeu.
- **Linha 49:** chama `verificar_vitoria` no tabuleiro do bot.
- **Linhas 50 a 52:** exibem a mensagem de vitória.
- **Linhas 53 e 54:** linha em branco e comentário sobre continuar ou sair.
- **Linha 55:** inicia um laço para validar essa decisão.
- **Linha 56:** pede a escolha do jogador.
- **Linha 57:** linha em branco.
- **Linha 58:** testa a opção de continuar.
- **Linhas 59 e 60:** comentário e importação local de `abrir_jogo`, evitando fazer esse import no topo junto com os módulos que já dependem da partida.
- **Linha 61:** volta à tela inicial.
- **Linha 62:** retorna e encerra a partida atual.
- **Linha 63:** testa a opção de sair.
- **Linha 64:** comentário sobre o encerramento.
- **Linha 65:** agradece ao jogador.
- **Linha 66:** retorna e encerra a função.
- **Linhas 67 e 68:** tratam uma escolha inválida e mantêm o laço de decisão ativo.
- **Linha 69:** linha em branco.
- **Linha 70:** anuncia o turno do bot.
- **Linha 71:** linha em branco.
- **Linha 72:** comentário sobre o ataque do bot.
- **Linha 73:** executa um ataque aleatório contra o tabuleiro do jogador.
- **Linha 74:** linha em branco.
- **Linha 75:** comentário sobre verificar se o jogador perdeu.
- **Linha 76:** testa se não restam navios no tabuleiro do jogador.
- **Linhas 77 a 79:** exibem a mensagem de derrota.
- **Linhas 80 e 81:** linha em branco e comentário sobre a decisão final.
- **Linha 82:** começa o laço que valida continuar ou sair.
- **Linha 83:** pede a decisão.
- **Linha 84:** linha em branco.
- **Linha 85:** testa a opção de iniciar outra partida.
- **Linhas 86 e 87:** comentário e importação local de `abrir_jogo`.
- **Linha 88:** abre novamente a tela inicial.
- **Linha 89:** encerra a partida atual.
- **Linha 90:** testa a opção de sair.
- **Linha 91:** comentário sobre o encerramento.
- **Linha 92:** imprime a mensagem de agradecimento.
- **Linha 93:** retorna da função.
- **Linhas 94 e 95:** informam uma opção inválida e repetem o laço.

## Fluxo completo do programa

1. `começo_do_jogo/main.py` chama `abrir_jogo`.
2. A interface apresenta a arte, as regras e o menu.
3. Ao escolher jogar, `abrir_tabuleiro` cria uma matriz 10x10 e solicita os três navios.
4. Cada entrada é validada quanto ao formato, aos limites, à direção e à sobreposição.
5. `iniciar_partida` cria o tabuleiro secreto do bot.
6. O jogador ataca usando `abrir_ataque`; depois o bot ataca usando `ataque_bot`.
7. `verificar_vitoria` procura se ainda existe algum `" N "` em cada tabuleiro.
8. Quando um tabuleiro não possui mais navios, o jogo mostra vitória ou derrota e oferece uma nova partida ou a saída.

## Observações importantes

- O nome do jogador é exibido, mas não é usado na lógica da partida.
- `time` foi importado em `tabuleiro.py`, mas não é utilizado ali.
- A verificação de posição aceita números com mais de um dígito e depois rejeita os que ficam fora de 0 a 9; isso funciona, embora a mensagem peça um único dígito.
- O código impede sobreposição de navios, mas permite que navios fiquem encostados uns nos outros.
- O bot não revela seus navios porque `mostrar_tabuleiro_bot` troca `" N "` por `" ~ "` apenas no momento da impressão.
