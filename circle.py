from manim import *

class TwoCircles(Scene):

    def construct(self):
        axes = ComplexPlane()

        circle1 = Circle(radius=1.4,color=RED)
        circle1.shift(RIGHT*2)

        circle2 = Circle(radius=1.4,color=BLUE)
        circle2.shift(UP*2)

        circle3 = Circle(radius=5,color=RED)
        circle3.shift(RIGHT*2)

        circle4 = Circle(radius=5,color=BLUE)
        circle4.shift(UP*2)

        dot1 = Dot([1,1,0],color=PURPLE)
        dot2 = Dot([-2.45,-2.45,0])
        dot3 = Dot([4.45,4.45,0])

        line1 = Line(start=dot1,end=dot3,color=PURPLE_A)
        line2 = Line(start=dot1,end=dot2,color=PURPLE_B)
        self.play(Create(axes), run_time=3)
        self.play(Create(circle1))
        self.wait(0.5)
        self.play(Create(circle2))
        self.wait(1)
        self.play(Create(dot1))
        self.wait(0.5)
        self.play(Transform(circle1,circle3),Transform(circle2,circle4),Create(line1),Create(line2), run_time=6, rate_func=there_and_back_with_pause)
        self.wait(1)


