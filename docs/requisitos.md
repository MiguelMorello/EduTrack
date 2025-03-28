# Requisitos do Sistema de Cadastro de Alunos

Este sistema foi desenvolvido com alguns requisitos técnicos e de funcionalidade. Aqui estão listados os requisitos necessários para que o sistema funcione corretamente.

## Requisitos Funcionais

1. **Cadastro de Alunos**:
   - O sistema deve permitir o cadastro de alunos com as seguintes informações:
     - Nome do aluno
     - Matrícula
     - Notas das disciplinas
   - O sistema deve permitir adicionar novos alunos à turma.

2. **Listagem de Alunos**:
   - O sistema deve ser capaz de listar os alunos de uma turma.
   - O sistema deve exibir informações como o nome do aluno e matrícula.

3. **Cálculo de Média**:
   - O sistema deve calcular a média das notas de cada aluno.
   - O sistema deve determinar se o aluno foi aprovado ou reprovado com base na média calculada (aprovado ≥ 7.0).

4. **Relatórios de Turma**:
   - O sistema deve gerar um relatório com a listagem de alunos e suas respectivas médias de notas.
   - O sistema deve mostrar o status de aprovação de cada aluno.

## Requisitos Não Funcionais

1. **Desempenho**:
   - O sistema deve ser capaz de processar turmas com até 100 alunos sem degradação de desempenho.

2. **Escalabilidade**:
   - O sistema deve ser escalável para suportar diferentes quantidades de alunos e turmas.

3. **Testes**:
   - O sistema deve possuir testes automatizados para garantir o funcionamento correto de cada módulo.

## Requisitos Técnicos

1. **Linguagem**: Python 3.x
2. **Bibliotecas**:
   - `unittest`: Para testes automatizados.
3. **Estrutura**: O projeto deve ser organizado com base em boas práticas de programação, utilizando estrutura modular (dividido em classes e funções).
4. **Controle de Versão**: O sistema deve ser versionado no Git, com commits claros e bem documentados.
5. **Documentação**:
   - O sistema deve ter documentação clara, incluindo README e instruções de uso.

## Como Rodar

1. Instalar as dependências:

```bash
pip install -r requirements.txt


