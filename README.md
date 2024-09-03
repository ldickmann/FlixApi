<div align="center">
<h1>FlixAPI - Desenvolvido por Lucas E. Dickmann</h1>
</div>

**API para gerenciamento de filmes, atores, gêneros e avaliações.**

Este projeto é uma API RESTful construída com Django Rest Framework para fornecer funcionalidades de gerenciamento de filmes, atores, gêneros e avaliações. A API permite realizar operações como criar, listar, atualizar e excluir registros de filmes, atores, gêneros e avaliações.

### Recursos

* **Filmes:**
    * Criar novos filmes com título, gênero, data de lançamento, atores e resumo.
    * Listar todos os filmes ou buscar por título.
    * Atualizar informações de filmes existentes.
    * Excluir filmes.
* **Atores:**
    * Criar novos atores com nome, data de nascimento e nacionalidade.
    * Listar todos os atores ou buscar por nome.
    * Atualizar informações de atores existentes.
    * Excluir atores.
* **Gêneros:**
    * Criar novos gêneros.
    * Listar todos os gêneros.
    * Atualizar gêneros existentes
    * Excluir gêneros.
* **Avaliações (Reviews):**
    * Criar novas avaliações para filmes, com nota e comentário.
    * Listar todas as avaliações de um filme específico
    * Atualizar avaliações existentes.
    * Excluir avaliações.

### Tecnologias Utilizadas

* **Django:** Framework web Python de alto nível.
* **Django Rest Framework:** Toolkit poderoso para construir APIs RESTful.
* **Python:** Linguagem de programação principal.
* **SQLite:** Banco de dados relacional leve (utilizado para desenvolvimento).
* **Outras bibliotecas:** Consulte o arquivo `requirements.txt` para obter a lista completa de dependências.

### Como Executar o Projeto

A API estará disponível em `https://ldickmann.pythonanywhere.com/api/v1/`.

### Endpoints da API

* **Filmes:**
    * `GET /api/v1/movies/`: Lista todos os filmes.
    * `POST /api/v1/movies/`: Cria um novo filme.
    * `GET /api/v1/movies/<id>/`: Recupera detalhes de um filme específico.
    * `PUT /api/v1/movies/<id>/`: Atualiza um filme existente.
    * `DELETE /api/v1/movies/<id>/`: Exclui um filme.
* **Atores:**
    * `GET /api/v1/actors/`: Lista todos os atores.
    * `POST /api/v1/actors/`: Cria um novo ator.
    * `GET /api/v1/actors/<id>/`: Recupera detalhes de um ator específico.
    * `PUT /api/v1/actors/<id>/`: Atualiza um ator existente.
    * `DELETE /api/v1/actors/<id>/`: Exclui um ator.
* **Gêneros:**
    * `GET /api/v1/genres/`: Lista todos os gêneros
    * `POST /api/v1/genres/`: Cria um novo gênero
    * `PUT /api/v1/genres/<id>/`: Atualiza um gênero existente
    * `DELETE /api/v1/genres/<id>/`: Exclui um gênero
* **Avaliações (Reviews):**
    * `GET /api/v1/movies/<movie_id>/reviews/`: Lista todas as avaliações de um filme específico
    * `POST /api/v1/movies/<movie_id>/reviews/`: Cria uma nova avaliação para um filme
    * `PUT /api/v1/reviews/<id>/`: Atualiza uma avaliação existente
    * `DELETE /api/v1/reviews/<id>/`: Exclui uma avaliação

**Observações:**

* Substitua `seu-usuario` pelo seu nome de usuário do GitHub.
* Para produção, considere usar um banco de dados mais robusto como PostgreSQL ou MySQL.
* Adicione autenticação e autorização para proteger seus endpoints, se necessário.
* Documente detalhadamente cada endpoint, incluindo os parâmetros esperados e as respostas possíveis.

## Capturas de tela do Postman

<div align="center">
<h3>Lista de Atores</h3>  
<table border=0 style="border: 1.2px solid #c6c6c6 !important; border-spacing: 2px; width: auto !important;">
<div align=center><img src="https://github.com/user-attachments/assets/72ef8380-62ba-461c-b4cd-5beeba81d62f" alt="lista de atores" style="margin: 0 !important; height: 400px !important;">
</div></table></div>

<div align="center">
<h3>Lista de Gêneros</h3>  
<table border=0 style="border: 1.2px solid #c6c6c6 !important; border-spacing: 2px; width: auto !important;">
<div align=center><img src="https://github.com/user-attachments/assets/a42204f9-8e96-4154-8a47-ce75f2433c14" alt="lista de gêneros" style="margin: 0 !important; height: 400px !important;">
</div></table></div>

<div align="center">
<h3>Lista de Filmes</h3>  
<table border=0 style="border: 1.2px solid #c6c6c6 !important; border-spacing: 2px; width: auto !important;">
<div align=center><img src="https://github.com/user-attachments/assets/5e3e836d-63ee-4bbd-b0a5-ecd47a5cbb15" alt="lista de filmes" style="margin: 0 !important; height: 400px !important;">
</div></table></div>

**Contribuições:**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

**Contato:**

Em caso de dúvidas ou sugestões, entre em contato pelo email [[ldickmann12@gmail.com]].

## Desenvolvido por Lucas E. Dickmann, no decorrer do curso Django Master.
