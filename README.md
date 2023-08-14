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

- [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access): If you don't already have a basic Twitter Developer Account, you'll need to apply for access to the Twitter API version 2. This account will provide you with the necessary API keys and access tokens required to authenticate with the Twitter API.

Please note that this access level is necessary to interact with certain endpoints required by the app. The Twitter Developer Account is essential for obtaining the Bearer Token, which is used for authenticating API requests in the application. As of July 2023, Twitter API version 1.1 has been deprecated, so ensure that you are using version 2.

#### Database Setup

The database required for this application will be created automatically during the application's operation. You don't need to explicitly create the database beforehand. The application will handle the database creation and management internally.

To set up the database, ensure that you have the required dependencies installed and the environment variables configured as described earlier in the README.

#### Launching The App

1. Clone this repository to your local machine

2. Initialize and activate a virtualenv:

```bash
    # Creating a virtual environment

    # Unix/maxOS
    python3 -m venv env

    # Windows
    python -m venv env

    # Activating a virtual environment

    # Unix/maxOS
    source env/bin/activate

    # Windows
    .\env\Scripts\activate
```

3. Install the dependencies:

```bash
    pip install -r requirements.txt
```

4. Setup environment variables:

```bash
    # UNIX/macOS
    export BEARER_TOKEN='<your_bearer_token>'

    # Windows
    set BEARER_TOKEN='<your_bearer_token>'
```

5. Running the Application

Before running the application, make sure you have set the `BEARER_TOKEN` environment variable as described in the Setup environment section.

To run the application, follow these steps:

5.1. Adding Accounts

    Edit the `accounts.csv` file and add the Twitter accounts you want to track. The CSV should contain a list of account usernames with the format `@username`.

5.2. Running the Twitter API Script

    Open one terminal and navigate to the project directory. Run the `twitter_api.py` script:

    ```bash
        python twitter_api.py
    ```

    This script initializes the initial data load and daily updates of liked tweets for the specified accounts.

5.3. Running the Streamlit Application

    Open a second terminal and navigate to the project directory. Run the `streamlit_app.py` script:

    ```bash
        streamlit run streamlit_app.py
    ```

    This will launch the Streamlit web interface where you can explore the liked tweets for the specified accounts.

5.4. Accessing Liked Tweets

    Use the Streamlit web interface to navigate through the liked tweets data. You can select the page size and page number to view and navigate through the data.

## Acknowledgements and Considerations

### Twitter API Limitations

Please be aware of the limitations imposed by the Twitter API:

- **Rate Limits**: The Twitter API has rate limits that restrict the number of requests you can make in a certain time frame. The current implementation allows only 5 requests every 15 minutes. If you have more than 5 accounts in the `accounts.csv` file, you might encounter a "too many requests" error with response code 429. To mitigate this, it's recommended to have a maximum of 5 accounts in the CSV file.

### Data Storage and Deletion

- **Data Retention**: The data stored in the database is retained for 30 days, and it's set to be deleted gradually over time. Every day, records older than 30 days will be automatically removed from the database. This ensures that the database remains manageable and doesn't become overly bloated.

### Assumptions

- **Daily Like Limit**: The assumption is that users won't like more than 100 tweets per day due to the restricted Twitter API rate limits. This is to ensure that the application doesn't reach the API rate limits too quickly.

These considerations are important to ensure smooth and effective usage of the application. Feel free to adjust the application's configuration and assumptions according to your specific use case and requirements.
