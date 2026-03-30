# import os
# import shutil

# from module_detector import detect_modules
# from dependency_detector import detect_dependencies
# from migration_engine import migrate_repository
# from cpp_analyzer import analyze_cpp_repo
# from python_analyzer import analyze_python_repo
# import migration_engine


# CPP_REPO = "cpp_repo"
# OUTPUT = "python_repo"


# # ===============================================
# # Clean Output Folder
# # ===============================================

# if os.path.exists(OUTPUT):
#     shutil.rmtree(OUTPUT)

# os.makedirs(OUTPUT, exist_ok=True)


# # ===============================================
# # Detect Modules
# # ===============================================

# modules = detect_modules(CPP_REPO)

# print("Detected Modules:")
# print(modules)


# # ===============================================
# # Detect Dependencies
# # ===============================================

# dependencies = detect_dependencies(CPP_REPO)

# print("Detected Dependencies:")
# print(dependencies)


# # ===============================================
# # Build Repository Input for LLM
# # ===============================================

# repo_code = ""

# for root, files in modules.items():

#     for file in files:

#         path = os.path.join(root, file)

#         with open(path, encoding="utf-8") as f:
#             code = f.read()

#         repo_code += f"\nFILE: {file}\n"
#         repo_code += code


# repo_code += "\n\nDEPENDENCIES\n"
# repo_code += str(dependencies)


# # ===============================================
# # Load Migration Skill
# # ===============================================

# with open("skill.md", encoding="utf-8") as f:
#     skill = f.read()


# # ===============================================
# # Run Migration
# # ===============================================

# python_code = migrate_repository(repo_code, skill)


# # ===============================================
# # Parse Generated Python Files
# # ===============================================

# files = python_code.split("FILE:")

# generated_files = []

# for block in files:

#     block = block.strip()

#     if block == "":
#         continue

#     lines = block.split("\n")

#     filename = lines[0].strip()

#     if not filename.endswith(".py"):
#         continue

#     code = "\n".join(lines[1:])

#     path = os.path.join(OUTPUT, filename)

#     with open(path, "w", encoding="utf-8") as f:
#         f.write(code)

#     generated_files.append(filename)

#     print("Created:", filename)


# print("\nRepository Migration Completed")


# # ===============================================
# # Run Code Analyzers
# # ===============================================

# cpp_analysis = analyze_cpp_repo(modules)
# python_analysis = analyze_python_repo(OUTPUT)


# # ===============================================
# # Repository Statistics
# # ===============================================

# cpp_file_count = sum(len(files) for files in modules.values())
# python_file_count = len(generated_files)
# dependency_count = sum(len(v) for v in dependencies.values())


# # ===============================================
# # Architecture Mapping
# # ===============================================

# architecture_map = []

# for root, files in modules.items():

#     for file in files:

#         if file.endswith(".cpp"):
#             architecture_map.append(f"{file} → {file.replace('.cpp','.py').lower()}")

#         if file.endswith(".h"):
#             architecture_map.append(f"{file} → {file.replace('.h','.py').lower()}")


# # ===============================================
# # Generate Conversion Mapping
# # ===============================================

# def generate_conversion_mapping(cpp_analysis, python_analysis):

#     mapping = []

#     for inc in cpp_analysis["includes"]:

#         if "iostream" in inc:
#             mapping.append("#include <iostream> → Python print()")

#         if "vector" in inc:
#             mapping.append("#include <vector> → Python list")

#     for c in cpp_analysis["classes"]:
#         if c in python_analysis["classes"]:
#             mapping.append(f"C++ class {c} → Python class {c}")

#     for m in cpp_analysis["methods"]:

#         for py_m in python_analysis["methods"]:

#             if m.lower() in py_m.lower():
#                 mapping.append(f"C++ method {m}() → Python method {py_m}()")

#     if "main" in python_analysis["methods"]:
#         mapping.append("C++ main() → Python entrypoint")

#     return sorted(set(mapping))


# conversion_mapping = generate_conversion_mapping(
#     cpp_analysis,
#     python_analysis
# )


# # ===============================================
# # Estimate Migration Complexity
# # ===============================================

# if cpp_file_count <= 5 and dependency_count <= 5:
#     complexity = "LOW"
# elif cpp_file_count <= 20:
#     complexity = "MEDIUM"
# else:
#     complexity = "HIGH"


