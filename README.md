# Desafio API Python

Este desafio é uma oportunidade para demonstrar sua experiência e habilidade criando um protótipo de serviço de notificação meteorológico.

## O que iremos revisar

Seu projeto será revisado pelo time de engenheiros e será levado em consideração seu nível de experiência.
Buscamos avaliar seu conjunto de habilidades e como você irá abordar a solução para o problema.

### Iremos avaliar as seguintes áreas:

-   **Arquitetura**. Como você decidiu estruturar seu projeto?
-   **Qualidade do código**. Você está seguindo boas práticas de codificação? Seu código é fácil de ler e manter? É testável?
-   **Escolhas técnicas**. Suas opções de bibliotecas, pacotes e ferramentas são apropriadas?
-   **Testes**. Há cobertura de teste adequada?

## Desafio

Criar um serviço capaz de monitorar e alertar usuários de que há chances de chuva em um período previamente cadastrado para determinada cidade. Exemplo, antes de sair para o trabalho, gostaria de ser avisado para levar meu guarda-chuvas.

- Crie serviços para gerenciar o cadastro de usuários e de seus respectivos dados para monitoramento.

- Implemente a integração com ao menos um provedor de informações meteorológicas.

- Crie uma interface entre o(s) serviço(s) meteorológico(s) e a classe onde será implementada a lógica. A substituição ou adição de um novo serviço meteorológico não deve causar refatoração do código implementado.

- Implemente a lógica para monitorar e notificar todos os usuários que devem ser avisados para não esquecerem seus guarda-chuvas.
> **ATENÇÃO**: Em uma versão completa do serviço, o resultado desta
> implementação resultaria no envio de uma mensagem para um servidor de
> mensageria, que posteriormente seria consumido por outra aplicação
> responsável apenas pelo envio das notificações. Neste desafio, não é
> necessário integrar com nenhum serviço de mensageria, apenas leve em
> consideração durante a codificação.

- Crie um método assíncrono para importar novos usuários a partir de um arquivo CSV (levar em consideração que o arquivo já exista na pasta /tmp por exemplo)

- Crie um método assíncrono para exportar todos os usuários da base de dados em um arquivo CSV (o arquivo pode ser salvo na pasta /tmp)

#### Para este projeto, indicamos um dos dois serviços de consulta meteorológica:

 - Yahoo Weather [https://developer.yahoo.com/weather/](https://developer.yahoo.com/weather/)
 - OpenWeatherMap [https://www.openweathermap.org/api](https://www.openweathermap.org/api)

## Dicas:

 - Uma pessoa pode residir em uma cidade, mas trabalhar em outra.
 - Leve em consideração o período cadastrado para monitorar. Um turno
   pode começar em um dia, mas terminar em outro.
 - Podem ser implementadas duas ou mais APIs de consulta meteorológica,
   porém deve-se ter um controle sob qual é a padrão e/ou a ordem de
   prioridade da consulta.

## Atenção:

 - A interpretação do desafio faz parte do desafio
 - Recomendamos o uso do Python 3
 - Desenvolver a API RESTful

## Entrega:

- Versionar o código em um repositório público no git e enviar o link por email.
- Você terá 2 dias para completar o desafio
