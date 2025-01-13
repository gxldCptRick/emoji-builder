import json

from .model import EmojiRequest
from .encoding import tokenize
import click
import pyperclip
import yaml


@click.group()
def main():
    # used to denote the main entrypoint for the cli
    pass


def tokenize_and_save_to_file(
    request: EmojiRequest,
):

    tokens = tokenize(
        message=request.message,
        foreground=request.foreground,
        background=request.background,
    )
    output_message = "\n".join(token.render(request.width) for token in tokens)
    with open(request.output, "w", encoding="utf-8") as f:
        f.write(output_message)
    pyperclip.copy(output_message)


@main.command("cli")
@click.option("--black", "-b", default="💖")
@click.option("--white", "-w", default="😭")
@click.option("--message", "-m", required=True)
@click.option("--width", "-wd", default=12, type=int)
@click.option("--output", "-o", default="output.txt")
def legacy(black: str, white: str, message: str, width: int, output: str):
    return tokenize_and_save_to_file(
        EmojiRequest(
            message=message,
            foreground=black,
            background=white,
            width=width,
            output=output,
        )
    )


def load_file(filename: str):
    if filename.endswith(".txt"):
        with open(filename, "r", encoding="utf-8") as f:
            message = f.read()
            return EmojiRequest(message=message)
    elif filename.endswith(".json"):
        with open(filename, "r", encoding="utf-8") as f:
            return EmojiRequest.model_validate(json.load(f))
    elif filename.endswith(".yaml") or filename.endswith(".yml"):
        with open(filename, "r", encoding="utf-8") as f:
            return EmojiRequest.model_validate(yaml.safe_load(f))
    else:
        raise ValueError(f"Unsupported file type: {filename}")


@main.command("file")
@click.option("--input-file", "-i", required=True)
@click.option("--output-file", "-o")
def transform_from_file(input_file: str, output_file: str | None = None):
    values = load_file(input_file)
    values.output = output_file or values.output
    return tokenize_and_save_to_file(values)
