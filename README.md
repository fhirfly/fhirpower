
# FHIR Power - FHIR Sentence Labeling Tool

FHIR Power is an open-source Python tool designed to create labeled FHIR sentences from FHIR resources represented in JSON format. It flattens nested JSON structures, commonly used to represent FHIR resources, into a flat dictionary with labeled keys corresponding to the paths in the nested structure.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

FHIR (Fast Healthcare Interoperability Resources) is a standard for exchanging healthcare information electronically. FHIR resources are often represented in JSON format, which can contain nested structures. Kindling simplifies the process of converting these nested structures into flat labeled dictionaries, making it easier for downstream applications such as natural language processing and data analysis.

## Installation

To use FHIR Power, you need to have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

You can then clone the FHIR Power repository and install the required dependencies using the following commands:

```
git clone https://github.com/fhirfly/fhirpower.git
cd fhirpower
pip install -r requirements.txt
```
## Usage
To use FHIR Power, you can import the flatten_fhir function from the fhirpower.py module in your own scripts. Here's a basic example of how to use the tool:
```
from fhirpower import flatten_fhir

# Example nested JSON FHIR resource
nested_json = {
    "resourceType": "Patient",
    "name": [
        {
            "given": "John",
            "family": "Doe"
        }
    ]
}

flat_dict = flatten_fhir(nested_json)
print(flat_dict)
```

### Examples
For more comprehensive examples and use cases, please refer to the examples directory in this repository. Each example demonstrates how to use Kindling for different types of FHIR resources.

### Contributing
Contributions to Kindling are welcome! If you'd like to contribute, please follow these steps:

### Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name.
Make your changes and commit them with descriptive messages.
Push your changes to your fork: git push origin feature-name.
Create a pull request detailing your changes.
Please ensure your code follows the project's coding style and includes appropriate tests.

### License
This project is licensed under the MIT License.
