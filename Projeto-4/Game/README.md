# 🎮 Jogo da Adivinhação (Com Níveis de Dificuldade)

<p align="left">
  <img src="https://img.shields.io/badge/Python-Game-yellow?style=flat-square&logo=python" alt="Python">
</p>

## 📝 Descrição
Um jogo interativo de terminal onde o jogador tenta descobrir um número secreto gerado aleatoriamente pelo sistema. O jogo conta com três níveis de dificuldade que alteram o intervalo de números e a quantidade de tentativas disponíveis.

## 🚀 Como funciona
1. O menu inicial solicita ao jogador que escolha o nível de dificuldade:
   - **Fácil:** 1 a 10 (5 tentativas)
   - **Médio:** 1 a 50 (4 tentativas)
   - **Difícil:** 1 a 100 (3 tentativas)
2. O sistema gera o número com a biblioteca `random`.
3. Através de um laço `while`, o jogador insere seus palpites.
4. Estruturas condicionais (`if/elif/else`) fornecem dicas se o número secreto é "MAIOR" ou "MENOR" que o palpite atual.
5. O jogo encerra com mensagem de vitória caso o usuário acerte, ou derrota caso as tentativas acabem.

**Arquivo principal:** `jogo_adivinhacao.py`
