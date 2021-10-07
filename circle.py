from manim import *

class TwoCircles(Scene):
    def construct(self):
        axes = Axes(
            # x_range=[-50,10],
            # y_range=[-10,10],
            # tips=False,
        )

        circle1 = Circle(radius=1.4,color=RED)
        circle1.shift(RIGHT*2)

        circle2 = Circle(radius=1.4,color=BLUE)
        circle2.shift(UP*2)

        circle3 = Circle(radius=5,color=RED)
        circle3.shift(RIGHT*2)

        circle4 = Circle(radius=5,color=BLUE)
        circle4.shift(UP*2)

        self.add(axes)
        self.play(Create(circle1))  # show the circle on screen
        self.wait(0.5)
        self.play(Create(circle2))
        self.wait(1)
        self.play(Transform(circle1,circle3),Transform(circle2,circle4), run_time=4, rate_func=linear)
        self.wait(1)