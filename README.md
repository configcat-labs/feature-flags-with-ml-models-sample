# Using Feature Flags with Machine Learning Models

#### [Read the blog post here](https://configcat.com/blog/)

A companion repository for the blog post above. This repository contains a sample application that demonstrates how to use feature flags with machine learning models. It showcases the implementation of two text classification models using the popular machine learning library [SpaCy](https://spacy.io/). The models, namely the **Base Model** and the **Pro Model**, are designed to classify user-input text into specific intents based on their training data.

## Key Features

- **Base Model**: Designed for general text classification, covering intents such as goodbye, greeting, and business_hours.

- **Pro Model**: Tailored for advanced scenarios, including additional intent classification such as payment_methods, making it ideal for scenarios where premium features are reserved for paid users.

## Usage Scenario

These models are particularly useful in scenarios where you want to differentiate user access based on their subscription level. For instance, the Pro Model allows for more sophisticated intent classification, making it suitable for cases where users need information about payment methods, a capability not available in the Base Model.

## Example

The Pro Model is able to classify the following user input:

_"Can I pay you with my Google Pay wallet?"_

resulting in classification to the `payment_methods` intent, a capability beyond the scope of the Base Model.

## Build & Run

### Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [PIP](https://pip.pypa.io/en/stable/installation/)

### Steps to run

1. Clone the repository

```sh
git clone git@github.com:configcat-labs/feature-flags-with-ml-models-sample.git
```

2. Create a and activate a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

4. Install dependencies and run the app

```bash
pip3 install -r requirements.txt
```

```bash
python3 interact.py
```

5. Train both base and pro models by entering the appropriate option in the command line. For this example, I'll train the base model first.

```bash
1 - Interact | 2 - Train | 3 - Exit: 2

Model to train: 1 - Base | 2 - Pro: 1

Training completed for base model
```

Train the pro model.

```bash
1 - Interact | 2 - Train | 3 - Exit: 2

Model to train: 1 - Base | 2 - Pro: 2

Training completed for pro model
```

6. Now, copy your SDK key from the [ConfigCat dashboard](https://app.configcat.com) and paste it in the `YOUR-CONFIGCAT-SDK-KEY` placeholder in the `interact.py` file.

## Learn more

Useful links to technical resources:

- [**ConfigCat SDK Documentation**](https://configcat.com/docs/sdk-reference/python/) - ConfigCat SDK Documentation for Python.

- [SpaCy Documentation](https://spacy.io/usage) - SpaCy Documentation for Python.

[**ConfigCat**](https://configcat.com) also supports many other frameworks and languages. Check out the full list of supported SDKs [here](https://configcat.com/docs/sdk-reference/overview/).

You can also explore other code samples for various languages, frameworks, and topics here in the [ConfigCat labs](https://github.com/configcat-labs) on GitHub.

Keep up with ConfigCat on [Twitter](https://twitter.com/configcat), [Facebook](https://www.facebook.com/configcat), [LinkedIn](https://www.linkedin.com/company/configcat/), and [GitHub](https://github.com/configcat).

## Author

[Chavez Harris](https://github.com/codedbychavez)

## Contributions

Contributions are welcome!
