# CI-CD-RafaelTorices

Repository for the CI/CD subject of the module KeepCoding DevOps Bootcamp

## Description

This repository contains a simple application written in **Python** that uses the **Flask** framework. The application is a simple **_calculator web application_** with various operations (add, subtract, multiply, divide, power). The application is deployed in a **Kubernetes cluster** using **ArgoCD**. The application is automated using **CircleCI**. The application is tested using **pytest** and the coverage is calculated using **pytest-cov**. The application is linted using **pylint** and **flake8**. Also, the static code analysis is done using **SonarCloud**. All these tools have been used to create a CI/CD pipeline for the application.

## Repository structure

The repository is structured as follows:

- **.circleci**: Contains the configuration file for CircleCI (**config.yml** is the file that contains the pipeline).
- **argocd**: Contains the configuration files for ArgoCD (the **argoapp.yml** file contains the configuration of the application in ArgoCD). File **values.yaml** contains the values default for deploy Helm chart of ArgoCD.
- **k8s**: Contains the Kubernetes manifests for the deployment of the application in the cluster (deployment, service, ingress) with ArgoCD.
- **src**: Contains the application python code.
- **tests**: Contains the tests for the python application code.
- **.gitignore**: Contains the files that are ignored by git.
- **Dockerfile**: Contains the instructions to create the docker image of the python application.
- **MANIFEST.in**: Contains the instructions to package the python application.
- **requirements.txt**: Contains the dependencies of the python application.
- **README.md**: Contains the description of the repository (this file).
- **setup.py**: Contains the instructions to package the python application.

> ## Note
>
> Each folder contains a README.md file with a description of its contents.

## Github individual repositories

- **Python application**: https://github.com/RafaTorices/CI-CD-APP-RafaelTorices
- **ArgoCD application**: https://github.com/RafaTorices/CI-CD-ArgoCD-RafaelTorices
- **K8s manifests**: https://github.com/RafaTorices/CI-CD-APP-RafaelTorices
- **Docker image**: https://hub.docker.com/repository/docker/rafacv99/pycalculator/general

## Aplication

**src/calculator.py**:
Contains the code of the application.

    The application is a simple calculator that has the following operations: - Add - Subtract - Multiply - Divide - Power

**Dependencies**

    - Packaging: for packaging the application.
    - Pytest: for testing the application.
    - Coverage: for calculating the coverage of the application.
    - Pylint: for linting the application.
    - Flake8: for to check the code quality.
    - pdoc: for generating the documentation of the application.
    - Flask: for the web application.
    - Build: for building the package of the application.
    - setuptools: for building the package of the application.
