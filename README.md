# Autonomous AI Deal Hunter

An AI-powered resale deal finder that scans Japanese marketplaces and identifies profitable items for resale.

## Features

- Multi-brand scanning (Patagonia, Arc'teryx, Nike ACG, etc.)
- AI resale price estimation using OpenAI
- Profit calculation
- Deal scoring system

## Architecture

Scanner → Deal Analyzer → AI Resale Evaluator → Ranked Deals

## Example Output

{
"title": "Patagonia Phone Home Jacket",
"price": 3800,
"resale": 15000,
"profit": 11200,
"score": 0.75
}

## Tech Stack

Python  
LangChain  
OpenAI API  
Linux

## Run

python run_deal_finder.py
