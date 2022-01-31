Test Serverless WSGI/ASGI Locally
=================================
An example of testing a serverless WSGI/ASGI APIs locally.

Motivation
----------
I decided to create this mini project as an example of how you can locally test 
your serverless Python API built on top of a WSGI/ASGI architecture 
using the main web frameworks on the market. The aim is to simulate 
the production environment (AWS Lambda machine) before deploying the application, 
without having to use a server (uvicorn/gunicorn) as a dev dependency, 
all this taking advantage of the facilities and practicalities of a web framework.

About the application
*************
The emulation of the AWS Lambda machine is done by the `Serverless Framework <https://www.serverless.com/>`_, 
the adaptation of the WSGI/ASGI application to AWS Lambda and API Gateway 
is done by `Mangum <https://mangum.io/>`_ and the communication of these two tools is done through a ``.yml`` file, e.g.:

.. code-block:: yml

        functions:
          githubAPI:
            handler: serverless_wsgi.wsgi.handler  # serverless_wsgi/wsgi.py -> handler = Mangum(app=app)
            events:
              - httpApi: ANY /
              - httpApi: 'ANY /{proxy+}'
              
You can see more details in the ``serverless.yml`` file.

Mangum wraps the WSGI/ASGI application, becoming the main handler for AWS Lambda, and then handles all application routes (see more info on the docs).

For this example i'll use `FastAPI <https://fastapi.tiangolo.com/>`_ as the web framework.

How it works?
*************
Requirements:

- Python = "^3.8"
- `Poetry <https://python-poetry.org/>`_ (or whatever package manager you prefer)
- Node.js and npm (stable versions)

First clone this repository and enter the project root folder, then run the following commands:

creating and activating an venv

.. code-block:: sh

        poetry shell
        
installing dependencies

.. code-block:: sh

        poetry install
        
installing node dependencies

.. code-block:: sh

        npm i
        npx sls plugin install -n serverless-python-requirements
        
run the API

.. code-block:: sh

        npx sls offline
        
At this point you can go to `http://0.0.0.0:4000/serverless-wsgi/docs` where you will have access to the Swagger UI and then you can test the API routes.
