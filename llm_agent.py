from openai import OpenAI

client = OpenAI()

def answer_with_llm(question: str) -> str:
    response = client.responses.create(
        model="gpt-6-luna",
        input=question
    )
    return response.output_text

if __name__ == "__main__":
    question = input("Pose ta question : ")
    answer = answer_with_llm(question)
    print("Réponse de l'IA :", answer)
