from manim import *

class TwoCircles(Scene):
    def construct(self):
        axes = ComplexPlane().add_coordinates()


        circle1 = Circle(radius=1.4,color=RED)
        circle1.shift(RIGHT*2)

        circle2 = Circle(radius=1.4,color=BLUE)
        circle2.shift(UP*2)

        circle3 = Circle(radius=5,color=RED)
        circle3.shift(RIGHT*2)

        circle4 = Circle(radius=5,color=BLUE)
        circle4.shift(UP*2)

        line1 = Line(start=([-3,-3,0]),end=([3,3,0]))

        self.add(axes,line1)
        self.play(Create(circle1))  # show the circle on screen
        self.wait(0.5)
        self.play(Create(circle2))
        self.wait(1)
        self.play(Transform(circle1,circle3),Transform(circle2,circle4), run_time=6, rate_func=there_and_back_with_pause)
        self.wait(1)