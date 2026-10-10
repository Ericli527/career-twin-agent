"""Professional, responsive styling for Eric's Gradio Career Twin.

Drop-in replacement for styles.py. Public names GOLD, BLUE, PURPLE,
EXAMPLES, CSS and JS are retained for compatibility with app.py.
"""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about Eric's background and career journey.",
    "Why would Eric be a good fit for a Data Analyst role?",
    "How has Eric applied Python and machine learning?",
    "Tell me about Eric's experience in finance and risk.",
    "What AI projects has Eric developed?",
    "What career opportunities is Eric looking for?",
]

CSS = r"""
/* ==============================================================
   ERIC'S CAREER TWIN — PROFESSIONAL PORTFOLIO UI
   Gradio ChatInterface / Chatbot, light and dark compatible.
   Styles are cosmetic; no change to chatbot logic.
   ============================================================== */
:root {
  --twin-gold: #ecad0a;
  --twin-blue: #209dd7;
  --twin-purple: #753991;
  --twin-bg: #0d111b;
  --twin-card: #151c29;
  --twin-card-2: #1c2636;
  --twin-border: #303b4c;
  --twin-text: #f2f5fa;
  --twin-muted: #b3bfd0;
  --twin-shadow: 0 8px 32px rgba(0,0,0,.16);
}
body:not(.dark) {
  --twin-bg: #f5f7fb;
  --twin-card: #ffffff;
  --twin-card-2: #f1f5f9;
  --twin-border: #dce3ed;
  --twin-text: #172334;
  --twin-muted: #53647a;
  --twin-shadow: 0 8px 28px rgba(30,48,75,.06);
}

html, body, gradio-app {
  background: var(--twin-bg) !important;
}
.gradio-container {
  width: min(100%, 1040px) !important;
  max-width: 1040px !important;
  margin: 0 auto !important;
  padding: 42px 28px 56px !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}
.gradio-container * { box-sizing: border-box; min-width: 0; }

/* Hero heading and description: restrained, easy to scan */
.gradio-container h1 {
  font-size: clamp(26px, 3vw, 34px) !important;
  line-height: 1.22 !important;
  font-weight: 760 !important;
  letter-spacing: -.035em !important;
  color: var(--twin-text) !important;
  border-left: 4px solid var(--twin-gold);
  padding-left: 16px !important;
  margin: 0 0 15px !important;
}
.gradio-container > .prose,
.gradio-container .prose {
  color: var(--twin-text);
}
.gradio-container .prose:not(.message) > p {
  line-height: 1.7;
}

/* Neutralise Gradio's default component chrome without affecting form controls */
.gradio-container .block {
  box-shadow: none;
}

/* Main conversation frame */
.gradio-container .chatbot,
.gradio-container .chatbot.block {
  background: var(--twin-card) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 18px !important;
  box-shadow: var(--twin-shadow) !important;
  overflow: hidden !important;
  min-height: 360px !important;
}
.chatbot .block-label,
.chatbot .label-wrap { display: none !important; }

/* Empty-state placeholder: centre content without forcing its inner width.
   In Gradio some versions constrain the content with an inline max-width;
   keep text modest to avoid a tall narrow white column. */
.chatbot .placeholder-container,
.chatbot .placeholder {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  color: var(--twin-muted) !important;
  max-width: 100% !important;
  margin: 0 auto !important;
  padding: 18px 22px !important;
  text-align: center !important;
}
.chatbot .placeholder h1,
.chatbot .placeholder h2,
.chatbot .placeholder h3,
.chatbot .placeholder-container h1,
.chatbot .placeholder-container h2 {
  border: 0 !important;
  padding: 0 !important;
  margin: 0 0 10px !important;
  font-size: 20px !important;
  letter-spacing: -.02em !important;
  color: var(--twin-text) !important;
}
.chatbot .placeholder p,
.chatbot .placeholder-container p {
  font-size: 14px !important;
  line-height: 1.6 !important;
  color: var(--twin-muted) !important;
}
.chatbot .placeholder strong { color: var(--twin-text) !important; }

/* Messages: clear hierarchy, readable paragraphs */
.chatbot .message-row { background: transparent !important; }
.chatbot .message-row .message,
.chatbot .message-row .message-bubble,
.chatbot .message-row .bubble {
  font-size: 14px !important;
  line-height: 1.65 !important;
  padding: 12px 15px !important;
  border-radius: 13px !important;
  box-shadow: none !important;
}
.chatbot .message-row.user-row .message,
.chatbot .message-row.user-row .bubble,
.chatbot .message-row[data-role="user"] .message,
.chatbot .message-row[data-role="user"] .message-bubble {
  background: #eaf3ff !important;
  color: #162e49 !important;
  border: 1px solid #cce2ff !important;
}
body.dark .chatbot .message-row.user-row .message,
body.dark .chatbot .message-row.user-row .bubble,
body.dark .chatbot .message-row[data-role="user"] .message,
body.dark .chatbot .message-row[data-role="user"] .message-bubble {
  background: #17334d !important;
  color: #eaf3ff !important;
  border-color: #244d70 !important;
}
.chatbot .message-row.bot-row .message,
.chatbot .message-row.bot-row .bubble,
.chatbot .message-row[data-role="assistant"] .message,
.chatbot .message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-card-2) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-left: 3px solid var(--twin-purple) !important;
}
.chatbot .message-row .message p,
.chatbot .message-row .message-bubble p,
.chatbot .message-row .bubble p {
  font-size: 14px !important;
  line-height: 1.65 !important;
  margin: 0 0 9px !important;
}
.chatbot .message-row .message p:last-child,
.chatbot .message-row .message-bubble p:last-child,
.chatbot .message-row .bubble p:last-child { margin-bottom: 0 !important; }
.chatbot .message-row a { color: var(--twin-blue) !important; text-decoration: underline; }
.chatbot .message-row pre { overflow-x: auto; }

/* Suggested example prompts: tidy, clearly clickable cards */
.examples,
.examples-holder,
[data-testid="examples"] {
  width: 100% !important;
  max-width: 100% !important;
  background: transparent !important;
  margin: 14px 0 8px !important;
  padding: 0 !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button,
.examples td button,
.example,
[data-testid="examples"] button {
  border: 1px solid var(--twin-border) !important;
  border-radius: 12px !important;
  background: var(--twin-card) !important;
  color: var(--twin-text) !important;
  padding: 14px 16px !important;
  min-height: 65px !important;
  height: auto !important;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  line-height: 1.45 !important;
  text-align: left !important;
  white-space: normal !important;
  overflow-wrap: break-word !important;
  letter-spacing: normal !important;
  text-transform: none !important;
  box-shadow: 0 2px 8px rgba(0,0,0,.025) !important;
  cursor: pointer !important;
  transition: border-color .16s ease, transform .16s ease, box-shadow .16s ease !important;
}
.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  box-shadow: 0 5px 16px rgba(32,157,215,.12) !important;
  transform: translateY(-1px);
}

/* Input: professional textbox, gold send CTA */
.gradio-container textarea,
.gradio-container input[type="text"] {
  background: var(--twin-card) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 12px !important;
  padding: 12px 15px !important;
  font-family: inherit !important;
  font-size: 14px !important;
  line-height: 1.5 !important;
}
.gradio-container textarea::placeholder,
.gradio-container input::placeholder { color: var(--twin-muted) !important; }
.gradio-container textarea:focus,
.gradio-container input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  box-shadow: 0 0 0 3px rgba(236,173,10,.16) !important;
  outline: none !important;
}
.gradio-container button.primary,
.gradio-container button.submit,
.gradio-container button.submit-button,
.gradio-container .submit-button,
.gradio-container button[variant="primary"] {
  background: var(--twin-gold) !important;
  border: 1px solid var(--twin-gold) !important;
  color: #151515 !important;
  border-radius: 12px !important;
  min-height: 48px !important;
  cursor: pointer !important;
}
.gradio-container button.primary:hover,
.gradio-container button.submit:hover,
.gradio-container button.submit-button:hover,
.gradio-container .submit-button:hover {
  background: #f9bb27 !important;
  border-color: #f9bb27 !important;
}
.gradio-container button.primary svg,
.gradio-container button.submit svg,
.gradio-container button.submit-button svg,
.gradio-container .submit-button svg {
  color: #151515 !important;
  width: 19px !important;
  height: 19px !important;
}

/* Secondary / message action controls */
.chatbot button.icon-button,
.gradio-container .icon-button {
  min-height: initial !important;
  padding: 5px !important;
  border-radius: 8px !important;
  color: var(--twin-muted) !important;
  background: transparent !important;
}
.chatbot button.icon-button:hover,
.gradio-container .icon-button:hover {
  color: var(--twin-blue) !important;
}
:focus-visible { outline: 2px solid var(--twin-blue) !important; outline-offset: 2px; }

/* Keep page and chat scrollbars discrete */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-muted); }
::selection { background: rgba(236,173,10,.45); }

@media (max-width: 700px) {
  .gradio-container { padding: 25px 14px 36px !important; }
  .gradio-container h1 { font-size: 25px !important; padding-left: 12px !important; }
  .gradio-container .chatbot,
  .gradio-container .chatbot.block { min-height: 300px !important; border-radius: 14px !important; }
  .chatbot .placeholder,
  .chatbot .placeholder-container { padding: 12px !important; }
  .examples button,
  .example,
  [data-testid="examples"] button { min-height: 50px !important; font-size: 12px !important; padding: 11px 12px !important; }
}
@media (prefers-reduced-motion: reduce) {
  .gradio-container *, .gradio-container *::before, .gradio-container *::after {
    transition: none !important;
    animation: none !important;
  }
}
"""

JS = """() => {
    document.title = "Eric's Career Twin | AI-Powered Chatbot";
    // Avoid auto-focus: on mobile it can scroll past the welcome content.
}"""
