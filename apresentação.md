# Apresentação do projeto: Batalha Naval

## 1. O que é o projeto?

Este projeto é um jogo de Batalha Naval feito em Python e executado pelo
terminal do computador.

O jogador enfrenta o computador. Cada um possui um tabuleiro de 10 linhas por
10 colunas e três navios:

- Porta-avião: 4 casas;
- Cruzador: 3 casas;
- Submarino: 2 casas.

O objetivo é descobrir e acertar todas as partes dos navios do adversário
antes que ele acerte os nossos.

## 2. Como o jogo começa?

O arquivo `main.py` é o ponto de entrada do programa. Ele chama a função
`abrir_jogo()`, que fica no arquivo da interface.

Na tela inicial, o programa:

1. Mostra uma arte de Batalha Naval;
2. Apresenta uma mensagem de boas-vindas;
3. Pergunta se o jogador quer conhecer as regras;
4. Pede o nome do jogador;
5. Mostra as opções de jogar ou sair.

As pausas feitas com `time.sleep()` deixam as mensagens mais organizadas e
criam um efeito de carregamento.

## 3. Como é o tabuleiro?

O tabuleiro é uma lista formada por dez linhas, e cada linha possui dez casas.
As colunas são identificadas pelas letras de `A` a `J`, e as linhas pelos
números de `0` a `9`.

Os símbolos usados são:

- `~`: água ou uma casa ainda não descoberta;
- `N`: parte de um navio;
- `X`: navio atingido;
- `O`: ataque que acertou a água.

Por exemplo, a posição `B5` significa coluna B e linha 5.

## 4. Como o jogador posiciona os navios?

Ao escolher jogar, a função `abrir_tabuleiro()` cria o tabuleiro do jogador e
solicita a posição inicial de cada navio.

O jogador informa:

- A posição inicial, como `A5`;
- A direção, que pode ser horizontal ou vertical.

O programa verifica automaticamente se:

- A posição foi escrita corretamente;
- A linha e a coluna estão dentro do tabuleiro;
- O navio cabe inteiro no tabuleiro;
- O navio não ocupa uma casa já usada por outro navio.

Se houver algum erro, o jogador precisa tentar novamente. Quando a posição é
aceita, as casas do navio recebem o símbolo `N`.

## 5. Como o computador monta o tabuleiro?

O computador usa a biblioteca `random` para escolher aleatoriamente:

- A linha inicial;
- A coluna inicial;
- A direção do navio.

O programa repete o sorteio se o navio não couber ou se ocupar uma casa já
usada. Dessa forma, o computador sempre termina com os três navios em
posições válidas.

Os navios do computador ficam escondidos. Quando o tabuleiro dele é mostrado,
as casas com navios aparecem como água, mas o tabuleiro real continua guardado
internamente.

## 6. Como funcionam os ataques?

Na vez do jogador, a função `abrir_ataque()` pede uma coordenada. Ela verifica
se a posição está dentro do tabuleiro e se ainda não foi atacada.

- Se houver um navio, a casa recebe `X` e aparece “ACERTOU!”;
- Se houver água, a casa recebe `O` e aparece “ÁGUA!”;
- Se a casa já tiver `X` ou `O`, o programa pede outra coordenada.

Na vez do computador, a função `ataque_bot()` escolhe uma casa aleatória.
Casas já atacadas são ignoradas e um novo sorteio é feito.

## 7. Como a vitória é verificada?

A função `verificar_vitoria()` percorre todas as linhas do tabuleiro procurando
casas que ainda tenham o símbolo `N`.

- Se encontrar pelo menos um `N`, ainda existem navios vivos;
- Se não encontrar nenhum `N`, todos os navios foram destruídos.

Depois de cada ataque, o jogo faz essa verificação. Se o tabuleiro do
computador ficar sem navios, o jogador vence. Se o tabuleiro do jogador ficar
sem navios, o jogador perde.

## 8. Organização dos arquivos

- `começo_do_jogo/main.py`: inicia o programa;
- `começo_do_jogo/interface.py`: mostra a tela inicial, as regras e os menus;
- `tabuleiro/tabuleiro.py`: cria o tabuleiro do jogador e posiciona seus navios;
- `bot/tabuleiro_bot.py`: cria e posiciona os navios do computador;
- `ataque/ataque.py`: controla os ataques do jogador;
- `bot/ataque_bot.py`: controla os ataques do computador;
- `partida/partida.py`: alterna os turnos e verifica o resultado.

Cada arquivo possui uma responsabilidade específica. Isso facilita entender,
organizar e modificar o programa.

## 9. Fluxo de uma partida

1. O programa abre a tela inicial.
2. O jogador escolhe começar uma partida.
3. O jogador posiciona seus três navios.
4. O computador posiciona seus navios automaticamente.
5. O jogador escolhe uma casa para atacar.
6. O computador escolhe uma casa para atacar.
7. Os turnos continuam alternados.
8. Após cada ataque, o programa verifica se alguém perdeu todos os navios.
9. No final, o jogador pode iniciar outra partida ou sair.

## 10. Conclusão

O projeto combina entrada de dados, listas, funções, repetições, condições e
sorteios para criar um jogo completo no terminal.

A ideia principal é separar o jogo em partes: a interface cuida das mensagens,
os módulos de tabuleiro cuidam dos navios, os módulos de ataque cuidam das
jogadas e o módulo de partida coordena tudo.
