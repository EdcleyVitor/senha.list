# senha.list

## 📌 Sobre o projeto

Este projeto surgiu durante uma situação prática em um **laboratório de informática escolar**, enquanto eram realizadas tarefas de manutenção em computadores com **Windows** (formatação, limpeza e otimização de máquinas que estavam lentas).

Durante esse processo surgiu um problema: **não havia acesso ao usuário administrador** de alguns computadores.

A primeira tentativa foi utilizar ferramentas de recuperação de sistema, como **Hiren’s Boot**, para criar ou recuperar um usuário administrador. Porém, essa abordagem não funcionou como esperado.

Observando o uso dos computadores no laboratório, surgiu uma hipótese de que a senha poderia seguir um **padrão relacionado ao próprio laboratório**, com palavras como:

* `SALAINFORMATICA`
* `SALADEINFORMATICA`
* `LABORATORIOINFORMATICA`
* `LABORATORIODEINFORMATICA`

A partir dessa ideia nasceu este pequeno projeto.

---

# ⚙️ O que o script faz

O script gera **todas as combinações possíveis de senha** a partir de palavras base, aplicando substituições comuns usadas em senhas (estilo *leet*), como:

| Letra | Substituição |
| ----- | ------------ |
| A     | 4            |
| E     | 3            |
| I     | 1            |
| O     | 0            |
| T     | 7            |
| D     | 3            |

Exemplo:

```
SALAINFORMATICA
S4L41NF0RM4T1C4
SAL41NF0RMAT1CA
```

O programa então gera **todas as variações possíveis** dessas substituições.

---

# 🔧 Funcionalidades

O script permite:

* escolher uma **palavra base**
* gerar **variações com substituições numéricas**
* gerar versões **apenas com vogais substituídas**
* **visualizar todas as combinações**
* **salvar todas as senhas em um arquivo `.txt`**

---

# 💻 Exemplo de uso

Ao executar o script:

```
--- GERADOR DE SENHAS ---

SALVAR EM ARQUIVO? (SIM para salvar / ENTER para apenas ver):

Opções disponíveis:
[15] ou [A] para SALAINFORMATICA
[17] ou [B] para SALADEINFORMATICA
[21] ou [C] para LABORATORIOINFORMATICA
[23] ou [D] para LABORATORIODEINFORMATICA
```

O usuário escolhe uma palavra base e o programa gera todas as combinações possíveis.

Exemplo de saída:

```
0001-- SALAINFORMATICA
0002-- S4LAINFORMATICA
0003-- SAL41NFORMATICA
0004-- S4L41NFORMATICA
...
```

---

# 🧠 Conceitos usados

O projeto utiliza:

* `itertools.product()` para gerar combinações
* manipulação de strings em Python
* geração de listas de variações
* escrita de arquivos `.txt`
* lógica de substituição de caracteres

---

# 📂 Estrutura

```
senha.list/
 ├─ gerador.py
 └─ README.md
```

---

# ⚠️ Aviso

Este projeto foi criado **apenas para fins educacionais**, com objetivo de estudar:

* lógica de programação
* geração de combinações
* automação com Python
* padrões comuns em criação de senhas

Não deve ser utilizado para acessar sistemas sem autorização.

---

# 🚀 Possíveis melhorias

Ideias para evolução do projeto:

* adicionar **mais padrões de substituição**
* permitir **entrada de qualquer palavra**
* exportar para **wordlists maiores**
* gerar **estatísticas de combinações**
