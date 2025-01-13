"""
Module containing the logic to parse a string into token objects which can then be used to print out the emojified version of the message.

**Functions**
- `tokenize(message: str, background: str, foreground: str) -> list[Token]`: Transforms a string into a list of Token objects which can be used to render into emojis.

**Classes**
- `Token`: Base class for all token objects. This class is abstract and should not be used directly.

**Examples**

```python
import builder.encoding

tokens = builder.encoding.tokenize(
    message="Some Message",
    background="😭",
    foreground="💖",
)

for token in tokens:
    print(token.render(width=12))
```
"""

from .base import TOKEN_MAP, Token

import builder.encoding.emojis  # pull this in so that we register them.
import builder.encoding.letters  # pull this in so that we register them.
import builder.encoding.symbols  # pull this in so that we register them.


def tokenize(
    message: str,
    background: str,
    foreground: str,
) -> list[Token]:
    """Transforms a string into a list of Token objects which can be used to render into emojis.

    **Parameters**
    - message (`str`): Message we are breaking down.
    - background (`str`): string we will use as the background.
    - foreground (`str`): string we will use as the foreground.

    **Returns**
    - list[`Token`]: The tokens created configured with the background and foreground already.
    """
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
