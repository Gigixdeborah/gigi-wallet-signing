# Gigi Wallet Signing

Static pages for connecting wallets and signing transactions across TON, EVM and Solana.

## Setup
1. Clone the repo
2. Copy `.env.example` to `.env` and set `WEBHOOK_BASE` and `WEBHOOK_SECRET`
   to your backend URL and shared secret
3. Build and run with Docker:
   ```bash
   docker build -t gigi-wallet-signing .
   docker run -p 8080:80 --env-file .env gigi-wallet-signing
   ```

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
