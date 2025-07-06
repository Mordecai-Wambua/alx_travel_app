# Milestone 1: Setup and Database Configuration
The **alxtravelapp** project is a real-world Django application that serves as the foundation for a travel listing platform.
This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations. The aim is to equip learners with industry-standard best practices for starting and managing Django-based projects efficiently.

This milestone will teach you to set up a scalable backend, integrate MySQL for database management, and use Swagger for automated API documentation. These foundational steps are critical in preparing the application for future features and seamless team collaboration.

## Django Project Setup with API Documentation and Database Configuration

### Objective

Set up the Django project with the necessary dependencies, configure the database, and add Swagger for API documentation.

### Instructions

- **Create a Django Project**:

    - Set up a new Django project named `alx_travel_app`.
    - Create an app within the project named `listings`.
    - Install necessary packages, including `django, djangorestframework, django-cors- headers, celery, rabbitmq`, and `drf-yasg `for Swagger documentation.

- **Configure Settings**:

  - In `settings.py`, configure the project for REST framework and CORS headers.
        - Set up the database configuration to use MYSQL. Use environment variables for sensitive information such as database credentials. (Hint: Use the `django-environ` package to handle .env files).
- Add Swagger:
    - Install `drf-yasg` for Swagger documentation.
    - Configure Swagger to automatically document all APIs. The documentation should be available at `/swagger/`.
- Initialize Git Repository:
  - Initialize a Git repository and make your initial commit with the project setup files.