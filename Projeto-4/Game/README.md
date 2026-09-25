# 🎮 Jogo da Adivinhação (Versão Simples)

<p align="left">
  <img src="https://img.shields.io/badge/Python-Game-yellow?style=flat-square&logo=python" alt="Python">
</p>

## 📝 Descrição
A versão inicial de um minijogo interativo de lógica para o terminal. Neste script, o jogador tem o desafio de descobrir um número secreto com uma dificuldade fixa e uma quantidade limitada de chances.

## 🚀 Como funciona
1. O sistema utiliza a biblioteca `random` para gerar um número aleatório fixo entre **1 e 10**.
2. O jogador possui exatamente **3 tentativas** para acertar.
3. Um laço de repetição (`while`) controla o fluxo do jogo, deduzindo uma tentativa a cada palpite incorreto.
4. Estruturas condicionais simples avaliam se o palpite é igual ao número secreto (vitória) ou se o jogador errou.
5. O jogo termina automaticamente quando o jogador acerta ou quando as tentativas chegam a zero.

**Arquivo principal:** `jogo_adivinhacao.py`
