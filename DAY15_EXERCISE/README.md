# Meeting Notes Summarizer

Meeting Notes Summarizer turns pasted meeting notes into three sections:

- **Decisions made**
- **Action items**, including owners and any deadlines mentioned
- **Unresolved questions**

It is intended for NGO, school, and business teams. It uses OpenAI's
`gpt-4o-mini` model and does not invent details missing from the notes.

## Requirements

- Python available as `python` in your terminal
- An OpenAI API key with API access
- An internet connection

## Installation

Open a terminal in the project root (the folder containing
`Meeting_Notes_Summarizer.py`) and install the dependencies:

```powershell
python -m pip install openai python-dotenv
```

Create a `.env` file in that same project root:

```text
OPENAI_API_KEY=your_openai_api_key
```

Replace the placeholder with your API key. Keep the key private and do not
commit the `.env` file.

## Example interaction

From the project root, run:

```powershell
python Meeting_Notes_Summarizer.py
```

Paste your notes, then press **Ctrl+Z** and **Enter** on Windows:

```text
Discussed the school garden project. Amina will order seeds by Friday.
The team agreed to start planting next Monday. Need to confirm who will
arrange transport for the tools.
```

Example output:

```text
Decisions made
- Start planting next Monday.

Action items
- Amina: order seeds by Friday.

Unresolved questions
- Who will arrange transport for the tools?
```

Empty notes, missing or invalid API keys, connection failures, timeouts, and
empty API responses produce an error message with a suggested next step.
