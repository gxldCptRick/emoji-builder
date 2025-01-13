from .base import Token, register


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
                [0, 0, 0, 0, 0, 0],
            ],
        )
