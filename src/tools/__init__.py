"""Simple utility tools used by the agents and pipelines."""

import os


def list_files(path: str = "."):
    try:
        return os.listdir(path)
    except Exception as e:
        return f"Error: {str(e)}"


def read_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"


def write_file(path: str, content: str):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return "Write successful"
    except Exception as e:
        return f"Error: {str(e)}"


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
}
