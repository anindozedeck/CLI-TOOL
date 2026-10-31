# Meeting Notes Summarizer

Meeting Notes Summarizer turns pasted meeting notes into three concise sections: decisions made, action items with owners and any mentioned deadlines, and unresolved questions. It is designed for NGO, school, and business teams. It uses OpenAI's `gpt-4o-mini` model and does not invent missing owners or deadlines.

## Requirements

- Python installed and available as `python` in your terminal
- An OpenAI API key with API access enabled
- An internet connection

## Installation

Open a terminal in this folder and install the dependencies:

```powershell
python -m pip install openai python-dotenv
```

Create a file named `.env` in this folder and add your API key:

```text
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual key. Keep it private and do not commit the `.env` file.

## Example interaction

Run the summarizer:

```powershell
python Day15_exercise.py
```

Paste the notes, then press **Ctrl+Z** and **Enter** on Windows to send them:

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

The tool reports actionable errors for empty notes, missing or invalid API keys, connection and timeout failures, and empty API responses.

## Existing Email Drafter

This repository also includes the Email Drafter CLI. It creates a concise, professional Kenyan business email from a topic using the same API key and dependencies.

```powershell
python CLI_Tool.py "follow up on unpaid invoice"
```

The example request is estimated at about **KES 0.10 per email**. This is only a rough estimate: actual cost depends on the topic and generated email length, current OpenAI token pricing, and the USD/KES exchange rate. Check the [OpenAI API pricing page](https://openai.com/api/pricing/) for current rates. API usage is billed by OpenAI and is separate from any ChatGPT subscription.
