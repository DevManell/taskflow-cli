# TaskFlow CLI

**Autor:** Emmanuel Avelino Lima Barreto

## 📌 Sobre o Projeto
O TaskFlow CLI é uma aplicação de linha de comando desenvolvida em Python para auxiliar na organização de tarefas do dia a dia de forma simples, rápida e eficiente.

---

## 🎯 Problema
Muitas pessoas enfrentam dificuldades para organizar suas tarefas diárias, o que pode impactar diretamente na produtividade, no cumprimento de prazos e até no bem-estar.

---

## 💡 Solução
O TaskFlow CLI oferece uma forma prática de gerenciar tarefas diretamente pelo terminal, permitindo ao usuário:

- Adicionar novas tarefas
- Listar tarefas existentes
- Remover tarefas concluídas

---

## 👥 Público-Alvo
- Estudantes
- Profissionais
- Pessoas que desejam melhorar sua organização pessoal

---

## ⚙️ Tecnologias Utilizadas
- Python
- Pytest (testes automatizados)
- Ruff (análise de código / lint)
- Git & GitHub
- GitHub Actions (CI)

---

## ✅ Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Remover tarefas
- Armazenamento em arquivo JSON

---

## 🚀 Como Executar o Projeto

Para executar o projeto, siga os passos abaixo:

### 1. Clonar o repositório

git clone https://github.com/DevManell/taskflow-cli
cd taskflow-cli

### 2. Instalar as dependências
python -m pip install -r requirements.txt

### 3. Executar a aplicação
python run.py

## 🖼️ Exemplo de Uso

Abaixo um exemplo do sistema em funcionamento:

![Execução do sistema](img/Captura%20de%20tela%202026-04-10%20191013.png)

---

## 📈 Atualizações da Entrega Intermediária

Nesta nova etapa do projeto foram adicionadas melhorias importantes para tornar o sistema mais completo e profissional.

### ✨ Novidades

- Integração com API pública
- Exibição de frases motivacionais
- Testes de integração com Pytest
- Workflow automatizado com GitHub Actions
- Melhor organização do projeto
- Validação automática a cada push no GitHub

---

## 🌐 API Pública Utilizada

O sistema agora utiliza a API pública ZenQuotes para exibir mensagens motivacionais diretamente no terminal.

https://zenquotes.io/

---

## 🖼️ Nova Versão do Sistema

Exemplo da nova funcionalidade de frases motivacionais:

![Nova versão do sistema](img/Captura%20de%20tela%202026-05-15%20195056.png)

---

## 🧪 Testes Automatizados

Para executar os testes do projeto:

```bash
python -m pytest
```

---

## 🔄 Integração Contínua

O projeto utiliza GitHub Actions para executar automaticamente:

- Testes automatizados
- Verificação das dependências
- Validação do sistema em ambiente Linux