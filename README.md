# owmains-subreddit-stats

Collect data on the Overwatch Mains subreddits

## Requirements

* Python
* Docker
* Docker Compose

## Setup

1. Follow Reddit's [First Steps Guide](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to obtain a Client ID & Client Secret

2. Create a .env file in the root directory and paste the following inside it:

    ```env
    CLIENT_ID=your-client-id
    CLIENT_SECRET=your-client-secret
    USER=your-reddit-username
    PASSWORD=your-reddit-password
    USER_AGENT=subcounts by u/your-reddit-username
    ```

3. Replace each field in the .env with your credentials.

4. Create and activate a virtual environment.

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

5. Install dependencies.

    ```sh
    pip install -r requirements.txt
    ```
