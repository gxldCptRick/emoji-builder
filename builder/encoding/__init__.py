from .base import TOKEN_MAP, Token

import builder.encoding.emojis  # pull this in so that we register them.
import builder.encoding.letters  # pull this in so that we register them.
import builder.encoding.symbols  # pull this in so that we register them.


def tokenize(
    message: str,
    background: str,
    foreground: str,
) -> list[Token]:
    # doing this in case we update this after the module has been imported i.e. if someone extends it.
    special_tokens = {key for key, value in TOKEN_MAP.items() if value["is_special"]}

    tokens = []

    for segment in message.split(" "):
        if segment in special_tokens:
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


__all__ = [
    "tokenize",
    "Token",
    "base",
    "emojis",
    "letters",
    "symbols",
]
