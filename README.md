# Groq AI Clothing Brand Assistant 🧥🚀

An interactive, production-grade conversational AI pipeline engineered to assist fashion entrepreneurs in building, naming, and scaling apparel brands. This architecture utilizes a low-latency inference workflow engine to maintain continuous context tracking across multi-turn brand development sessions.

## 🛠️ Key Technical Features
* **Stateful Dialogue Architecture:** Implements a dynamic session memory array structure (`messages.append`) to retain multi-turn context history, allowing the assistant to process dependent follow-up questions accurately.
* **Low-Latency Inference Engine:** Integrated with Groq's high-performance hardware infrastructure using the `llama-3.3-70b-versatile` model to deliver millisecond response tokens.
* **System Persona Guardrails:** Configured with specific system core expert guidelines (`role: system`) to lock the LLM into a deterministic retail strategist persona, preventing generic conversational drift.
* **Production Error Resilience:** Implements centralized `try/except` exception tracking loops to catch real-world API rate limits or network drops gracefully without crashing the active terminal session loop.

## 📂 Project Structure
* `main.py` - Core execution loop script managing the terminal-based interactive chat matrix.
* `app.py` - Responsive Streamlit frontend web user interface dashboard providing a visual chat wrap.
* `.gitignore` - Safeguards your local workspace parameters and secure `.env` key tokens from public cloud exposure.

## ⚙️ Local Setup Instructions
1. Clone this repository to your local computer.
2. Initialize and activate an isolated python environment:
   ```bash
   uv venv
   .venv\Scripts\activate
   ```
3. Install the required client integration libraries:
   ```bash
   uv pip install groq python-dotenv streamlit
   ```
4. Configure your private validation key file named `.env` in the root project folder:
   ```text
   GROQ_API_KEY=your_actual_groq_api_key_string_here
   ```
5. To execute the interactive command-line application session loop:
   ```bash
   python main.py
   ```
6. To launch the visual browser-based frontend application dashboard layer:
   ```bash
   uv run streamlit run app.py
   ```
