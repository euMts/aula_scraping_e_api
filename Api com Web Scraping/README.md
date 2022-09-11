# API com Web Scraping

Este script utiliza web scraping para enviar o [formulário de contado do meu site](https://matheus-eduardo.com.br/contact).<br>
Para instalar os pacotes necessário rode o seguinte comando:<br>
`pip install -r requirements.txt`<br>

Documentação relacionada:<br>
- [Consumindo API](https://github.com/euMts/aula_scraping_e_api/tree/main/Consumindo%20API)<br>
- [Web Scraping](https://github.com/euMts/aula_scraping_e_api/tree/main/Web%20Scraping)<br>


## Rotas
### Checar status<br>
Método: **GET**<br>
```
/
```
Retorno:<br>
```
{
	"status":"Im alive!!! 🚀", 
	"datetime": "2022-09-11 00:48:14.021304"
}
```
---
### Enviar novo formulário<br>
Método: **POST**<br>
```
/api/contact/
```
Requisição:<br>
```
{
	"name": "string",
	"email": "string",
	"message": "string"
}
```
Retorno:<br>
```
{
	"status" : "200",
	"message" : "We're working on it, your message can't be sent right now."
}
```
