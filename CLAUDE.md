# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Calculadora Python simples, usada para praticar o fluxo de contribuição com Git/GitHub. Duas interfaces (menu de terminal e GUI Tkinter) compartilham a mesma lógica de operações em `calculadora.py`.

## Comandos

- Rodar a calculadora via menu de terminal: `python main.py`
- Rodar a calculadora com interface gráfica (Tkinter): `python calculadora_gui.py`
- Rodar todos os testes: `pytest test_calculadora.py` (ou apenas `pytest`)
- Rodar um único teste: `pytest test_calculadora.py::test_dividir_por_zero`

## Arquitetura

- `calculadora.py` é o único módulo de lógica de negócio: expõe as quatro operações puras (`somar`, `subtrair`, `multiplicar`, `dividir`). Tanto `main.py` quanto `calculadora_gui.py` importam diretamente dessas funções — não há estado ou classes compartilhadas entre as duas interfaces, cada uma reimplementa seu próprio fluxo em cima das mesmas funções.
- `dividir` lança `ValueError` em divisão por zero; ambas as interfaces capturam essa exceção para exibir uma mensagem de erro em vez de quebrar. Qualquer nova operação/interface deve seguir esse mesmo contrato (levantar `ValueError` para casos inválidos, não `assert` nem retornar sentinelas).
- `main.py`: interface de linha de comando. Monta um dicionário `operacoes` mapeando "1"-"4" para `(nome, função)` e pede dois números ao usuário via `pedir_numero` (que já valida input não numérico em loop).
- `calculadora_gui.py`: interface gráfica Tkinter autocontida na classe `CalculadoraApp`. O estado da calculadora (primeiro número, operação pendente, se está começando um novo número) vive como atributos da instância; cliques de botão passam todos por `ao_clicar`.
- `gui/` (pasta ainda não commitada/untracked no git): um split em andamento de `calculadora_gui.py` em `controller.py` (lógica, equivalente a `CalculadoraApp`) e `view.py` (montagem dos widgets). **Está incompleto**: `gui/__init__.py` importa `gui.app.CalculadoraApp`, mas `gui/app.py` não existe — esse pacote não é funcional nem é referenciado por `main.py` ou `calculadora_gui.py` ainda.
