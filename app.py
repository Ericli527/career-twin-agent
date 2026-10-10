"""Career Twin Gradio app with an accessible profile header."""

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
        tool_calls = response.choices[0].message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(response.choices[0].message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


PROFILE_CARD = """
<section class="career-profile" aria-label="Eric Li professional profile">
  <div class="career-profile__avatar" aria-hidden="true">EL</div>
  <div class="career-profile__body">
    <div class="career-profile__eyebrow">WELCOME TO MY CAREER TWIN</div>
    <h1 class="career-profile__name">Eric Li</h1>
    <p class="career-profile__headline">Data Analytics &amp; AI <span aria-hidden="true">·</span> Financial &amp; Risk Analytics</p>
    <p class="career-profile__intro">Explore my background in engineering and mathematical finance, practical analytics experience, and AI projects through the chatbot below.</p>
    <div class="career-profile__skills" aria-label="Selected skills">
      <span>Python</span><span>Power BI</span><span>Machine Learning</span><span>Financial Modelling</span>
    </div>
  </div>
  <nav class="career-profile__links" aria-label="Professional links">
    <a href="https://www.linkedin.com/in/ericliuk0527/" target="_blank" rel="noopener noreferrer" aria-label="View Eric's LinkedIn profile">LinkedIn ↗</a>
    <a href="https://github.com/Ericli527" target="_blank" rel="noopener noreferrer" aria-label="View Eric's GitHub profile">GitHub ↗</a>
  </nav>
</section>
"""


if __name__ == "__main__":
    with gr.Blocks(title="Eric's Career Twin | AI-Powered Chatbot") as demo:
        gr.HTML(PROFILE_CARD, padding=False)
        gr.Markdown(
            "### Ask my AI career assistant\n"
            "Choose a suggested question or ask about my experience, technical projects and career interests.",
            elem_classes=["career-chat-heading"],
        )
        gr.ChatInterface(
            fn=chat,
            examples=EXAMPLES,
            chatbot=gr.Chatbot(
                show_label=False,
                height=260,
                placeholder=(
                    "### 👋 Welcome to Eric's Career Twin!\n\n"
                    "Ask about my **experience, AI projects, technical skills, "
                    "or career interests**."
                ),
            ),
        )
    demo.launch(css=CSS, js=JS, theme=gr.themes.Base())
