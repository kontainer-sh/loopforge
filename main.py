import sys
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def load_file(path):
    """Load and return the content of a file."""
    if not os.path.exists(path):
        print(f"[!] File not found: {path}")
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def ask_openai(prompt, code, model="gpt-4"):
    """Send prompt + code to OpenAI and get a response."""
    try:
        full_prompt = f"""You're an expert software engineer.

The user has the following instruction:

### Instruction:
{prompt}

### Code:
{code}

Provide your best response, formatted clearly and concisely."""

        print("[+] Sending request to OpenAI...")
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[ERROR] Failed to get response from OpenAI: {str(e)}"


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py \"<your prompt>\" <path_to_code_file>")
        return

    user_prompt = sys.argv[1]
    file_path = sys.argv[2]

    print("[+] Loading file:", file_path)
    code = load_file(file_path)

    if not code:
        return

    ai_response = ask_openai(user_prompt, code)

    print("\n[AI Response]:\n")
    print(ai_response)


if __name__ == "__main__":
    main()

