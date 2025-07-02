# Language Model Workshop

This is the coding portion for a workshop on Language Models created for the 2025 Data Science Fellowship cohort at UC Riverside.

`main.py` is a small retrieval augmented generation script.
`main_with_blanks.py` is the main script with some code taken away and `TODO` comments,
to be filled in during the workshop.

## Getting it running

You must setup Ollama with the proper models and install the Python dependencies.

### Ollama setup
Before running the script, you must install [Ollama](https://ollama.com/).
Then, run

```bash
ollama pull qwen3:1.7b
ollama pull nomic-embed-text:latest
```

to download the needed models.

If Ollama is not currently running, you can start it with

```bash
ollama serve
```

Ollama must be running on localhost on port 11434, which should be the default.

### Python dependencies

If you have `uv` installed, use

```bash
uv run main.py
```

in the root directory.

If you do not have `uv` installed, you can use

```bash
pip install .
```

to download the dependencies into your python Environment.
Then, run the script with

```bash
python main.py
```

## Functionality

When `main.py` is run, starts a loop that
1. prompts the user to ask a question through standard input;
2. injects relevant data into the prompt to help the LM answer the question;
3. prints this context-injected prompt to the standard output;
4. prints the response of the LM to the standard output.

Exit this loop with CTRL+C or your OS's equivalentt.

The LM receives data from `facts.txt`.
To test its abilities with retrieval augmented generation,
formulate questions for which the answers depend on the information in `facts.txt`.

The model is not supposed to respond if the data do not support any reponse.
Test this by asking questions irrelevant to the data.