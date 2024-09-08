# 🤖 TON SBT Destroyer Bot

[![TON](https://img.shields.io/badge/TON-grey?logo=TON&logoColor=40AEF0)](https://ton.org)
[![Telegram Bot](https://img.shields.io/badge/Bot-grey?logo=telegram)](https://core.telegram.org/bots)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License](https://img.shields.io/github/license/nessshon/sbt-destroyer-bot)](https://github.com/nessshon/sbt-destroyer-bot/blob/main/LICENSE)
[![Redis](https://img.shields.io/badge/Redis-Yes?logo=redis&color=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker&logoColor=white)](https://www.docker.com/)

Tired of clutter in your wallet? Let our bot help you tidy up by removing unwanted SBT NFTs effortlessly. Simply provide
the address of the NFT you wish to part ways with, and our bot will handle the rest. Say goodbye to clutter and hello to
a cleaner wallet with just a few clicks!

* Bot example: [@SBTDestroyerBot](https://t.me/SBTDestroyerBot)

## Features

* **SBT Destroy:** Get rid of unwanted SBT NFTs in your wallet.

* **TON-Connect Integration:** Ensures a secure and user-friendly experience.

* **Multilingual Support:** Supports Russian and English for user interaction.

## Usage

<details>
<summary><b>Preparation and installation</b></summary>

1. Create a bot via [@BotFather](https://t.me/BotFather) and save the `TOKEN` (later referred to as `BOT_TOKEN`).

2. Create an API key on [tonconsole.com](https://tonconsole.com) (later referred to as `TONAPI_KEY`).

3. Obtain a key for TON Connect (**Optional**, later referred to as `TONAPI_TONCONNECT_KEY`).
   <blockquote>This key is necessary for the correct functioning of TON Connect on the backend under heavy user load. If you are expecting a high volume of traffic, more than one user per second, contact <a href="https://t.me/subden" alt=''">@subden</a> via private message to receive the key. Tell him about your project and the need for this key. If you don't expect much traffic, you can skip this step and use the bot without a key.</blockquote>

4. Clone the repository:

    ```bash
    git clone https://github.com/nessshon/sbt-destroyer-bot.git
    ```

5. Navigate to the bot directory:

    ```bash
    cd sbt-destroyer-bot
    ```

6. Clone the environment variables file:

   ```bash
   cp .env.example .env
   ```

7. Configure [environment variables](#environment-variables-reference) file:

   ```bash
   nano .env
   ```

8. Install Docker and Docker Compose:

   ```bash
   sudo apt install docker.io && apt install docker-compose -y
   ```

9. Run the bot in a Docker container:

   ```bash
   docker-compose up --build
   ```
   If you encounter the error:
   ```log
   Error while fetching server API version: HTTPConnection.request() got an unexpected keyword argument 'chunked'
   ```
   Install the latest version of docker-compose using the following command:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose  && sudo chmod +x /usr/bin/docker-compose
   ```
   After the bot is up and running smoothly, you can stop the containers by pressing **Ctrl + C** or **Ctrl + Shift + C
   ** in the terminal. Then, to restart them in the background, use:
   ```bash
   docker-compose up -d
   ```

</details>

## Environment Variables Reference

<details>
<summary><b>Click to expand</b></summary>

Here's a comprehensive reference guide for the environment variables used in the project:

| Variable                | Type  | Description                                                                                    | Example                                                                                      |
|-------------------------|-------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `BOT_TOKEN`             | `str` | Bot token obtained from [@BotFather](https://t.me/BotFather)                                   | `123456:qweRTY`                                                                              | 
| `BOT_DEV_ID`            | `int` | User ID of the bot developer, obtain it from [my_id_bot](https://t.me/my_id_bot)               | `123456789`                                                                                  |
| `MANIFEST_URL`          | `str` | URL of the bot's manifest file                                                                 | `https://raw.githubusercontent.com/nessshon/sbt-destroyer-bot/main/tonconnect-manifest.json` |
| `TONAPI_KEY`            | `str` | API key for TONAPI, obtain it from [tonconsole.com](https://tonconsole.com)                    | `AE33E...3FYQ`                                                                               |
| `TONAPI_TONCONNECT_KEY` | `str` | API key for TON Connect (**optional**), obtain it by contacting [@subden](https://t.me/subden) | `587d4...5a71` or leave empty                                                                |
| `REDIS_DSN`             | `str` | Redis connection DSN (Data Source Name)                                                        | `redis://redis:6379/0`                                                                       |

</details>

## Contribution

We welcome your contributions! If you have ideas for improvement or have identified a bug, please create an issue or
submit a pull request.

## Donations

**TON** - `EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess`

**USDT** (TRC-20) - `TGKmm9H3FApFw8xcgRcZDHSku68vozAjo9`

## Support

Supported by [TON Society](https://github.com/ton-society/grants-and-bounties), Grants and Bounties program.

## License

This repository is distributed under
the [MIT License](https://github.com/nessshon/sbt-destroyer-bot/blob/main/LICENSE).
