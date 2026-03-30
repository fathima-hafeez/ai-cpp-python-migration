import os
import boto3
import json

MODEL_ID = "eu.anthropic.claude-sonnet-4-6"

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="eu-north-1"
)

PYTHON_REPO = "python_repo"

project_code = ""

# Read all generated Python files
for file in os.listdir(PYTHON_REPO):

    if file.endswith(".py"):

        path = os.path.join(PYTHON_REPO, file)

        with open(path, encoding="utf-8") as f:
            code = f.read()

        project_code += f"\nFILE: {file}\n"
        project_code += code


prompt = f"""
You are a senior Python QA engineer.

Generate unit tests for the following Python project.

Rules:

- Use Python unittest framework
- Cover all classes and methods
- Include edge cases
- Output runnable Python code
- Do NOT include markdown blocks

Python Project:
{project_code}
"""

body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 6000,
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

response = bedrock.invoke_model(
    modelId=MODEL_ID,
    body=json.dumps(body)
)

result = json.loads(response["body"].read())

tests = result["content"][0]["text"]

test_file = os.path.join(PYTHON_REPO, "test_generated.py")

with open(test_file, "w", encoding="utf-8") as f:
    f.write(tests)

print("Unit tests generated in python_repo/test_generated.py")