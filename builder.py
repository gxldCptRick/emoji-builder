from abc import ABC, abstractmethod
import click
import pyperclip


@click.command()
@click.option("--black", "-b", default="💖")
@click.option("--white", "-w", default="😭")
@click.option("--message", "-m", required=True)
@click.option("--width", "-wd", default=12, type=int)
@click.option("--output", "-o", default="output.txt")
def main(
    black: str,
    white: str,
    message: str,
    width: int,
    output: str,
):
    tokens = tokenize(message, foreground=black, background=white)
    output_message = "\n".join(token.render(width) for token in tokens)
    with open(output, "w", encoding="utf-8") as f:
        f.write(output_message)
    pyperclip.copy(output_message)


class Token(ABC):
    def __init__(self, background: str, foreground: str):
        self.background = background
        self.foreground = foreground

    @abstractmethod
    def render(self, width: int) -> str:
        pass

    def render_map(self, width: int, map: list[list[int]]):
        """Renders map of characters using the foreground and background"""
        # TODO: Figure out a way to read in the map and then render it by multiplying the row to match width
        char_map = [
            [
                self.foreground if character != 0 else self.background
                for character in row
            ]
            for row in map
        ]
        return "\n".join("".join(row) for row in char_map)


class AToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class BToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class CToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class DToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class EToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class FToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class GToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class HToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class IToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class JToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class KToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class LToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class MToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class NToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class OToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class PToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class QToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
            ],
        )


class RToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class SToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class TToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class UToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class VToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class WToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class XToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class YToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class ZToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class HeartToken(Token):

    def render(self, width: int) -> str:
        bitmap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        return self.render_map(width, bitmap)


class SpaceToken(Token):
    def render(self, width: int) -> str:
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ],
        )


class ATToken(Token):
    def render(self, width: int) -> str:
        # TODO: Make @ sign with it
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 0],
            ],
        )


class DFaceToken(Token):
    def render(self, width: int) -> str:
        # TODO: MAke D Face
        return self.render_map(
            width,
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 0],
            ],
        )


TOKEN_MAP = {
    "A": AToken,
    "B": BToken,
    "C": CToken,
    "D": DToken,
    "E": EToken,
    "F": FToken,
    "G": GToken,
    "H": HToken,
    "I": IToken,
    "J": JToken,
    "K": KToken,
    "L": LToken,
    "M": MToken,
    "N": NToken,
    "O": OToken,
    "P": PToken,
    "Q": QToken,
    "R": RToken,
    "S": SToken,
    "T": TToken,
    "U": UToken,
    "V": VToken,
    "W": WToken,
    "X": XToken,
    "Y": YToken,
    "Z": ZToken,
    "<3": HeartToken,
    " ": SpaceToken,
    "@": ATToken,
    "D:": DFaceToken,
}

SPECIAL_TOKENS = {"<3", "@", "D:"}


def tokenize(
    message: str,
    background: str,
    foreground: str,
) -> list[Token]:
    tokens = []

    for segment in message.split(" "):
        if segment in SPECIAL_TOKENS:
            tokens.append(TOKEN_MAP[segment](background, foreground))
        else:
            for char in segment:
                try:
                    tokens.append(TOKEN_MAP[char.upper()](background, foreground))
                except KeyError:
                    pass
        tokens.append(TOKEN_MAP[" "](background, foreground))

    tokens.pop()  # Remove the last space

    return tokens


if __name__ == "__main__":
    main()