# # ===============================================
# # Generate Migration Report
# # ===============================================

# report = f"""
# CTP Migration Report: C++ → Python
# ==================================

# Repository Overview
# -------------------
# C++ Files Analyzed: {cpp_file_count}
# Python Files Generated: {python_file_count}
# Dependencies Detected: {dependency_count}


# Architecture Mapping
# --------------------
# {chr(10).join(architecture_map)}


# C++ Code Structure
# ------------------
# Classes
# {chr(10).join(cpp_analysis["classes"])}

# Methods
# {chr(10).join(cpp_analysis["methods"])}

# Includes
# {chr(10).join(cpp_analysis["includes"])}


# Python Code Structure
# ---------------------
# Classes
# {chr(10).join(python_analysis["classes"])}

# Functions
# {chr(10).join(python_analysis["methods"])}

# Imports
# {chr(10).join(python_analysis["imports"])}


# Language Conversion Mapping
# ---------------------------
# {chr(10).join(conversion_mapping)}


# Migration Complexity
# --------------------
# Estimated Complexity: {complexity}


# Migration Metrics
# -----------------
# Claude API Calls: {migration_engine.api_calls}
# Input Tokens: {migration_engine.input_tokens}
# Output Tokens: {migration_engine.output_tokens}
# """


# if migration_engine.api_calls > 0:
#     report += f"Average Latency: {round(migration_engine.total_latency / migration_engine.api_calls,2)} seconds\n"

# report += f"Total Migration Time: {round(migration_engine.total_latency,2)} seconds\n"


# report_path = os.path.join(OUTPUT, "migration_report.txt")

# with open(report_path, "w", encoding="utf-8") as f:
#     f.write(report)


# print("Migration report saved to:", report_path)  

import os
import shutil

from migration_engine import migrate_repository
import migration_engine


CPP_REPO = "cpp_repo"
OUTPUT = "python_repo"


# clean output folder
if os.path.exists(OUTPUT):
    shutil.rmtree(OUTPUT)

os.makedirs(OUTPUT)


# read C++ repository
repo_code = ""

cpp_files = []

for file in os.listdir(CPP_REPO):

    path = os.path.join(CPP_REPO, file)

    with open(path, encoding="utf-8") as f:
        code = f.read()

    cpp_files.append(file)

    repo_code += f"\nFILE: {file}\n"
    repo_code += code


# load skill
with open("skill.md", encoding="utf-8") as f:
    skill = f.read()


# run migration
python_code = migrate_repository(repo_code, skill)


# save python files
files = python_code.split("FILE:")

generated_files = []

for block in files:

    block = block.strip()

    if block == "":
        continue

    lines = block.split("\n")

    filename = lines[0].strip()

    if not filename.endswith(".py"):
        continue

    code = "\n".join(lines[1:])

    path = os.path.join(OUTPUT, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    generated_files.append(filename)

    print("Created:", filename)


print("\nMigration Completed")


# generate comparison report
report = f"""
CTP Migration Report
====================

C++ Files
---------
{chr(10).join(cpp_files)}

Python Files
------------
{chr(10).join(generated_files)}

Code Migration Comparison
=========================
"""


# add before/after snippets
for file in cpp_files:

    if not file.endswith(".cpp"):
        continue

    cpp_path = os.path.join(CPP_REPO, file)

    py_file = file.replace(".cpp", ".py").lower()

    py_path = os.path.join(OUTPUT, py_file)

    if not os.path.exists(py_path):
        continue

    with open(cpp_path) as f:
        cpp_code = f.read()

    with open(py_path) as f:
        py_code = f.read()

    report += f"""

C++ File: {file}
----------------

C++ Code
--------
{cpp_code}

Python Code
-----------
{py_code}

"""


report += f"""

Migration Metrics
-----------------

Claude API Calls: {migration_engine.api_calls}
Input Tokens: {migration_engine.input_tokens}
Output Tokens: {migration_engine.output_tokens}
"""

if migration_engine.api_calls > 0:
    report += f"Average Latency: {round(migration_engine.total_latency / migration_engine.api_calls,2)} seconds\n"

report += f"Total Migration Time: {round(migration_engine.total_latency,2)} seconds\n"


report_path = os.path.join(OUTPUT, "migration_report.txt")

with open(report_path, "w", encoding="utf-8") as f:
    f.write(report)

print("Migration report saved to:", report_path)