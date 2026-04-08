from pydantic import BaseModel

class Observation(BaseModel):
    message: str

class Action(BaseModel):
    intent: str
    category: str
    response: str

class ChatbotEnv:
    def __init__(self):
        self.message = ""

    def reset(self):
        self.message = "My payment failed but money was deducted"
        return Observation(message=self.message)

    def step(self, action):
        reward = 0.0

        if action.intent.lower() == "complaint":
            reward += 0.4

        if action.category.lower() == "billing":
            reward += 0.3

        if "sorry" in action.response.lower():
            reward += 0.3

        return Observation(message=self.message), reward, True, {}

    def state(self):
        return {"message": self.message}