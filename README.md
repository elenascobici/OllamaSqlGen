# OllamaSqlGen

This is a small experimental projet which generates a SQL query using
Meta's Llama 3.2 AI model.

## Running

Ensure that Ollama is installed. Then, run `ollama serve` to initialize
the Ollama inference server. For a more detailed tutorial, refer
to this article: https://www.datacamp.com/tutorial/run-llama-3-locally.

Then, in a separate terminal window, navigate to the cloned directory
and run `python sql_gen.py` to run the program.

## Example Usage

```
<dir where you cloned project>/OllamaSqlGen>python sql_gen.py
Enter table name (or DONE if done) >> Person
Enter the columns in the table Person >> id, name, age, pet_id
Enter table name (or DONE if done) >> Pet
Enter the columns in the table Pet >> id, name
Enter table name (or DONE if done) >> DONE
Enter the query >> Get every person who is older than 10, their name and their pet's name.
Generating...

SELECT P.name, P.age, Pet.name FROM Person P JOIN Pet ON P.pet_id = Pet.id WHERE P.age > 10;
```

## Purpose

The purpose of this project is for me to gain some experience with
prompt engineering and utilizing AI models.