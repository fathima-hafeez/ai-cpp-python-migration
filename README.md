AI Repository Migration – C++ → Python using AWS Bedrock
##Overview

This project demonstrates a prototype AI-assisted code modernization pipeline that converts a C++ repository into Python modules using AWS Bedrock and Claude models.

The system uses a skill-based approach (skill.md) where migration instructions are defined once and then applied to convert the entire repository.

The pipeline reads C++ files, sends them to the model along with the migration instructions, and generates equivalent Python modules automatically.
##Use Case

Many enterprise applications are built using C++ and modular repositories. Migrating these systems to modern languages like Python usually requires manual effort.

This prototype explores how LLM-based automation can assist in repository-level migration by:

Reading C++ source files
Applying migration instructions
Generating Python modules
Preserving object-oriented structure and logic

Key Idea – skill.md Approach

Instead of sending multiple prompts to the model, migration instructions are defined in a reusable skill file.

Example:

skill.md

This file defines rules such as:

Convert C++ classes to Python classes
Merge header (.h) and implementation (.cpp) files
Preserve object-oriented structure
Generate Python modules in the specified format

The model then executes the migration using these predefined instructions.

Project Structure

ai_repo_migration
│
├── cpp_repo
│   ├── Account.cpp
│   ├── Account.h
│   ├── BankSystem.cpp
│   └── main.cpp
│
├── python_repo
│   └── (Generated Python modules)
│
├── run_migration.py
├── migration_engine.py
└── skill.md

C++ Sample Repository
The repository used in this prototype represents a small banking system with multiple classes.

Components include:

Account
BankSystem
Main application

Concepts demonstrated:

Object-oriented design
Class definitions
Repository-level code structure
Migration Pipeline

The migration pipeline follows these steps:

C++ Repository
      ↓
Read Source Files
      ↓
Apply skill.md Instructions
      ↓
Send Code to Claude (AWS Bedrock)
      ↓
Generate Python Modules
Migration Engine

migration_engine.py handles communication with AWS Bedrock.

Responsibilities include:

Preparing the prompt
Sending repository code to the model
Receiving generated Python code
Returning the output to the migration script

The model used:

Claude (via AWS Bedrock)
Migration Script

run_migration.py orchestrates the entire process.

Steps performed:

Reads all .cpp and .h files from the C++ repository
Loads migration instructions from skill.md
Sends the repository and instructions to the model
Receives generated Python code
Splits the response into individual Python modules
Writes generated modules into python_repo
Running the Migration

Activate the Python environment and run:

python run_migration.py

Example output:

Created: account.py
Created: banksystem.py
Created: main.py

Generated files will appear inside:
python_repo/

Example Code Conversion
C++ Code
Account acc1(1,1000);
acc1.deposit(200);
Generated Python Code
acc1 = Account(1,1000)
acc1.deposit(200)

Technologies Used
Python
C++
AWS Bedrock
Claude LLM
Git

Author
Fathima Hafeez
Senior Data Scientist

