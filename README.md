# Orders MVC JWT

Nesse desafio, é apresentado de forma prática, os conceitos sobre autenticação JWT, segurança e MVC apresentados durante a Formação Python da Rocketseat.

Trata-se de uma API de pedidos que utiliza JWT para autenticação e autorização.

A ideia desse desafio é desenvolver uma API de pedidos que utilize JWT para autenticação e autorização. A API deve ter diferentes endpoints que só podem ser acessados por usuários que tenham autenticação via token.

## Sobre o token JWT

Ao fazer login, o usuário recebe um token JWT que contém as seguintes informações:

- **ID do Usuário**: Identificador único do usuário na base de dados.
- **Nome de Usuário**: Nome do usuário para exibição.
- **Token JWT**: Token necessário para ser colocado na requisição.

## Sobre os endpoints

- [✓] Deve ser possível listar os pedidos do usuário autenticado
- [✓] Deve ser possível adicionar um novo pedido.
- [✓] Um usuário só pode ter acesso aos seus pedidos e não de outros.

## Sobre as tabelas no banco

- [✓] Os usuários devem possuir um id, o username e a senha que deverá ser armazenada.
- [✓] Os pedidos por sua vez, deve ter uma relação com os usuários, descrição, id e a data na qual o pedido foi criado no banco.

## Conceitos utilizados

- MVC
- JWT
- SQL
- Testes unitários
- Criação e integração com banco de dados SQLite