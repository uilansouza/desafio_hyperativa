#Desafio Hyperia

## Itens Obrigatórios

- Ter instalado Docker
- Ter Instalado Postman/insomnia
- Ter git, para realizar o clone

#### Tarefas

Após ter instalado o docker, é necessário executar o comando:
`docker-compose up -d` para que suba os container

### Acessando Client do Mongodb
Acesse o endereço do banco de dados não relacional no endereço
`localhost:3000` e clique no botão ao lado esquerdo __connect__  e selecione a base *default*
Para acessar as collections criadas apenas clique na aba collections ao lado esquerdo da tela.

### Cadastro de um novo Usuario
Para Cadastrar um novo usuário, o endpoint é o seguinte `localhost:8888/register` é necessário passar o seguinte payload em uma requisição do tipo POST
```
{
	"username":"usuario"
	"password":"123456"
}
```
é retornado um `id:15489614478`

### Autenticação do usuário no sistema
Para se autenticar no sistema é necessário acessar o seguinte endpoint em uma requisição do tipo POST `localhost:8888/login`
A resposta será um token semelhante a esse abaixo
```
{
    "id": "lucas",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJsdWNhcyIsImV4cCI6MTYyMDcwNjY1OH0.MN6mZG54nWM8b1PYz0h7GZLrSwsxG4_Mej--CUvrz0k"
}
```
### Cadastro de um novo cartão
Para  cadastrar um novo cartão de  é necessário acessar o endpoint em uma requisição do tipo POST  ``localhost:8888/card`` 

É necessário passar o seguinte payload
```
{
	"card": "12345645897"
}
```
porem antes de realizar a requisição é necessário colocar o _token_ gerado no endpoint `localhost:8888/login`  no Header Autorization no tipo **Bearer Token** 

O endpoint retorna um Id de confirmação, caso tenha sucesso

### Consulta de cartão 
Para consultar um cartão, será necessário passar o numero do cartão em uma requisição do tipo GET para o endpoint `localhost:8888/card/<number_card>`  com o numero do cartão a ser consultado
Porem antes de realizar a requisição é necessário colocar o _token_ gerado no endpoint `localhost:8888/login`  no Header Autorization no tipo **Bearer Token** 
O endpoint retorna um Id e alguns caracteres do cartão, caso seja sucesso

__obs__: O número do cartão esta criptografado na base de dados, infelizmente tive alguns contratempos e não consegui enviar os  cartões via arquivos,
Esses seriam enviados   via envio de arquivos por um botão de upload em uma pagina web utilizando um template.
Quem sabe uma proxima vez.
Desculpe o atraso, espeo que gostem

