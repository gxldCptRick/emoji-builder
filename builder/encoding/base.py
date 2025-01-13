"""
Base module for all tokens that can transforms a string into an emoji
All characters we transform create their own subclass of Token.

We also have a registry where we manage the tokens and allow you to map your own tokens to encode messages you want.
"""

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
