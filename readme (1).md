# 🗂️ Gerenciador de Tarefas

Uma aplicação de terminal simples desenvolvida em **Python** para **cadastrar**, **listar** e **remover** tarefas, com persistência em arquivo **JSON**. Ideal para praticar manipulação de arquivos, listas/dicionários, funções e tratamento de exceções em Python.

---

## 🧩 Situação-Problema

Em ambientes de trabalho e estudo, tarefas e prazos podem se acumular rapidamente. Nem sempre é desejável ou possível utilizar aplicações web ou mobile pesadas — às vezes precisamos de uma ferramenta leve, executável pelo terminal, que funcione offline e salve os dados localmente. O **Gerenciador de Tarefas** foi criado para suprir essa necessidade: um utilitário rápido que permite registrar compromissos, visualizá-los e removê-los, garantindo a persistência em disco e comportamento robusto frente a erros.

---

## 🎯 Objetivo

Construir um aplicativo de linha de comando (CLI) em **Python** que permita:

- Cadastrar novas tarefas;
- Listar tarefas salvas;
- Remover tarefas;
- Persistir dados em um arquivo **tarefas.json**;
- Tratar exceções (erros) para evitar falhas durante a execução.

---

## 🧾 Funcionalidades principais

- **Listar tarefas:** Exibe todas as tarefas registradas com ID, descrição e status.  
- **Adicionar tarefa:** Permite inserir uma nova tarefa; o sistema atribui um ID único automaticamente.  
- **Remover tarefa:** Exclui uma tarefa com base no ID informado pelo usuário.  
- **Persistência:** Armazena e carrega tarefas de um arquivo JSON local.  
- **Tratamento de exceções:** Mensagens amigáveis para entradas inválidas e problemas com o arquivo JSON.

---

## 💬 Fluxo de interação (descrito)

Ao rodar o programa, o usuário encontra um menu com opções numeradas. Selecionando “Adicionar tarefa” é solicitado que digite a descrição; ao confirmar, a tarefa é adicionada. Em “Listar tarefas” o programa imprime todas as tarefas armazenadas; em “Remover tarefa”, o usuário informa o ID da tarefa a ser excluída, o programa valida a entrada e, se existir, remove e atualiza o arquivo JSON. Erros de digitação, IDs inexistentes e problemas de leitura/escrita do arquivo são tratados com mensagens claras para o usuário.

---

## 💻 Como executar

**Pré-requisitos:** Python 3.8+ (não há dependências externas obrigatórias)

1. Clone o repositório ou baixe os arquivos:
```bash
git clone https://github.com/SEU_USUARIO/seu_repositorio.git
cd seu_repositorio
```

2. Certifique-se de que tarefas.json exista no diretório do projeto. Você pode criar um com o formato mostrado abaixo:

```bash
{
    "tarefas": [
        "Lavar o carro",
        "Colocar o lixo para fora"
    ],
    "datas": [
        "21/10",
        "16/10"
    ]
}
```

3. Execute o programa:
```bash
python gerenciador_de_tarefas_V2.py
```

---

