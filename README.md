# GAIA AI Agent

**An AI-powered assistant built with Python, OpenAI, and Gradio.**

GAIA AI Agent is a personal learning project designed to answer natural language questions and analyze external content, including PDF documents, Excel spreadsheets, and YouTube videos.

The project started from the Hugging Face Agents Course GAIA assignment and evolved into an interactive AI application using the OpenAI API and additional data-processing tools.

## Features

**AI Chat**

- Answer general questions using an OpenAI language model.
- Generate natural language explanations.
- Adapt responses to different questions and contexts.

**PDF Analysis**

- Upload PDF documents.
- Extract text using Python.
- Ask questions and generate summaries based on document content.

**Excel Analysis**

- Upload Excel spreadsheets (.xlsx).
- Extract tabular data using Pandas.
- Ask questions about the available data.

**YouTube Video Analysis**

- Paste a YouTube video URL.
- Retrieve available transcripts using the Supadata API.
- Summarize video discussions and answer questions about spoken content.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| OpenAI API | AI-powered responses |
| Gradio | Interactive web interface |
| Pandas | Excel data processing |
| pypdf | PDF text extraction |
| Supadata API | YouTube transcript retrieval |
| Git & GitHub | Version control and project management |
| GitHub Codespaces | Cloud-based development environment |

## Project Structure

```text
gaia-ai-agent/
├── app.py
├── llm_agent.py
├── pdf_reader.py
├── excel_reader.py
├── youtube_reader.py
├── requirements.txt
└── README.md
```

- `app.py`: Main Gradio interface and application logic.
- `llm_agent.py`: OpenAI API integration.
- `pdf_reader.py`: PDF text extraction.
- `excel_reader.py`: Excel spreadsheet processing.
- `youtube_reader.py`: YouTube transcript retrieval through Supadata.

## Installation

Clone the repository:

```bash
git clone https://github.com/mabinkss/gaia-ai-agent.git
cd gaia-ai-agent
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Configure the following environment variables:

```text
OPENAI_API_KEY
SUPADATA_API_KEY
```

These API keys must be stored securely as environment variables or development environment secrets. Never commit API keys to GitHub.

Launch the application:

```bash
python app.py
```

Open the local Gradio application in your browser.

## Limitations

This project is an educational prototype.

- PDF analysis currently focuses on extractable text and does not support scanned documents requiring OCR.
- Excel extraction is limited to a subset of rows and may not cover complete datasets.
- YouTube analysis relies on available transcripts and does not analyze video images.
- Long documents and transcripts may be truncated.
- OpenAI and Supadata API access may involve usage limits or costs.
- The application is an AI assistant with integrated tools, not a fully autonomous multi-step agent.

## Project Background

This project was developed as part of my independent learning journey in artificial intelligence, Python programming, and AI applications.

It allowed me to practice working with APIs, organizing Python modules, integrating external data sources, developing user interfaces, and using GitHub for version control.

My goal is to continue improving the project while developing practical skills in AI engineering and automation.

## Author

**Mahel Symphor Chaix**

BBA Student at EM Normandie

Interested in AI Engineering, AI Agents, Automation, and Data.

[LinkedIn](https://www.linkedin.com/in/mahel-symphor-chaix-88925429b/)