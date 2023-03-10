from manim import *
import math
# manim: https://github.com/ManimCommunity/manim/
# ThreeDScene: https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html

# deg2rad = math.pi/180.0

class QuatDefinition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        origin = [0, 0, 0]
        vec = [0, 0, 2]
        dot = Dot(origin)
        vecEnd = Dot(vec)
        arrow = Arrow(origin, vec, buff=0, color=BLUE)
        arrowText = Tex(r"$\overrightarrow u$", color=BLUE).scale(1.5).next_to(vecEnd, UP, buff=0.1)
        thetaText = Tex(r"$\theta$", color=GOLD).scale(1.5).next_to([-1.5,1.5,0.], UP, buff=0.1)

        self.add_fixed_orientation_mobjects(arrowText)
        self.add_fixed_orientation_mobjects(thetaText)

        radius = 2
        arc = Arc(radius=radius, start_angle=0, angle=math.pi, num_components=9, arc_center=[0., 0., 0.], color=GOLD).add_tip()
        
        self.add(axes, dot, arrow, arrowText, arc)
        # self.play(Create(arc))


class ActiveTransformation(ThreeDScene):
    def construct(self):
        # create scene 
        # axes = ThreeDAxes()
        # add camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # add axes
        x_axis = Arrow3D(start=ORIGIN, end=[2.0,0,0], color=BLUE_C, thickness=0.03)
        y_axis = Arrow3D(start=ORIGIN, end=[0,2.0,0], color=BLUE_C, thickness=0.03)
        z_axis = Arrow3D(start=ORIGIN, end=[0,0,2.0], color=BLUE_C, thickness=0.03)
        x_text = Tex(r"$A_x$", color=BLUE_C).scale(1.5).next_to([2.0,0,0])
        y_text = Tex(r"$A_y$", color=BLUE_C).scale(1.5).next_to([0,3.0,0])
        z_text = Tex(r"$A_z$", color=BLUE_C).scale(1.5).next_to([0,0,2.5])
        self.add(x_axis, y_axis, z_axis)
        self.add_fixed_orientation_mobjects(x_text, y_text, z_text)

        
        
        # add dot
        point_start = [1,-1,1]
        dot = Dot3D(point=point_start, color=ORANGE)
        self.add(dot)

        # add text
        self.add_fixed_in_frame_mobjects(Text("Active Transformation").to_corner(DL))
        
        # animate
        self.play(Rotate(dot, angle=PI, axis=[0,0,1], about_point=ORIGIN, rate_func=linear))
        self.wait(duration=2.0)
