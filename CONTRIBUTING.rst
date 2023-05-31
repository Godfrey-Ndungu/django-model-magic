Contributing Guidelines
======================

Thank you for your interest in contributing to django-model-magic. We welcome contributions from the community to help make our project even better. To ensure a smooth collaboration process, please follow the guidelines below.

Clone the Project
-----------------

1. Fork the project repository on GitHub.
2. Clone your forked repository to your local machine::

   git clone https://github.com/your-username/project.git

Branching
---------

1. Create a new branch for your contribution::

   git checkout -b feature/your-feature-name

Development Environment
-----------------------

1. Install the necessary dependencies::

   pip install -r requirements.txt

2. Set up the project environment using Tox::

   tox

   Make sure all tests pass and the code style is consistent.

Making Changes
--------------

1. Make your desired changes to the codebase.
2. Ensure that your changes adhere to our coding conventions and best practices.
3. Update any relevant documentation, including the Sphinx documentation if necessary.

Testing
-------

1. Run the test suite using Tox::

   tox

   Make sure all tests pass successfully.

Committing Changes
------------------

1. Commit your changes with a descriptive commit message::

   git commit -m "Add your commit message here"

Pushing Changes and Creating a Pull Request
-------------------------------------------

1. Push your changes to your forked repository::

   git push origin feature/your-feature-name

2. Go to the original repository on GitHub and create a new pull request, providing a detailed description of your changes.

Continuous Integration
----------------------

- Our CI system will automatically run checks on your pull request to ensure the build is clean and the tests pass successfully. Make sure your changes do not introduce any regressions.

Documentation
-------------

- If your changes require updates to the project documentation, please make the necessary additions or modifications to the Sphinx documentation. Ensure that your changes are clearly documented and follow the existing conventions.

We appreciate your valuable contributions to our project. Thank you for helping us improve!

Note: These contributing guidelines are subject to change. Please stay updated with the latest guidelines in the repository's CONTRIBUTING.rst file.
