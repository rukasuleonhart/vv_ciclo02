# Projeto de TDD para Cálculo da Média de Três Notas

Este projeto implementa um algoritmo para calcular a média de três notas utilizando a metodologia de Test-Driven Development (TDD). O objetivo é garantir a corretude do código através de uma abordagem de testes automatizados.

## Objetivo

O objetivo deste projeto é desenvolver um algoritmo que calcule a média de três notas fornecidas pelo usuário, aplicando o TDD nas fases de Red, Green e Refactor.

## Estrutura do Projeto

- `media.py`: Contém a função `calcular_media` que implementa a lógica para calcular a média das três notas.
- `test_media.py`: Contém os testes que validam a funcionalidade da função `calcular_media`, cobrindo diversos cenários e casos de borda.

## Fases do TDD

### 1. Fase Red

Na fase inicial, foram escritos testes que verificam se a função `calcular_media` está implementada corretamente. Todos os testes falharam inicialmente, pois a lógica ainda não estava implementada. Os testes cobrem os seguintes cenários:

- Cálculo da média com valores normais.
- Cálculo da média quando todas as notas são zero.
- Cálculo da média com notas máximas.
- Cálculo da média com valores decimais.
- Tratamento de entradas inválidas.

### 2. Fase Green

Na fase Green, a função `calcular_media` foi implementada com a lógica necessária para passar nos testes. A função calcula a média das três notas da seguinte maneira:

```python
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
