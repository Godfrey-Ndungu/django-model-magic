# Django-Model-Magic

Project Description: django-model-magic

django-model-magic is a powerful Python module that empowers developers to unleash the power of automated data generation and seamless integration with Django models. With this module, you can effortlessly generate realistic data for your Django models, saving you time and effort during the development and testing phases of your project.

By leveraging the capabilities of django-model-magic, you can quickly populate your Django models with meaningful data without having to manually create and input every entry. This automation streamlines the process and enables you to focus on other crucial aspects of your application's development.

## Features

- Automated Data Generation: django-model-magic automates the process of generating data for your Django models. It intelligently creates realistic and representative data, taking into account the various field types and constraints defined in your models.

- Seamless Integration with Django Models: The module seamlessly integrates with your existing Django models. By utilizing the power of introspection, django-model-magic analyzes your models' structure and generates appropriate data for each field, including foreign keys, one-to-one relationships, and many-to-many relationships.

- Realistic Data Generation: The generated data closely resembles real-world scenarios, enhancing the quality and authenticity of your test data. Whether you're working on a small personal project or a large-scale enterprise application, django-model-magic ensures that your data accurately represents the expected user interactions.

- Customization Options: django-model-magic provides flexible customization options to cater to your specific needs. You can define your own data generation rules and constraints, allowing you to tailor the generated data to suit your application's requirements.

- Time-Saving Solution: With django-model-magic, you can significantly reduce the time and effort required for data entry and testing. The module automates the generation of large datasets, including handling foreign keys, one-to-one relationships, and many-to-many relationships, enabling you to focus on other critical development tasks.

- Database clearing command: Provides a convenient command to clear the database, making it easy to reset and re-populate data during development and testing phases.

- Variation and stress testing: Generate diverse data sets with varying characteristics and volumes to test the scalability and robustness of your Django models and applications.

## Installation

Install with pip

```bash
  pip install django-model-magic
```

Add model_magic  to installed apps as the last item

```bash
  INSTALLED_APPS[
  #other apps
  
  "model_magic",
  ]
```


## Documentation

[Documentation](https://django-model-magic.readthedocs.io/en/latest/introduction.html)

## Usage
python manage.py generate_data [app_name] [model_name] number_of_records

- `[app_name]` (optional): Replace this with the name of your Django app for which you want to generate data. If not provided, data will be generated for all apps.
- `[model_name]` (optional): Replace this with the name of your Django model for which you want to generate data. If not provided, data will be generated for all models within the specified app.
- `number_of_records` (required): Replace this with the number of records you want to generate.

**Examples:**

- To generate 100 records for all apps and models, run:

```bash
  python manage.py generate_data 100
```

- To generate 100 records for a specific app, run:

```bash
  python manage.py generate_data myapp 100
```

- To generate 100 records for a specific app and model, run:

```bash
  python manage.py generate_data myapp MyModel 100
```

4. The command will execute and generate the specified number of records for the app and model you provided.

**Note:** Make sure you replace `[app_name]`, `[model_name]`, and `number_of_records` with the actual values you want to use.


If you need help or want to see a list of allowed arguments, use the following command:

```bash
    python manage.py generate_data --help
```

    This command will display the available options and their descriptions.


