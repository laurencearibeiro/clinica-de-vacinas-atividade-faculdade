# 🏥 Sistema de Atendimento de uma Clínica de Vacinas (CLI em Python)

Projeto acadêmico em Python para gerenciar **cadastro de pacientes**, **fila de vacinação (FIFO)** e **histórico de vacinados (LIFO)** via terminal. O objetivo é praticar **funções**, **estruturas de dados** e **algoritmos de ordenação**.

> Arquivo principal sugerido: `clinicadevacina.py`

---

## 🔧 Requisitos

* **Python 3.10+** (usa `match-case`)
* Sem dependências externas

---

## ▶️ Como executar

```bash
python clinicadevacina.py
```

---

## 📋 Funcionalidades (menu)

1. **Cadastrar paciente** – valida nome e código (não permite vazio; código precisa ser numérico).
2. **Adicionar paciente na fila** – procura por código no cadastro e adiciona na **fila de vacinação**.
3. **Chamar próximo** – retira o primeiro da fila (FIFO) e adiciona no **histórico de vacinados**.
4. **Ver fila de espera** – lista os pacientes aguardando.
5. **Ver histórico** – mostra os pacientes que já foram vacinados (último vacinado aparece primeiro).
6. **Buscar paciente cadastrado** – consulta por código e exibe o nome.
7. **Listar pacientes ordenados** – ordena por **Nome** ou **Código** usando **Selection Sort** (implementação manual para fins didáticos).
8. **Sair** – encerra o programa.

---

## 🧠 Estruturas de dados

* `pacientes: list[list[str, int]]` – lista de pacientes cadastrados no formato `[nome, codigo]`.
* `fila_vacinacao: list` – fila (FIFO) representada por lista; usa `append` e `pop(0)`.
* `historico_vacinados: list` – pilha (LIFO) representada por lista; usa `append` e exibição com `reversed`.

---

## 🗂️ Organização do código (principais funções)

* `menu()` – exibe o menu principal.
* `cadastrar_pacientes()` – valida e cadastra `[nome, codigo]` em `pacientes`.
* `buscar_paciente(codigo)` – retorna o registro pelo código ou `None`.
* `adicionar_na_fila()` – adiciona o paciente existente em `fila_vacinacao`.
* `chamar_proximo()` – aplica a lógica FIFO e move para `historico_vacinados`.
* `ver_fila()` – exibe a fila atual.
* `ver_historico()` – exibe o histórico (ordem inversa, tipo pilha).
* `buscar_paciente_cadastro()` – busca interativa por código.
* `listar_pacientes_ordenados()` – **Selection Sort** por Nome **ou** Código.

---

## 🧪 Exemplo de sessão

```text
==== Clínica de Vacinas ====
1 - Cadastrar paciente
2 - Adicionar paciente na fila de vacinação
3 - Chamar próximo paciente para vacinação
4 - Ver fila de espera
5 - Ver histórico de pacientes vacinados
6 - Buscar paciente cadastrado
7 - Listar pacientes cadastrados ordenados
8 - Sair
Escolhe uma opção: 1
Digite o nome do paciente: Ana Silva
Digite o código do paciente: 101
Paciente cadastrado com sucesso! Nome: ANA SILVA | Código: 101

Escolhe uma opção: 2
Digite o código do paciente para adicionar na fila: 101
Paciente adicionado na fila de vacinação.

Escolhe uma opção: 3
Chamando paciente para vacinação: Ana Silva

Escolhe uma opção: 5
Histórico de pacientes vacinados:
- Ana Silva (Código: 101)
```

---

## ✅ Validações implementadas

* **Obrigatoriedade** de `nome` e `código` no cadastro.
* **Código numérico** (conversão para `int`).
* Busca de paciente **somente por código**.

---

## 📚 Conceitos praticados

* Funções e escopo.
* Estruturas lineares: **lista**, **fila (FIFO)** e **pilha (LIFO)**.
* Algoritmo de ordenação **Selection Sort** (implementação manual para fins didáticos).
* Controle de fluxo com `match-case` (Python 3.10+).

---

## 🧭 Decisões de design

* **Listas simples** para manter o foco nos conceitos básicos (sem classes/OO).
* **Fila com `pop(0)`** pela simplicidade (adequada a pequenos volumes neste contexto didático).
* **Histórico como pilha** para facilitar a visualização do último vacinado primeiro.

## 🧾 Licença

Defina uma licença para o repositório (ex.: **MIT**). Se nada for definido, o padrão do G
