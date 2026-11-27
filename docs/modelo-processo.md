# Modelo de dados: Processo

| Campo | Tipo | Obrigatório | Regras |
|---|---|---|---|
| numero_cnj | texto | sim | formato NNNNNNN-DD.AAAA.J.TR.OOOO, único, Resolução CNJ nº 65/2008 para o DD que calcula dígito verificador válido |
| vara | texto | não |  |
| area | enum | sim | CIVEL, TRABALHISTA, PREVIDENCIARIO, TRIBUTARIO, CONSUMIDOR, FAMILIA, SUCESSOES, BANCARIO, EMPRESARIAL; selecionar área principal |
| escritorio_defende | enum | sim | ATIVO, PASSIVO, TERCEIRO |
| foro | texto | sim | |
| assunto | texto | sim | |
| valor_da_causa | decimal | sim | Pode ser zero ou maior que zero, não negativo, duas casas decimais |
| data_da_distribuicao | data | sim |  |
| data_da_criacao | data_hora | sim | gerado pelo sistema |
| data_de_alteracao | data_hora | sim | gerado pelo sistema |
| segredo_de_justica | booleano | sim | padrão=True -> secure by default |
| status | enum | sim | EM_ANDAMENTO, EXTINTO, ARQUIVADO, SUSPENSO |
| fase | enum | sim | CONHECIMENTO, RECURSAL, CUMPRIMENTO_SENTENCA |
| id | uuid | sim | gerado pelo sistema, único |
| juiz | texto | não | |
| classe | texto | não | |


## Entidades futuras

### Cliente

| Campo | Tipo | Obrigatório | Regras |
|---|---|---|---|
| id | uuid | sim | gerado pelo sistema |
| nome | texto | sim | |
| cpf_cnpj | texto | sim | regra para verificar se o cpf/cnpj são válidos, criptografia no banco, mascaramento na tela e acesso ao número completo só para quem precisa, único |


### Endereço
| Campo | Tipo | Obrigatório | Regras |
|---|---|---|---|
| id | uuid | sim | gerado pelo sistema |
| rua | texto | sim |  |
| numero | texto | sim | |
| bairro | texto | sim | |
| complemento | texto | não | |
| cidade | texto | sim | |
| estado | enum | sim | AC, AM, AP, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN, SE, DF, GO, MT, MS, ES, MG, RJ, SP, PR, RS, SC |
| cep | texto | sim | deve ter 8 caracteres, retirar o traço |
| cliente_id | uuid | sim | |


### Telefone
| Campo | Tipo | Obrigatório | Regras |
|---|---|---|---|
| id | uuid | sim | gerado pelo sistema |
| ddd | texto | sim | deve ter 2 caracteres |
| numero | texto | sim | se telefone fixo, 8 caracteres, se celular, 9 caracteres, retirar o traço |
| tipo | enum | sim | CELULAR, RESIDENCIAL, COMERCIAL |
| cliente_id | uuid | sim | |


### Email
| Campo | Tipo | Obrigatório | Regras |
|---|---|---|---|
| id | uuid | sim | gerado pelo sistema |
| email | texto | sim | formato de e-mail válido |
| tipo | enum | não | PESSOAL, COMERCIAL |
| cliente_id | uuid | sim | |


### Partes
Essa tabela conterá as possíveis partes do processo

***Campos a definir***


### Documentos
Essa tabela conterá documentos relativos ao processo e ao cliente. Pode ser decisões, documentos pessoais, documentos jurídicos.

***Campos a definir***


### Movimentação
Essa tabela poderá armazenar movimentações, evitando abrir o processo para saber os andamentos.

***Campos a definir***
