# DjangoFlix API

<br>

### 📝 Índice
* [Descrição](#-descrição)
* [Funcionalidades](#-funcionalidades)
* [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
* [Instalação e Execução](#️-instalação-e-execução)
* [Como Utilizar](#-como-utilizar)

<br>

## 📖 Descrição
__Este projeto__ é uma API RESTful de backend, desenhada para servir como a espinha dorsal de uma aplicação de catálogo de filmes, como um serviço de streaming ou uma base de dados de cinema (similar ao IMDb).

* __Qual problema este projeto resolve?__
  Ele resolve a necessidade de um backend centralizado, robusto e escalável para aplicações que dependem de dados complexos e relacionados (filmes, atores, gêneros, avaliações). Ele fornece uma interface limpa e documentada para que equipes de frontend (web ou mobile) possam construir a experiência do utilizador sem se preocuparem com a lógica de negócio do lado do servidor.
  <br>

* __Qual é o seu objetivo principal?__
  O objetivo é fornecer uma API de alta performance, segura e fácil de consumir. Para os desenvolvedores de frontend, oferece endpoints previsíveis e bem documentados. Para os administradores de conteúdo, oferece uma interface administrativa poderosa (Django Admin) para gerir todo o catálogo de forma intuitiva.
  <br>

* __Para quem este projeto é destinado?__
  1. __Desenvolvedores de Frontend/Mobile__: O público que irá consumir os dados da API para construir a aplicação visível para o utilizador final.
  2. __Administradores de Conteúdo__: Utilizadores internos que irão gerir o catálogo de filmes, atores e géneros através do Django Admin.
  <br>


## ✨ Funcionalidades

Este projeto implementa funcionalidades robustas, seguindo as melhores práticas de desenvolvimento de APIs.

__Backend e Lógica da API__

* __Gestão de Catálogo Completa (CRUD)__: Operações para Criar, Ler, Atualizar e Apagar Filmes, Atores e Géneros.

* __Sistema de Avaliações Avançado__: Utilizadores autenticados podem submeter avaliações (nota e comentário). A lógica de negócio impede que o mesmo utilizador avalie o mesmo filme mais de uma vez.

* __Segurança e Permissões__:

  * __Autenticação com JWT__: Sistema de autenticação stateless e seguro com djangorestframework-simplejwt.

  * __Permissões por Modelo__: Utiliza o sistema DjangoModelPermissions para garantir que apenas utilizadores com as permissões corretas (ex: add_movie) possam realizar ações de escrita.

  * __Permissões por Objeto__: Apenas o autor de uma avaliação pode editá-la ou apagá-la.

* __Endpoint de Estatísticas Agregadas__: Um endpoint (/movies/stats/) que fornece dados calculados em tempo real, como o número total de filmes, contagem de filmes por género e a média geral de todas as avaliações.

* __Performance Otimizada__: As queries da base de dados são otimizadas com select_related e prefetch_related para evitar o problema de queries N+1, garantindo respostas rápidas mesmo com grandes volumes de dados.
<br>

__Arquitetura & DevOps__

* __Estrutura de Projeto Limpa__: O projeto segue uma arquitetura modular com o código-fonte em /core para configurações do projeto e /apps com as aplicações separadas por responsabilidade (actors, genres, movies, etc.).

* __Ambiente 100% Containerizado__: A aplicação e todos os seus serviços (Django, PostgreSQL, Nginx e Traefik) são geridos com Docker e Docker Compose, garantindo um ambiente de desenvolvimento consistente e pronto para deploy.

* __Serviços de Produção__: Utiliza Traefik como proxy reverso e load balancer, Nginx como servidor web, Gunicorn como servidor de aplicação WSGI e Whitenoise como servidor de arquivos estáticos (Django admin, por exemplo).

* __Configuração Segura__: Usa variáveis de ambiente (através de ficheiros .env) para gerir segredos como chaves de API e passwords.

* __Documentação Automática da API__: Integração com drf-spectacular para gerar uma documentação interativa com Swagger UI, que serve como um contrato vivo para os consumidores da API.
<br>

## 🛠️ Tecnologias Utilizadas
As principais tecnologias, frameworks e ferramentas utilizadas na construção deste projeto são:

* __Backend__:
Python 3.13+
Django 5.2+
Django REST Framework
Gunicorn (Servidor de Aplicação WSGI)
Whitenoise (Servidor de arquivos estáticos)
<br>

* __Base de Dados__:
PostgreSQL
<br>

* __Arquitetura & DevOps__:
Docker & Docker Compose (Containerização)
Nginx (Servidor Web)
Traefik (Proxy reverso e Load Balancer)
<br>

* __Bibliotecas Principais__:
djangorestframework-simplejwt (Autenticação JWT)
drf-spectacular (Geração de Schema OpenAPI/Swagger)
<br>

## ⚙️ Instalação e Execução
Siga este guia passo a passo para configurar e executar o projeto no seu ambiente local.

__Pré-requisitos__
Antes de começar, garanta que você tem as seguintes ferramentas instaladas na sua máquina:
* [Docker](https://www.docker.com/get-started)
* [Docker-Compose](https://docs.docker.com/compose/install/)

1. __Clone o repositório__
    ```sh
    git clone git@github.com:tperons/api-flix.git
    cd flix-api
    ```

2. __Configure as Variáveis de Ambiente__
    O projeto usa um ficheiro `.env` para gerir as configurações sensíveis. Crie uma cópia do ficheiro de exemplo:
    ```sh
    cp .envs/.local/.env.example .envs/.local/.env
    ```
    Agora, abra o ficheiro .env e preencha os valores para as variáveis.

3. __Construa as imagens Docker__
    ```sh
    docker compose -f docker-compose.local.yml build
    ```

4. __Inicie os serviços__
    ```sh
    docker compose -f docker-compose.local.yml up -d
    ```

5. __Configuração Inicial da Base de Dados__
    Com os containeres a funcionar, execute os seguintes comandos:

    * __Crie e aplique as migrações__:
    ```sh
    docker compose -f docker-compose.local.yml exec django python manage.py makemigrations

    docker compose -f docker-compose.local.yml exec django python manage.py migrate
    ```

    * __Crie um superutilizador para aceder ao Django Admin__:
    ```sh
    docker compose -f docker-compose.local.yml exec django python manage.py createsuperuser
    ```
<br>


## 🚀 Como Utilizar
Após a instalação, a sua API estará acessível e pronta para ser usada.

__Fluxo do Desenvolvedor (Consumidor da API)__
* __Acesse a Documentação__: A forma principal de interagir com a API é através da documentação Swagger em `http://localhost:8080/api/v1/schema/`. Lá, você pode ver todos os endpoints, os seus formatos de dados e executá-los diretamente.
* __Autenticação__:

    1. Para realizar ações de escrita (`POST`, `PUT`, `DELETE`), primeiro obtenha um token JWT fazendo um `POST` para `/api/v1/auth/token/` com o `username` e `password` de um utilizador.

    2. Nos pedidos seguintes, inclua o `access` token recebido no cabeçalho `Authorization` como `Bearer <token>`. O Swagger UI tem uma interface para "autorizar" os seus pedidos com o token.
<br>

__Fluxo do Administrador de Conteúdo__
* __Aceda ao Django Admin__: Navegue para `http://localhost:8080/admin/`.
* __Faça o Login__: Use as credenciais do superutilizador que você criou.
* __Gerir o Catálogo__: Utilize a interface para adicionar, editar e apagar Filmes, Atores e Géneros.
* __Gerir Utilizadores e Permissões__: Crie novos utilizadores e atribua-os a grupos com permissões específicas (ex: um grupo "Gestores de Conteúdo" que só pode adicionar filmes).
