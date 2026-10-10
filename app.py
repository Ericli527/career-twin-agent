from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = "gpt-5.4-mini"

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Eric's Career Twin | AI-Powered Chatbot",
        description=(
        "Ask my AI twin about my background, experience, "
        "technical skills, projects, and career interests.\n\n"
        "Explore how I combine Data Analytics, AI, and "
        "Quantitative Finance to solve business problems."
        ),
        chatbot=gr.Chatbot(
    show_label=False,
    placeholder=(
        "## 👋 Welcome to Eric's Career Twin!\n\n"
        "I'm Eric's AI-powered career assistant.\n\n"
        "Ask me about his experience in "
        "**Data Analytics, AI, Finance, and Risk**, "
        "or explore his technical projects and career interests.\n\n"
        "**Select a question below to get started!**"
        ),
    ),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())
