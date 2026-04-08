# Customer Support Chatbot (OpenEnv)

## Overview
This project simulates a customer support chatbot where an AI agent handles user queries.

## Tasks
1. Intent Classification (Easy)
2. Category Detection (Medium)
3. Response Generation (Hard)

## Observation
Customer message

## Action
- intent
- category
- response

## Reward
Based on correct classification and response quality

## Run
python inference.py

## Output
Reward: 1.0

## Baseline Inference

The inference script evaluates the environment using a baseline model simulation.

It reads API credentials from environment variables (HF_TOKEN) and computes average reward across multiple runs.

## Baseline Score
Baseline Score: 1.0



## Setup

Set environment variables:
- API_BASE_URL
- MODEL_NAME
- HF_TOKEN