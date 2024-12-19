import ollama

schema = ""
tableName = input("Enter table name (or DONE if done) >> ")

while tableName != "DONE":
    tableColumns = input("Enter the columns in the table " + tableName + " >> ")
    schema += "There is a table named " + tableName + " with the columns: " + tableColumns + "."
    tableName = input("Enter table name (or DONE if done) >> ")

query = input("Enter the query >> ")
print("Generating...\n")

response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "Consider the following SQL tables. "
                + schema
                + "Generate a SQL query for these tables for the following prompt: "
                + query
                + "Your answer must include a SELECT and FROM clause, and other clauses if needed."
                + "Your answer must be a valid SQL query and nothing else.",
        },
    ],
)
print(response["message"]["content"])