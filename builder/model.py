import pydantic


class EmojiRequest(pydantic.BaseModel):
    message: str
    foreground: str = "💖"
    background: str = "😭"
    width: int = 12
    output: str = "output.txt"
