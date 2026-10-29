from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


# Initialize the local language model
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
)


# Define the instructions for generating a LinkedIn post
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a professional LinkedIn content writer.

Generate engaging, informative, and professional LinkedIn posts.

Follow these rules:
- Write in the language selected by the user.
- Produce exactly 3 paragraphs.
- Keep the content relevant to the given topic.
- Use a natural, engaging, and professional tone.
- Avoid fabricated statistics and unsupported claims.
- Do not include headings or explanations outside the post.
- Return only the final LinkedIn post."""
    ),
    (
        "human",
        "Topic: {topic}\nLanguage: {language}"
    )
])


# Connect the prompt to the language model
chain = prompt | llm


def generate_post(topic: str, language: str) -> str:
    """Generate a LinkedIn post for the given topic and language."""

    response = chain.invoke({
        "topic": topic,
        "language": language
    })

    return response.content


def main():
    """Collect user inputs and display the generated post."""

    print("\n=== LinkedIn Post Generator ===\n")

    topic = input("Enter the post topic: ").strip()
    language = input("Enter the post language: ").strip()

    if not topic or not language:
        print("Error: Both topic and language are required.")
        return

    print("\nGenerating your LinkedIn post...\n")

    try:
        post = generate_post(topic, language)

        print("=" * 50)
        print(post)
        print("=" * 50)

    except Exception as error:
        print(f"Error generating post: {error}")
        print("Check that Ollama is running and the model is available.")


if __name__ == "__main__":
    main()
