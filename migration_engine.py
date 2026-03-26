# import boto3
# import json
# import time

# MODEL_ID = "eu.anthropic.claude-sonnet-4-6"

# bedrock = boto3.client(
#     service_name="bedrock-runtime",
#     region_name="eu-north-1"
# )

# api_calls = 0
# input_tokens = 0
# output_tokens = 0
# total_latency = 0


# def migrate_repository(repo_code, skill):

#     global api_calls, input_tokens, output_tokens, total_latency

#     prompt = f"""
# Execute the following skill.

# {skill}

# Repository Code:
# {repo_code}
# """

#     body = {
#         "anthropic_version": "bedrock-2023-05-31",
#         "max_tokens": 6000,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     }

#     start = time.time()

#     response = bedrock.invoke_model(
#         modelId=MODEL_ID,
#         body=json.dumps(body)
#     )

#     latency = time.time() - start

#     result = json.loads(response["body"].read())

#     text = result["content"][0]["text"]

#     if "usage" in result:
#         input_tokens += result["usage"].get("input_tokens", 0)
#         output_tokens += result["usage"].get("output_tokens", 0)

#     api_calls += 1
#     total_latency += latency

#     return text 

import boto3
import json
import time

MODEL_ID = "eu.anthropic.claude-sonnet-4-6"

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="eu-north-1"
)

api_calls = 0
input_tokens = 0
output_tokens = 0
total_latency = 0


def migrate_repository(repo_code, skill):

    global api_calls, input_tokens, output_tokens, total_latency

    prompt = f"""
Execute the following migration skill.

{skill}

Repository Code:
{repo_code}
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

    start = time.time()

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    latency = time.time() - start

    result = json.loads(response["body"].read())

    text = result["content"][0]["text"]

    if "usage" in result:
        input_tokens += result["usage"].get("input_tokens", 0)
        output_tokens += result["usage"].get("output_tokens", 0)

    api_calls += 1
    total_latency += latency

    return text