from manim import *

class TwoCircles(Scene):
    def construct(self):
        axes = ComplexPlane()

        circle1 = Circle(radius=1.4,color=RED)
        circle1.shift(RIGHT*2)

        circle2 = Circle(radius=1.4,color=BLUE)
        circle2.shift(UP*2)
        ######################################
        circle3 = Circle(radius=5,color=RED)
        circle3.shift(RIGHT*2)

        circle4 = Circle(radius=5,color=BLUE)
        circle4.shift(UP*2)
        ######################################

        circle5 = Circle(radius=1.4,color=RED)
        circle5.shift(RIGHT*4)

        circle6 = Circle(radius=1.4,color=BLUE)
        circle6.shift(UP*4)
        ######################################

        circle7 = Circle(radius=2.83,color=RED)
        circle7.shift(RIGHT*4)

        circle8 = Circle(radius=2.83,color=BLUE)
        circle8.shift(UP*4)
        ######################################

        circle9 = Circle(radius=10,color=RED)
        circle9.shift(RIGHT*4)

        circle10 = Circle(radius=10,color=BLUE)
        circle10.shift(UP*4)
        ######################################
        dot = Dot([1,1,0],color=PURPLE)

        linepath = Line([1,1,0],[2,2,0])

        line1 = Line(start=[1,1,0],end=[-2.45,-2.45,0],color=PURPLE_A)
        line2 = Line(start=[1,1,0],end=[4.45,4.45,0],color=PURPLE_B)

        line11 = Line(start=[2,2,0],end=[-5,-5,0],color=PURPLE_A)
        line22 = Line(start=[2,2,0],end=[10,10,0],color=PURPLE_B)

        self.play(Create(axes), run_time=3)
        self.play(Create(circle1))
        self.wait(0.5)
        self.play(Create(circle2))
        self.wait(1)
        self.play(Create(dot))
        self.wait(0.5)
        self.play(Transform(circle1,circle3),Transform(circle2,circle4),Create(line1),Create(line2), run_time=6, rate_func=there_and_back_with_pause)
        self.wait(1)

        self.play(Transform(circle1,circle5),Transform(circle2,circle6),run_time=3)
        self.play(Transform(circle1,circle7),Transform(circle2,circle8),run_time=3)
        self.play(MoveAlongPath(dot,linepath),run_time=2)
        self.play(Transform(circle1,circle9),Transform(circle2,circle10),Create(line11),Create(line22),run_time=6, rate_func=there_and_back_with_pause)
        self.wait(1)

        self.play(Transform(circle1,Circle(radius=1.4,color=RED).shift(RIGHT*2)),Transform(circle2,Circle(radius=1.4,color=BLUE).shift(UP*2)),FadeOut(dot))
        self.wait(0.5)

        self.play(circle1.animate.shift(LEFT),circle2.animate.shift(LEFT))
        self.wait(0.5)
        self.play(Create(Dot([0,1,0],color=PURPLE)))
        self.play(Transform(circle1,Circle(radius=5,color=RED).shift(RIGHT)),Transform(circle2,Circle(radius=5,color=BLUE).shift(LEFT,UP*2)))
        self.wait(2)