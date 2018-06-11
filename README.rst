Como instalar
=============

Requisitos
----------

* virtualenv

* virtualenvwrapper

* Python 3.6

Passo-a-passo
-------------

1 - Crie um ambiente virtual com o python 3

.. code-block:: bash

    $ mkvirtualenv forecast --python=`which python3`

2 - Instale os requisitos

.. code-block:: bash

    $ pip install -r requirements.txt

3 - Copie o arquivo de configurações:

.. code-block:: bash

    $ cp forecast/config.cfg forecast/config.py


4 - Para executar a aplicação WEB execute o comando abaixo:

.. code-block:: bash

    $ python run.py

Vá em http://localhost:8080/api/ para ter acesso à documentação e ações 'ao
vivo' da API.

5 - Para exportar os dados para um arquivo CSV, é necessário exportar a
variável de ambiente FLASK_APP e em seguida executar o comando para exportar:

.. code-block:: bash

    $ export FLASK_APP=forecast
    $ flask export_csv [PATH]

Para ajuda digite:

.. code-block:: bash

    $ flask export_csv --help