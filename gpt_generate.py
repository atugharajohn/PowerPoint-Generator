import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_development(user_message):
    conversation = build_conversation(user_message)
    try:
        assistant_message = generate_assistant_message(conversation)
    except openai.error.RateLimitError as e:
        assistant_message = "Rate limit exceeded. Sleeping for a bit..."

    return assistant_message


def build_conversation(user_message):
    return [
        {"role": "system",
         "content": "You are an assistant that gives the idea for PowerPoint presentations. When answering, give the user the summarized content for each slide based on the number of slide. "
                    "And the format of the answer must be Slide X(the number of the slide): {title of the content} /n Content: /n content with 2 or more bullet points."},
        {"role": "user", "content": user_message}
    ]


def generate_assistant_message(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response['choices'][0]['message']['content']
