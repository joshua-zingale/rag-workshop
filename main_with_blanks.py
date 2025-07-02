"""A small example of Retrieval Augmented Generation (RAG).

When run, starts a loop that
    - prompts the user to ask a question through standard input;
    - injects relevant data into the prompt to help the LM answer the question;
    - prints this context-injected prompt to the standard output;
    - prints the response of the LM to the standard output.

This script expects to find a text document called "facts.txt" in the same directory as itself.
Each line of the text file is parsed as one datum that can be retrieved to answer the question.

Ollama must be running on localhost on port 11434.
Additionally, the thinking model "qwen3:1.7b" and the embedding model "nomic-embed-text:latest" must be available in Ollama.
"""

from typing import List

import numpy as np
import numpy.typing as npt
from ollama import Client

OLLAMA_URL = "localhost:11434"

PROMPT = """You are a data retrieval bot that answers questions based on data from your stores. You will be given a question, followed by results from your database. You must then answer the question with a very short answer based on the data from your database. If none of the database results are relevant to the question, respond to the question with "I am sorry, but I cannot find anything on that."

## Example Question

Question: Where is the moon?

Database Results:
Bob is tall.
The sun is on the mountain.
New York is a facinating place.

## Response
"I am sorry, but I cannot find anything on that."

# Actual question

Question: {question}

Database Results
{context}
"""

client = Client(OLLAMA_URL)


def main():
    global client

    retriever = Retriever("facts.txt")

    while True:
        question = input("Question: ")

        # Inject the question and the retrieved data into the prompt
        prompt_with_context = PROMPT.format(
            question=question, context="\n".join(retriever.get_segments(question, 5))
        )

        print("PROMPT:")
        print(prompt_with_context)

        # Generate a response from the language model
        for chunk in client.generate(
                model="qwen3:1.7b",
                prompt=prompt_with_context,
                stream=True,
                
            ):
            print(chunk.response, end="") # type: ignore

        print()


class Retriever:
    """A tool for getting textual context that may be relevant to a question text."""

    def __init__(self, path: str):
        """Initializes a Retriever from a data file.
        
        The data file should have one datum, i.e. segment of text, per line.
        """
        with open(path, "r") as f:
            self._segments = np.array(f.read().split("\n"))
        self._embeddings = list(map(embed_text, self._segments))

    def get_segments(self, question: str, k: int = 1) -> List[str]:
        """Returns a list of k segments of text that may be relevant to the question."""

        question_embedding = embed_text(question)

        # Get the indices for the segments sorted by their similarity to the question
        similarity_indicies = # TODO
        return self._segments[similarity_indicies[:k]] # type: ignore


def embed_text(text: str) -> npt.NDArray[np.float64]:
    """Returns a vector embedding for the input text."""
    global client
    return np.array(
        client.# TODO: Fetch the data from ollama. Find the correct method for getting an embedding
        dtype=np.float64 # type: ignore
    )


if __name__ == "__main__":
    main()
