# LinkedIn Post Generator

An AI-powered LinkedIn Post Generator built with **Python, LangChain, and Ollama**. This project generates professional, engaging LinkedIn posts based on a user-provided topic and selected language using a locally running large language model (LLM).

Developed as part of the **Module 21 – AI Agent Project** assignment.

## Overview

Creating engaging professional content consistently can be challenging. This application simplifies the process by allowing users to enter a topic and choose a language, then automatically generating a LinkedIn-style post.

The application uses LangChain to manage the prompt and language-model workflow, while Ollama runs the language model locally. This approach avoids dependence on external AI APIs for text generation.

## Features

- **Topic-Based Generation:** Generate posts about technology, career development, business, productivity, and other topics.
- **Multilingual Support:** Generate content in languages such as English, Bengali, and Spanish.
- **Professional Writing:** Uses prompt engineering to encourage engaging, informative, and professional content.
- **Structured Output:** Instructs the model to generate posts containing 2–4 paragraphs.
- **Local AI Inference:** Uses Ollama to run the language model on the user's computer.
- **No External AI API Required:** Generates posts locally without relying on third-party cloud AI API quotas.
- **Simple Interface:** Accepts user input and displays the generated post directly in the terminal.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application logic |
| LangChain Core | Prompt templates and runnable chains |
| LangChain Ollama | Integration between LangChain and Ollama |
| Ollama | Local language-model runtime |
| Qwen2.5 3B | Text generation |

## Architecture

The application follows a simple, prompt-driven LLM workflow.

```text
          User Input
       Topic + Language
               |
               v
      ChatPromptTemplate
               |
               v
       LangChain Chain
               |
               v
       ChatOllama Client
               |
               v
        Ollama Runtime
               |
               v
       Qwen2.5 3B Model
               |
               v
     Generated LinkedIn Post
```

### How It Works

1. **Input Collection:** The application asks the user to enter a post topic and the desired output language.
2. **Prompt Construction:** A `ChatPromptTemplate` combines the user's inputs with instructions defining the post's language, tone, structure, and content quality.
3. **Chain Execution:** A LangChain runnable chain connects the prompt template to the language model.
4. **Text Generation:** The `ChatOllama` integration sends the formatted messages to the locally running Ollama model.
5. **Output Display:** The application extracts the generated text and displays the LinkedIn post in the terminal.

## Prerequisites

Before running the application, ensure that you have:

- Python 3.12 installed.
- Git installed.
- Ollama installed and accessible from the terminal.
- Sufficient system memory and disk space for the selected language model.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/linkedin_post_generator.git
cd linkedin_post_generator
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
py -3.12 -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

### 4. Install and Start Ollama

Download and install Ollama from the official website:

https://ollama.com/download

Download the model used by this project:

```bash
ollama pull qwen2.5:3b
```

Ollama runs the model locally. Ensure that the Ollama service is running before executing the application.

You can verify that the model is available by running:

```bash
ollama list
```

## Usage

Start the application from the project directory:

```bash
python main.py
```

The application prompts you to enter a topic and a language.

### Example

```text
=== LinkedIn Post Generator ===

Enter the post topic: The importance of AI in software engineering
Enter the post language: Spanish

Generating your LinkedIn post...
```

The application then displays the generated LinkedIn post in the terminal.

You can enter different topics and languages each time you run the application.

## Prompt Engineering

The application uses a system prompt to guide the language model toward producing professional LinkedIn content.

The prompt instructs the model to:

- Write in the language specified by the user.
- Produce between two and four distinct paragraphs.
- Begin with an engaging introduction.
- Develop relevant ideas and insights.
- End with a meaningful conclusion.
- Maintain natural, professional language.
- Avoid repetitive content and unsupported claims.
- Return only the finished post without additional explanations.

These instructions help guide the model's output toward the assignment's requirements. However, the model may not follow every formatting instruction perfectly on every request.

## Project Structure

```text
linkedin_post_generator/
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

| File | Description |
|---|---|
| `main.py` | Contains the model configuration, prompt template, LangChain chain, and application entry point. |
| `requirements.txt` | Lists the Python dependencies required by the application. |
| `.gitignore` | Excludes virtual environments, cache files, and other unnecessary or sensitive files from Git. |
| `README.md` | Documents the project, setup instructions, architecture, and usage. |

## Key Implementation Concepts

### ChatPromptTemplate

`ChatPromptTemplate` defines reusable instructions and input placeholders. It allows the application to construct prompts dynamically using the user's topic and language.

### ChatOllama

`ChatOllama` connects the LangChain application to the selected model served by Ollama.

### LangChain Runnable Chain

The expression `prompt | llm` connects the prompt template to the language model. When invoked, the chain formats the prompt, sends it to the model, and returns the generated response.

### Local Language Model

Qwen2.5 3B generates the text using the locally running Ollama runtime. This eliminates the need for an external cloud AI API for the generation workflow.

## Limitations

- Output quality depends on the selected language model.
- The model may occasionally produce grammatical errors or formatting inconsistencies.
- The requested paragraph count is guided by the prompt and is not strictly validated by the application.
- Generation speed depends on the computer's hardware and available resources.
- The application currently uses a command-line interface rather than a graphical web interface.

## Future Improvements

Potential improvements include:

- Adding a graphical user interface.
- Allowing users to select different writing tones.
- Supporting post-length customization.
- Adding output validation to improve formatting consistency.
- Providing an option to save generated posts to a text file.

These improvements are optional and are not required for the current assignment.

## Assignment Deliverables

This project is developed to satisfy the Module 21 assignment requirements:

- **Code Repository:** Python implementation with project documentation.
- **LLM Integration:** LangChain workflow connected to a local Ollama model.
- **Input Handling:** User-provided topic and language.
- **Post Generation:** Professional LinkedIn-style content in the selected language.
- **Demo Video:** A 2–3 minute demonstration explaining the implementation and showing the application in action.

## Author

**Sadman Wasee**

Computer Science and Engineering Graduate

## License

No license has been specified for this project yet.