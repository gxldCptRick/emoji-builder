from .base import Token, register


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
                [0, 0, 0, 0, 0, 0],
            ],
        )
