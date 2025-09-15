import google.generativeai as genai

genai.configure(api_key="AIzaSyDZnqrWwFRdOc-AammIfXv1fp0ITnJP1iI")

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break

    # Send message and get response
    response = chat.send_message(user_input)
    print("AI:", response.text)