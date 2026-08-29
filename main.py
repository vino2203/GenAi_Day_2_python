"""
GenAI Day 2 - Python Project
Starter script for Generative AI experimentation.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY is not set in your environment or .env file.")
        print("Please copy .env.example to .env and add your API key.")
        return

    print("Project initialized successfully.")
    print("Ready to build GenAI applications!")


if __name__ == "__main__":
    main()
