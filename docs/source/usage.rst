usage
===============

generate_data command
---------------------

This command allows you to generate data for your Django app and model using a single command.


To generate data for your Django app and model, use the following command:

.. code-block:: bash

   python manage.py generate_data [app_name] [model_name] number_of_records

- ``[app_name]`` (optional): Replace this with the name of your Django app for which you want to generate data. If not provided, data will be generated for all apps.
- ``[model_name]`` (optional): Replace this with the name of your Django model for which you want to generate data. If not provided, data will be generated for all models within the specified app.
- ``number_of_records`` (required): Replace this with the number of records you want to generate.

Examples
--------

- To generate 100 records for all apps and models, run:

  .. code-block:: bash

     python manage.py generate_data 100

- To generate 100 records for a specific app, run:

  .. code-block:: bash

     python manage.py generate_data myapp 100

- To generate 100 records for a specific app and model, run:

  .. code-block:: bash

     python manage.py generate_data myapp MyModel 100


Make sure you replace ``[app_name]``, ``[model_name]``, and ``number_of_records`` with the actual values you want to use.

If you need help or want to see a list of allowed arguments, use the following command:

  .. code-block:: bash
    python manage.py generate_data --help