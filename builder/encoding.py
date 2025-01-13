from abc import ABC, abstractmethod
from typing import TypedDict


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


class TokenEntry(TypedDict):
    cls: type[Token]
    is_special: bool


TOKEN_MAP: dict[str, TokenEntry] = {}


def register(pattern: str, is_special: bool = False):
    is_special = is_special or len(pattern) > 1

    def decorator(cls):
        if pattern in TOKEN_MAP:
            # we skip the registration
            return cls

        TOKEN_MAP[pattern] = {
            "cls": cls,
            "is_special": is_special,
        }
        return cls

    return decorator


@register("A")
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


@register("B")
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


@register("C")
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


@register("D")
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


@register("E")
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


@register("F")
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


@register("G")
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


@register("H")
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


@register("I")
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


@register("J")
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


@register("K")
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


@register("L")
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


@register("M")
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


@register("N")
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


@register("O")
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


@register("P")
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


@register("Q")
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


@register("R")
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


@register("S")
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


@register("T")
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


@register("U")
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


@register("V")
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


@register("W")
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


@register("X")
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


@register("Y")
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


@register("Z")
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


@register("<3", is_special=True)
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


@register(" ", is_special=True)
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


@register("@", is_special=True)
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


@register("D:", is_special=True)
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


SPECIAL_TOKENS = {key for key, value in TOKEN_MAP.items() if value["is_special"]}


def tokenize(
    message: str,
    background: str,
    foreground: str,
) -> list[Token]:
    tokens = []

    for segment in message.split(" "):
        if segment in SPECIAL_TOKENS:
            tokens.append(TOKEN_MAP[segment]["cls"](background, foreground))
        else:
            for char in segment:
                try:
                    tokens.append(
                        TOKEN_MAP[char.upper()]["cls"](background, foreground)
                    )
                except KeyError:
                    pass
        tokens.append(TOKEN_MAP[" "]["cls"](background, foreground))

    tokens.pop()  # Remove the last space

    return tokens
