def build_prompt(cpp_code, skill):

    prompt = f"""
Convert the following C++ code into Python.

Follow the migration rules carefully.

Migration Skill:
{skill}

C++ Code:
{cpp_code}

Return only valid Python code.
"""

    return prompt