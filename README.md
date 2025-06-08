# Gigi Wallet Signing

Static pages for connecting wallets and signing transactions across TON, EVM and Solana.
amvojd-codex/refactor-and-enhance-multi-repository-project-for-production

## Setup
1. Clone the repo
2. Copy `.env.example` to `.env` and set `WEBHOOK_BASE` to your backend URL

Pages automatically initialise the Telegram Web App when embedded in the bot so MetaMask and Phantom can run inside Telegram.

## Setup
1. Clone the repo
2. Copy `.env.example` to `.env` and set `WEBHOOK_BASE` and `WEBHOOK_SECRET`
   to your backend URL and shared secret

3. Build and run with Docker:
   ```bash
   docker build -t gigi-wallet-signing .
   docker run -p 8080:80 --env-file .env gigi-wallet-signing
   ```

amvojd-codex/refactor-and-enhance-multi-repository-project-for-production
## Environment Variables
- `WEBHOOK_BASE` – Base URL of the webhook server used by the pages.

## Local Testing
Run the example webhook server and point the pages to it:

```bash
pip install -r requirements.txt
python webhook_server.py
```

Set `WEBHOOK_BASE` in `.env` to `http://localhost:5000`.

## Environment Variables
- `WEBHOOK_BASE` – Base URL of the webhook server used by the pages.
- `WEBHOOK_SECRET` – Secret used for HMAC signing.


## Tests
Install requirements then run `pytest`.

## Architecture
```
Wallet page -> Webhook backend -> Telegram bot
```

See `deploy/` for example nginx and systemd configs.
