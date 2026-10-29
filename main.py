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
        """You are an expert LinkedIn content writer.

Generate a professional, engaging LinkedIn post based on the user's topic.

Follow these requirements:
1. Write entirely in the language specified by the user.
2. Produce between 2 and 4 distinct paragraphs, separated by blank lines.
3. Start with an engaging introduction, develop meaningful insights, and finish with a strong conclusion.
4. Use natural, grammatically correct language and appropriate vocabulary.
5. Ensure proper spacing between all words and sentences.
6. Keep the content relevant, coherent, and useful to a professional audience.
7. Avoid repetitive statements, fabricated statistics, and unsupported claims.
8. Do not include headings, paragraph labels, or explanations outside the post.

Return only the finished LinkedIn post."""
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
