import openai

#openai.api_key = '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'
#message_history = []

def chat(inp, message_history, role="user"):
    message_history.append({"role": role, "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content

