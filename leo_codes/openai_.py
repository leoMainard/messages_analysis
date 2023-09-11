import openai

# Configurez votre clé d'API OpenAI
openai.api_key = "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"



# Posez une question à OpenAI GPT-3
question = input("Chat : ")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu es un assistant, tu réponds aux questions."},
        {"role": "user", "content": question}
    ]
)

# Affiche la réponse générée par GPT-3
print("GPT-3 :", response['choices'][0]['message']['content'])
