import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY") ,
    #"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"
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = "meta-llama/llama-3.1-8b-instruct"

with open("prompts/ai_judge_prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()


state = {
    "round_number": 1,
    "bomb_used_by_user": False
}


for _ in range(3):
    user_input = input(f"\nRound {state['round_number']} - Enter your move: ")

    user_prompt = f"""
Current game state:
- round_number: {state['round_number']}
- bomb_used_by_user: {state['bomb_used_by_user']}

User input:
"{user_input}"
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    raw_output = response.choices[0].message.content.strip()

    try:
        result = json.loads(raw_output)
    except json.JSONDecodeError:
        print("\nModel returned invalid JSON:")
        print(raw_output)
        break

    print("\nAI Judge Decision:")
    print(json.dumps(result, indent=2))


    state["round_number"] += 1
    state["bomb_used_by_user"] = result.get(
        "bomb_used_by_user", state["bomb_used_by_user"]
    )
