import boto3
import json
import time
from config import MODEL_ID, REGION

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

def convert_cpp_to_python(prompt):

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 3000,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    start = time.time()

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    latency = time.time() - start

    result = json.loads(response["body"].read())

    python_code = result["content"][0]["text"]

    usage = result.get("usage", {})

    input_tokens = usage.get("input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)

    return python_code, input_tokens, output_tokens, latency