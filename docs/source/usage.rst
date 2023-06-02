Usage
=====

To use the custom command, run the following command in your terminal or command prompt:

.. code-block:: bash

    python manage.py db <command> [options]

Commands
--------

**generate_data:** Generates data for all apps.

.. code-block:: bash

    python manage.py db generate_data

**generate_data:** Generates data for a specified app and model with the given number of records. Optional commands can be added.

.. code-block:: bash

    python manage.py db generate_data --app_name=<app_name> --model_name=<model_name> --number_of_records=<number>

Replace ``<app_name>``, ``<model_name>``, and ``<number>`` with the appropriate values.

Examples:

- Generate data for the ``myapp`` app, ``mymodel`` model, and generate 10 records:

  .. code-block:: bash

      python manage.py db generate_data --app_name=myapp --model_name=mymodel --number_of_records=10

**stress_test:** Performs a stress test operation.

.. code-block:: bash

    python manage.py db stress_test

Help
----

To see a list of allowed arguments and their descriptions, use the following command:

.. code-block:: bash

    python manage.py db --help

``--help`` provides detailed information about the available options and how to use them.

