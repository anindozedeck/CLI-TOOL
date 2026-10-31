# Email Drafter CLI

Email Drafter is a small command-line tool that turns a short topic into a concise, warm, professional Kenyan business email using OpenAI's `gpt-4o-mini` model.

## Requirements

- Python installed and available as `python` in your terminal
- An OpenAI API key with API access enabled
- An internet connection

## Install

Open a terminal in the folder containing `CLI_Tool.py`, then install the required packages:

```powershell
python -m pip install openai python-dotenv
```

Create a file named `.env` in the same folder as `CLI_Tool.py` and add your API key:

```text
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual key. Do not share the key or commit the `.env` file.

## Use

From that folder, run the script with a topic in quotes:

```powershell
python CLI_Tool.py "follow up on unpaid invoice"
```

The generated email is printed in the terminal. The topic can include spaces; the tool combines all supplied words into one topic.

If you run the command without a topic, the tool prints the usage instructions. If a request fails, it prints an error and a suggested next step to stderr. For example, if the API key is missing or invalid, check the `OPENAI_API_KEY` value in `.env`.

## Cost

The example request is estimated at about **KES 0.10 per email**. This is only a rough estimate: actual cost depends on the topic and generated email length, current OpenAI token pricing, and the USD/KES exchange rate. Check the [OpenAI API pricing page](https://openai.com/api/pricing/) for current rates. API usage is billed by OpenAI and is separate from any ChatGPT subscription.
