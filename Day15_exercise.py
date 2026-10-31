import os
import sys

import openai
from dotenv import load_dotenv

load_dotenv()


SYSTEM_PROMPT = """You summarize meeting notes for NGO, school, and business teams.
Return exactly these sections:

Decisions made
- List each decision, or write "None recorded."

Action items
- List each action with its owner and deadline if one was mentioned. Do not invent
  owners or deadlines; write "Owner not specified" or "Deadline not specified"
  when needed. If there are no actions, write "None recorded."

Unresolved questions
- List questions or issues that still need clarification, or write "None recorded."

Be concise and use only information present in the notes."""


def summarize_meeting_notes(notes):
    if not notes.strip():
        raise ValueError("No meeting notes were provided. Paste the notes and try again.")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add your key to the .env file and try again."
        )

    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": notes.strip()},
            ],
            timeout=30,
        )
    except openai.RateLimitError as error:
        raise RuntimeError(
            "OpenAI rate limit reached. Wait 60 seconds, then try again."
        ) from error
    except openai.AuthenticationError as error:
        raise RuntimeError(
            "OpenAI rejected the API key. Check OPENAI_API_KEY in your .env file "
            "and try again."
        ) from error
    except openai.APITimeoutError as error:
        raise RuntimeError(
            "The OpenAI request timed out after 30 seconds. Check your connection "
            "and try again."
        ) from error
    except openai.APIConnectionError as error:
        raise RuntimeError(
            "Could not connect to OpenAI. Check your internet connection and try again."
        ) from error
    except openai.BadRequestError as error:
        raise RuntimeError(
            f"OpenAI rejected the meeting notes: {error}. Check the input and try again."
        ) from error
    except openai.APIStatusError as error:
        raise RuntimeError(
            f"OpenAI returned HTTP {error.status_code}. Try again; if the problem "
            "persists, check OpenAI's service status."
        ) from error
    except openai.OpenAIError as error:
        raise RuntimeError(
            f"The OpenAI request failed: {error}. Check your API configuration and try again."
        ) from error
    except Exception as error:
        raise RuntimeError(
            f"An unexpected error occurred: {error}. Check your configuration and try again."
        ) from error

    if not response.choices or not response.choices[0].message.content:
        raise RuntimeError(
            "OpenAI returned no summary. Try submitting the notes again."
        )

    summary = response.choices[0].message.content.strip()
    if not summary:
        raise RuntimeError(
            "OpenAI returned an empty summary. Try submitting the notes again."
        )
    return summary


def main():
    print("Paste your meeting notes, then press Ctrl+Z and Enter to finish.")
    notes = sys.stdin.read()

    try:
        summary = summarize_meeting_notes(notes)
    except (ValueError, RuntimeError) as error:
        print(f"[Error] {error}", file=sys.stderr)
        return 1

    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())