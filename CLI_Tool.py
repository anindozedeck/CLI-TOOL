import openai
import sys
from dotenv import load_dotenv
import os

load_dotenv()


def safe_draft_email(topic):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "[Error] OPENAI_API_KEY is not set. Add it to your .env file and try again."

    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You write professional Kenyan business emails. Keep them concise, warm, and direct."},
                {"role": "user", "content": f"Write a professional email about: {topic}"}
            ],
            timeout=30
        )
        return response.choices[0].message.content
    except openai.RateLimitError:
        return "[Error] OpenAI rate limit reached. Wait 60 seconds, then try again."
    except openai.AuthenticationError:
        return "[Error] OpenAI rejected the API key. Check OPENAI_API_KEY in your .env file and try again."
    except openai.APITimeoutError:
        return "[Error] The OpenAI request timed out after 30 seconds. Check your connection and try again."
    except openai.APIConnectionError:
        return "[Error] Could not connect to OpenAI. Check your internet connection and try again."
    except openai.BadRequestError as error:
        return f"[Error] OpenAI rejected the request: {error}. Check the topic and request settings, then try again."
    except openai.APIStatusError as error:
        return (
            f"[Error] OpenAI returned HTTP {error.status_code}. "
            "Try again; if the problem persists, check OpenAI's service status."
        )
    except openai.OpenAIError as error:
        return f"[Error] The OpenAI request failed: {error}. Check your API configuration and try again."
    except Exception as error:
        return (
            f"[Error] An unexpected error occurred while generating the email: {error}. "
            "Check your configuration and try again; if it persists, contact support."
        )


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if not args:
        print("Usage: python CLI_Tool.py 'your email topic here'", file=sys.stderr)
        return 1

    topic = " ".join(args)
    email = safe_draft_email(topic)
    if email.startswith("[Error]"):
        print(email, file=sys.stderr)
        return 1

    print(email)
    return 0


if __name__ == "__main__":
    sys.exit(main())