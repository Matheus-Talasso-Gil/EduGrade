#  EduGrade - Sistema de Gestão Escolar (CLI)

O **EduGrade** é um sistema de linha de comando (CLI) desenvolvido em Python para automatizar o lançamento de notas, cálculo de médias e verificação de critérios de aprovação escolar. O projeto foi desenvolvido aplicando a metodologia ágil **Scrum** e gerido através de um quadro **Kanban**.

---

##  Funcionalidades

- **Cadastro de Alunos:** Registo de nome, disciplina e percentagem de frequência.
- **Lançamento de Notas:** Inserção de 3 notas com validação automática (0.0 a 10.0).
- **Cálculo Automático:** Cálculo da média aritmética simples.
- **Aplicação de Regras de Negócio:**
  - Reprovação por faltas (Frequência < 75%).
  - Aprovado (Média >= 7.0).
  - Recuperação (5.0 <= Média < 7.0).
  - Reprovado por Nota (Média < 5.0).
- **Consulta de Boletim:** Exibição detalhada por aluno ou listagem completa da turma.

---

##  Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Passo a Passo
1. Clona o repositório ou transfere o ficheiro do projeto:
   git clone [https://github.com/teu-usuario/edugrade.git](https://github.com/teu-usuario/edugrade.git)
   cd edugrade

2. Executa o ficheiro principal via terminal:
   python edugrade.py

---

##  Estrutura do Repositório

edugrade/
│
├── edugrade.py             # Código-fonte principal da aplicação CLI
├── README.md               # Apresentação do projeto e guia de uso
└── docs/
    ├── requisitos.md       # Documentação de User Stories, RF, RN e RNF
    ├── kanban.md           # Mapeamento do Backlog e acompanhamento das Sprints
    └── fluxo_cli.md        # Protótipo do fluxo de navegação no terminal

---

##  Tecnologias e Ferramentas

- **Linguagem:** Python 3
- **Gestão Ágil:** Kanban (Trello / GitHub Projects)
- **Prototipagem:** Fluxograma CLI (Mermaid / Figma)