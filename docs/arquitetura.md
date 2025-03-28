# Arquitetura do Sistema de Cadastro de Alunos

## Visão Geral

O sistema de cadastro de alunos foi desenvolvido com o objetivo de gerenciar informações de alunos em turmas de maneira simples e eficiente. A arquitetura foi pensada para ser modular, com as principais funcionalidades divididas em classes, e com testes automatizados para garantir o correto funcionamento do sistema.

## Estrutura do Projeto

A estrutura do sistema está organizada da seguinte maneira:

### **Modelos (Classes)**

- **Aluno**:
  - Representa um aluno com as informações essenciais como nome, matrícula, notas e status de aprovação.
  - A classe possui métodos para:
    - Atribuir notas.
    - Verificar se o aluno foi aprovado ou reprovado.
  
- **Turma**:
  - Representa uma turma contendo vários alunos.
  - A classe possui métodos para:
    - Adicionar alunos à turma.
    - Listar todos os alunos da turma.
    - Calcular a média da turma.
    - Verificar se a turma atingiu o número máximo de alunos.

### **Testes**

Os testes são realizados utilizando a biblioteca `unittest`, garantindo a integridade das funcionalidades e a conformidade com os requisitos.

- **Testes para a classe `Aluno`**:
  - Teste de atribuição de notas.
  - Teste para verificação da aprovação ou reprovação do aluno.
  
- **Testes para a classe `Turma`**:
  - Teste de adição de alunos à turma.
  - Teste de cálculo da média da turma.
  - Teste de listagem de alunos na turma.

### Fluxo de Execução

1. O **usuário** cria alunos e os adiciona a uma turma.
2. O **sistema** calcula a média das notas dos alunos.
3. O **sistema** retorna se o aluno foi aprovado ou reprovado.
4. O **sistema** gera um relatório de alunos por turma.
