import os
from env import ChatbotEnv, Action

# Required env variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

env = ChatbotEnv()

total_reward = 0

for _ in range(3):
    obs = env.reset()

    action = Action(
        intent="complaint",
        category="billing",
        response="Sorry for the issue. We will resolve it soon."
    )

    obs, reward, done, _ = env.step(action)
    total_reward += reward

print("Baseline Score:", total_reward / 3)