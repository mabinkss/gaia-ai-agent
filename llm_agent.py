from openai import OpenAI

client = OpenAI()

def answer_with_llm(question: str) -> str:
    response = client.responses.create(
        model="gpt-6-luna",
        instructions=(
            "Tu es un assistant IA intelligent, naturel et pédagogique. "
            "Réponds comme dans une conversation entre deux personnes. "
            "Utilise un langage clair, simple et humain. "
            "Évite les listes, les tableaux, les tirets et les astérisques "
            "sauf si l'utilisateur les demande. "
            "Adapte la longueur de tes réponses à la question posée."
        ),
        input=question
    )

    return response.output_text

if __name__ == "__main__":
    question = input("Pose ta question : ")
    answer = answer_with_llm(question)
    print("Réponse de l'IA :", answer)
