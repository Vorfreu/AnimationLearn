from manim import *

class Eliptic(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        elips = Surface(
            lambda u, v: np.array([
                3 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes), run_time=3)
        self.wait(2)
        self.play(Create(elips))
        self.wait(3)
