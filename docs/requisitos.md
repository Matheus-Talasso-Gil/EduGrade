#  Documento de Requisitos e User Stories

##  User Stories (Histórias de Utilizador)

1. **Como** professor, **eu quero** cadastrar alunos com nome, disciplina e frequência **para** ter o registo inicial no sistema.
2. **Como** professor, **eu quero** lançar 3 notas por aluno **para** avaliar o seu desempenho.
3. **Como** professor, **eu quero** que o sistema calcule a média e o status automaticamente **para** evitar erros manuais.
4. **Como** coordenador, **eu quero** consultar o boletim individual de um aluno **para** dar feedback aos encarregados de educação.
5. **Como** coordenador, **eu quero** listar todos os alunos cadastrados **para** acompanhar o panorama da turma.

---

##  Requisitos Funcionais (RF)

| ID | Descrição |
| :--- | :--- |
| **RF01** | O sistema deve permitir o cadastro de alunos (Nome, Disciplina, Presença em %). |
| **RF02** | O sistema deve permitir a inserção de 3 notas por aluno. |
| **RF03** | O sistema deve calcular automaticamente a média aritmética simples das 3 notas. |
| **RF04** | O sistema deve determinar a situação do aluno com base nas regras de negócio. |
| **RF05** | O sistema deve permitir listar todos os alunos e pesquisar boletins individuais por nome. |

---

##  Regras de Negócio (RN)

- **RN01 - Frequência Mínima:** Se a presença for inferior a **75%**, o aluno é automaticamente **Reprovado por Faltas**, independentemente das notas obtidas.
- **RN02 - Critérios de Aprovação por Nota (com Frequência >= 75%):**
  - **Média >= 7.0:** Aprovado.
  - **5.0 <= Média < 7.0:** Recuperação.
  - **Média < 5.0:** Reprovado por Nota.
- **RN03 - Validação de Dados:** 
  - As notas devem estar estritamente no intervalo de `0.0` a `10.0`.
  - A frequência deve estar estritamente no intervalo de `0.0%` a `100.0%`.

---

##  Requisitos Não Funcionais (RNF)

- **RNF01 - Interface CLI:** O sistema deve ter uma navegação baseada em menus numéricos claros no terminal.
- **RNF02 - Tratamento de Exceções:** O sistema deve tratar entradas inválidas (ex.: letras em campos numéricos) sem interromper a execução do programa (`try/except`).