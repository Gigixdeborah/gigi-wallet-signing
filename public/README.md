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
2. Update `WEBHOOK_BASE` and `WEBHOOK_SECRET` in `config.js` or via `.env`
   when building Docker image
3. Push to GitHub → deploy to Render

## Backend (example)
Run `webhook_server.py` to receive events.
