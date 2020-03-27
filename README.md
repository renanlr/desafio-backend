# Desafio Backend tembici.

## Descrição
Nesta API temos:
- Antenticação de usuário no padrão JWT (Não precisa dos endpoints para criar o usuário, mas somente o endpoint que recebe o email e senha do usuário e já faça a sua autenticação na API)
- Endpoint para listar as últimas viagens do usuário logado
- Endpoint para enviar a classificação da viagem e a sua nota

## Instalação
### Pré-requisitos:
 Ambiente virtual configurado com Python 3.5

### Passo a passo
1) Entre no ambiente virtual
2) clone o projeto `git clone https://github.com/renanlr/desafio-backend.git`
3) Entre na pasta do projeto `cd desafio-backend/`
4) Execute o comando `pip install -r requirements.txt`
5) Execute o comando `python manage.py migrate` 
6) Execute o comando `python manage.py runserver`
7) Após isso a api estará em execução no endereço http://127.0.0.1:8000/
8) Para criar um usuário utilize o comando `python manage.py createsuperuser`

## Documentação de URL's
Acessar o link http://127.0.0.1:8000/swagger/
