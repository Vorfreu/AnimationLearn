from manim import *

class TwoCircles(Scene):
    def construct(self):
        axes = ComplexPlane()
        circle0 = Circle(radius=1.4,color=RED)
        circle00 = Circle(radius=1.4,color=BLUE)

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

        circle11 = Circle(radius=1.4,color=RED)
        circle11.shift(DOWN)
        ######################################

        circle12 = Circle(radius=1.58,color=RED)
        circle12.shift(DOWN)

        circle13 = Circle(radius=1.58,color=BLUE)
        circle13.shift(UP*2).shift(LEFT)
        ######################################

        circle14 = Circle(radius=5,color=RED)
        circle14.shift(DOWN)

        circle15 = Circle(radius=5,color=BLUE)
        circle15.shift(UP*2).shift(LEFT)
        ######################################

        dot = Dot([1,1,0],color=PURPLE)
        dot2 = Dot([0,1,0],color=PURPLE)

        linepath = Line([1,1,0],[2,2,0])
        linepath2 = Line([0,1,0],[-0.5,0.5,0])

        line1 = Line(start=[1,1,0],end=[-2.40,-2.40,0],color=PURPLE_A)
        line2 = Line(start=[1,1,0],end=[4.40,4.40,0],color=PURPLE_B)

        line11 = Line(start=[2,2,0],end=[-5,-5,0],color=PURPLE_A)
        line22 = Line(start=[2,2,0],end=[10,10,0],color=PURPLE_B)

        line111 = Line(start=[0,1,0],end=[-3.40,-2.40,0],color=PURPLE_A)
        line222 = Line(start=[0,1,0],end=[3.40,4.40,0],color=PURPLE_B)

        line1111 = Line(start=[-0.5,0.5,0],end=[4,2,0],color=PURPLE_A)
        line2222 = Line(start=[-0.5,0.5,0],end=[-5,-1,0],color=PURPLE_B)

        frame = PictureInPictureFrame(height=2,aspect_ratio=3.5,fill_opacity=0.7).shift(LEFT*4).shift(UP*2)

        equation1 = Text('||Z|| = ||Z||',color=BLACK,fill_opacity=0.7).shift(LEFT*4).shift(UP*2)
        equation2 = Text('||Z-k|| = ||Z-ki||',color=BLACK,fill_opacity=0.7).shift(LEFT*4).shift(UP*2)
        equation3 = Text('||Z-m|| = ||Z+m-i2m||',color=BLACK,fill_opacity=0.7).shift(LEFT*4).shift(UP*2)
        equation4 = Text('||Z+mi|| = ||Z+m-i2m||', color=BLACK, fill_opacity=0.7).shift(LEFT * 4).shift(UP * 2)

        self.play(Create(axes), run_time=3)
        self.play(Create(circle0),Create(circle00))
        self.wait(0.5)
        self.play(Create(frame))
        self.wait(1)
        self.play(Write(equation1))
        self.wait(1)
        self.play(Transform(circle0,circle1),Transform(circle00,circle2),Transform(equation1,equation2),run_time=3)
        self.play(Create(dot))
        self.wait(0.5)
        self.play(Transform(circle0,circle3),Transform(circle00,circle4),Create(line1),Create(line2), run_time=6, rate_func=there_and_back_with_pause)
        self.wait(1)

        self.play(Transform(circle0,circle5),Transform(circle00,circle6),run_time=3)
        self.wait(0.5)
        self.play(Transform(circle0,circle7),Transform(circle00,circle8),run_time=3)
        self.wait(0.5)
        self.play(MoveAlongPath(dot,linepath),run_time=2)
        self.wait(0.5)
        self.play(Transform(circle0,circle9),Transform(circle00,circle10),Create(line11),Create(line22),run_time=6, rate_func=there_and_back_with_pause)
        self.wait(1)

        self.play(Transform(circle0,Circle(radius=1.4,color=RED).shift(RIGHT*2)),Transform(circle00,Circle(radius=1.4,color=BLUE).shift(UP*2)),FadeOut(dot))
        self.wait(0.5)

        self.play(circle0.animate.shift(LEFT),circle00.animate.shift(LEFT),Transform(equation1,equation3))
        self.wait(0.5)
        self.play(Create(dot2))
        self.wait(0.5)
        self.play(Transform(circle0,Circle(radius=5,color=RED).shift(RIGHT)),Transform(circle00,Circle(radius=5,color=BLUE).shift(LEFT,UP*2)),Create(line111),Create(line222),run_time=6, rate_func=there_and_back_with_pause)
        self.wait(0.5)

        self.play(Transform(circle0,circle11),Transform(equation1,equation4))
        self.wait(0.5)

        self.play(Transform(circle0,circle12),Transform(circle00,circle13))
        self.wait(0.5)

        self.play(MoveAlongPath(dot2,linepath2),run_time=2)
        self.wait(0.5)

        self.play(Transform(circle0,circle14),Transform(circle00,circle15),Create(line1111),Create(line2222),run_time=6, rate_func=there_and_back_with_pause)
        self.wait(2)