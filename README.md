# OpenCRE Library
# English
# OpenCRE Library

OpenCRE Library is a library developed to simplify integration with the [OpenCRE](https://www.opencre.org/) database, allowing developers to access and manipulate information related to security frameworks, controls, and requirements with simplicity and efficiency.

## 📚 Features

- Direct access to OpenCRE information.
- Filtering and querying security requirements.
- Easy integration for projects that use compliance and security data.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### Installation

1. Install the library:
   ```bash
   pip3 install opencre-lib
2. How use:
    ```python
    from opencre_lib.compare import Map
    
    r = Map(primary="CWE", secundary="ISO 27001").generate_table()
    print(r)
    ```
# Portuguese
OpenCRE Library é uma biblioteca desenvolvida para facilitar a integração com o banco de dados [OpenCRE](https://www.opencre.org/), permitindo que desenvolvedores acessem e manipulem informações relacionadas a frameworks de segurança, controles e requisitos com simplicidade e eficiência.

## 📚 Funcionalidades

- Acesso direto às informações do OpenCRE.
- Filtragem e consulta de requisitos de segurança.
- Integração fácil para projetos que utilizam dados de compliance e segurança.

## 🚀 Começando

### Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado no seu ambiente.

### Instalação

1. Clone este repositório:
   ```bash
   pip3 install opencre-lib
    ```
2. Como usar:
    ```python
    from opencre_lib.compare import Map

    r = Map(primary="CWE", secundary="ISO 27001").generate_table()
    print(r)
    ```