import pandas as pd
from difflib import get_close_matches

data = {
    "question": [
        "How to reset password?",
        "What is the refund policy?",
        "How to check account balance?"
    ],
    "answer": [
        "To reset your password, go to the login page and click 'Forgot Password'.",
        "Refunds are processed within 7 business days if conditions are met.",
        "You can check your account balance via the mobile app or by dialing *123#."
    ]
}
df = pd.DataFrame(data)

def knowledge_bot(query):
    matches = get_close_matches(query, df["question"], n=1, cutoff=0.3)
    if matches:
        answer = df.loc[df["question"] == matches[0], "answer"].values[0]
        return f"Answer: {answer}"
    else:
        return "Sorry, I couldn’t find relevant info."

# Interactive mode
while True:
    query = input("Ask me something (or type 'exit'): ")
    if query.lower() == "exit":
        break
    print(knowledge_bot(query))