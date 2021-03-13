# Blog - 30 dias de Flask (Primeiro desafio)

[30 Dias de Flask DEV Zone](https://github.com/DEV-Zone-BR/30-Dias-de-Flask)

## Features

* Conta
    * Registrar com confirmação de e-mail
    * Entrar
    * Sair
    * Recuperar senha por email
    * Deletar conta
* Postagem
    * Criar postagem
    * Listar postagem com paginação
    * Ler postagem
    * Gostar || Não gostar
    * Tags - Categorias
* Comentar em
    * Postagem
    * Comentários
* Perfil
    * Inserir informações pessoais com bio
    * Mudar informações pessoais
    * Seguir outros perfis


# Como executar

## Configurações
* crie um arquivo `.env`, para configurar o ambiente qu será utilizado 
  ```shell
  echo "FLASK_ENV=development" > .env
  ```

* Crie um arquivo `.secrets.toml`, para colocar chaves privadas
  ```shell
  touch .secrets.toml
  ```