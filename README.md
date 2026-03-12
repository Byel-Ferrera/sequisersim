# Módulo Acadêmico
CRC Admin - Modulo Acadêmico
Projeto colaborativo desenvolvido em Python 3 / Javascript para uso interno do Centro de Recondicionamento de Computadores do Maranhão - CRC MA.

## Dependências
- Django==4.2.7
- django-widget-tweaks==1.5.0
- psycopg2==2.9.9

## Modelagem de dados

### Etapas para um projeto de modelagemn de dados

- Entender o problema - contextualização do problema - Perguntas sobre o funcionamento.

- MER - Criação do modelo de Entidade - Relacionamento - Atributos da entidade (Ex: Entidade professor).

- DER - Criação do diagrama de entidades - Relacionamentos.

- Cardinalidades - Forma como as entidades se relacionam.

- Definição de um modelo lógico (Criação do modelo no django).

- Normalização das tabelas - aplicação de regras de verificação.

- Dicionário de dados - Lógica para criação das tabelas, entidades, atributos e relacionamentos.

- Implementação do modelo físico - criação do banco de dados usando a linguagem SQL - aplicação de testes.

### Tabelas a serem criadas

- <b>Cadastro de Aluno</b><br>
  A tabela cadastro de aluno deve conter:
  - Nome
  - Sobrenome
  - CPF (Chave primária)
  - Data de Nascimento
  - Sexo
  - Etnia
  - E-mail
  - Telefone
  - Foto
  - Nacionalidade
  - Naturalidade
  - Nome social
  - Estado Civil
  - Endereço
  - Bairro
  - Cidade
  - Zona Residêncial (Urbana ou rural)
  - Deficiência (sim ou não) Qual?
  - Nível de ensino
  - Tipo de instituição (Pública ou privada)
- <b>Cadastro do Curso</b><br>
  A tabela cadastro do curso deve conter:
  - Nome
  - Descrição
  - Carga horária
  - Tipo
  - Data de criação
- <b>Cadastro de disciplina</b><br>
  A tabela cadastro da disciplina deve conter:
  - Nome (Chave primária)
  - Descrição
  - Carga horária
- <b>Cadastro de turma</b><br>
  A tabela cadastro da turma deve conter:
  - Numero da turma (Chave primária)
  - Turno
  - Inicio
  - Fim
  - Descrição
  - Curso (chave estrangeira para curso)
- <b>Avaliação do aluno - (Frequência >= 70% + avaliação pelo professor)</b><br>
  A tabela avaliação do aluno deve conter:
  - Aluno (chave estrangeira para aluno)
  - Turma (chave estrangeira para turma)
  - Disciplina (chave estrangeira para disciplina)
  - Atividade (chave estrangeira para atividades)
  - Data da atividade
  - Nota da atividade
- <b>Avaliação do curso</b><br>
  A tabela avaliação do curso deve conter:
  - Aluno (chave estrangeira para aluno)
  - Seção
  - Pergunta
  - Resposta
- <b>Cadastro da Frequência</b><br>
  A tabela frequência deve conter:
  - Aluno (chave estrangeira para aluno)
  - Turma (chave estrangeira para turma)
  - Disciplina (chave estrangeira para disciplina)
  - Data da frequência
  - Frequência
- <b>Atividades</b><br>
  A tabela atividades deve conter:
  - Atividade (Chave primária)
  - Descrição
- <b>Produção</b><br>
    A tabela Produção deve conter:
    - Professor (chave estrangeira para usuários, função professor)
    - Horas trabalhadas
    - Valor hora
    - Valor total
    - Data do pagamento
    - Situação do pagamento
    - Competência
- <b>Tabela matricula</b><br>
  A tabela matricula deve conter:
    - Aluno (chave estrangeira para aluno)
    - Turma (chave estrangeira para turma)
    - Data da matricula
    - Data do cancelamento
- <b>Tabela intermediária professor turma disciplina</b><br>
  A tabela intermediária professor turma disciplina deve conter:
  - Professor (chave estrangeira para usuários, função professor)
  - Turma (chave estrangeira para turma)
  - Disciplina (chave estrangeira para disciplina)
"# lsadm" 
