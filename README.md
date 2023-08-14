# Twitter-Trackr

## Project Motivation

Twitter-Trackr is a Python application designed to track and store liked tweets of specified Twitter accounts. This application utilizes the Twitter API, a SQLite database, and the Streamlit framework to provide an interactive web interface for exploring and analyzing liked tweets.

## Key Features

- Initial load of liked tweets for specified accounts.
- Daily updates to retrieve new liked tweets and remove older data.
- Storing liked tweets in a SQLite database.
- Interactive web interface using Streamlit for exploring liked tweets.

## Getting started

The project adheres to the PEP 8 style guide and follows common best practices, including:

- Variable and function names are clear.
- Code is commented appropriately.
- Secrets are stored as environment variables.

### Key Dependencies & Platforms

- [`tweepy`](https://www.tweepy.org/): A Python library for accessing the Twitter API, enabling interaction with Twitter data.
- **[`streamlit`](https://www.streamlit.io/)**: A Python library for building interactive web applications with ease, used to create the web interface for exploring liked tweets.
- **[`SQLite`](https://www.sqlite.org/index.html)**: A lightweight and self-contained SQL database engine, employed to store and manage liked tweets data locally.

Feel free to explore the official documentation for each of these technologies to learn more about their features and usage.

### Running Locally

#### Installing Dependencies

- [Python 3.11](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) - Follow instructions to install the latest version of python for your platform.

- [Virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized.

Once you have your virtual environment setup and running, install dependencies by running:

```bash
    pip install -r requirements.txt
```

This will install all of the required packages I selected within the `requirements.txt` file.

#### Database Setup
