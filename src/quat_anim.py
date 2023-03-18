from manim import *
import math
# manim: https://github.com/ManimCommunity/manim/
# ThreeDScene: https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html

# deg2rad = math.pi/180.0

config.background_color = WHITE

class QuatDefinition(ThreeDScene):
    def construct(self):
        # axes = ThreeDAxes()
        # axes.color = GREY
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        dot = Dot(ORIGIN)
        
        arrow = Arrow3D(start=ORIGIN, end=[0, 0, 2], color=BLUE, thickness=0.03)
        arrowText = Tex(r"$\overrightarrow u$", color=BLUE).scale(1.5).next_to([0, 0, 2], UP, buff=0.1)
        thetaText = Tex(r"$\theta$", color=GOLD).scale(1.5).next_to([-1.5,1.5,0.], UP, buff=0.1)

        self.add_fixed_orientation_mobjects(arrowText, thetaText)

        radius = 2
        arc = Arc(radius=radius, start_angle=0, angle=math.pi, num_components=9, arc_center=[0., 0., 0.], color=GOLD).add_tip()
        
        self.add(dot, arrow, arrowText, arc)


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
        dot_text_a = Tex(r"${}^A p_1$", color=ORANGE).next_to(dot)
        dot_text_b = Tex(r"${}^A p_2$", color=ORANGE).next_to([-0.9,1,1])
        self.add(dot)
        self.add_fixed_orientation_mobjects(dot_text_a)

        # add text
        self.add_fixed_in_frame_mobjects(Text("Active Transformation", color=BLACK).to_corner(DL))
        self.wait(duration=1.0)
        
        # animate rotation
        self.play(Rotate(dot, angle=PI, axis=[0,0,1], about_point=ORIGIN, rate_func=linear),
                  ReplacementTransform(dot_text_a, dot_text_b).set_rate_func(rate_functions.ease_in_quad))
        self.add_fixed_orientation_mobjects(dot_text_b)

        # wait at the end before loop
        self.wait(duration=2.0)

class PassiveTransformation(ThreeDScene):
    def construct(self):
        # create scene 
        # axes = ThreeDAxes()
        # add camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # add axes
        x_axis = Arrow3D(start=ORIGIN, end=[2.0,0,0], color=BLUE_C, thickness=0.03)
        y_axis = Arrow3D(start=ORIGIN, end=[0,2.0,0], color=BLUE_C, thickness=0.03)
        z_axis = Arrow3D(start=ORIGIN, end=[0,0,2.0], color=BLUE_C, thickness=0.03)
        x_text_a = Tex(r"$A_x$", color=BLUE_C).scale(1.5).next_to([2.0,0,0],    aligned_edge=ORIGIN)
        y_text_a = Tex(r"$A_y$", color=BLUE_C).scale(1.5).next_to([0,3.0,0],    aligned_edge=ORIGIN)
        z_text_a = Tex(r"$A_z$", color=BLUE_C).scale(1.5).next_to([0,0,2.5],    aligned_edge=ORIGIN)
        x_text_b = Tex(r"$B_x$", color=BLUE_C).scale(1.5).next_to([-4.0,0,0],   aligned_edge=ORIGIN)
        y_text_b = Tex(r"$B_y$", color=BLUE_C).scale(1.5).next_to([0,-3.0,0],   aligned_edge=ORIGIN)
        z_text_b = Tex(r"$B_z$", color=BLUE_C).scale(1.5).next_to([0,0,2.5],    aligned_edge=ORIGIN)
        self.add(x_axis, y_axis, z_axis)
        self.add_fixed_orientation_mobjects(x_text_a, y_text_a, z_text_a)

        # add dot
        point_start = [1,-1,1]
        dot = Dot3D(point=point_start, color=ORANGE)
        dot_text_a = Tex(r"${}^A p_1$", color=ORANGE).next_to(dot)
        dot_text_b = Tex(r"${}^B p_1$", color=ORANGE).next_to(dot)
        self.add(dot)
        self.add_fixed_orientation_mobjects(dot_text_a)

        # add text
        self.add_fixed_in_frame_mobjects(Text("Passive Transformation", color=BLACK).to_corner(DL))
        
        # animate
        self.wait(duration=1.0)
        self.play(Rotate(x_axis, angle=PI, axis=[0,0,1], about_point=ORIGIN, rate_func=linear),
                  Rotate(y_axis, angle=PI, axis=[0,0,1], about_point=ORIGIN, rate_func=linear),
                  Rotate(z_axis, angle=PI, axis=[0,0,1], about_point=ORIGIN, rate_func=linear),
                  ReplacementTransform(x_text_a, x_text_b),
                  ReplacementTransform(y_text_a, y_text_b),
                  ReplacementTransform(z_text_a, z_text_b), 
                  ReplacementTransform(dot_text_a, dot_text_b))
        
        self.add_fixed_orientation_mobjects(x_text_b, y_text_b, z_text_b, dot_text_b)
        
        # uncomment to animate the color
        # self.play(x_axis.animate.set_color(GREEN),
        #           y_axis.animate.set_color(GREEN),
        #           z_axis.animate.set_color(GREEN))
        
        # wait at the end before loop
        self.wait(duration=2.0)


class QuatConj(ThreeDScene):
    def construct(self):
        # axes
        axes            = ThreeDAxes()
        axes.color      = GREY
        self.add(axes)

        # camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # vector
        vec             = [0, 0, 2]
        dot             = Dot3D(ORIGIN)
        vecEnd          = Dot3D(vec)
        arrow           = Arrow3D(start=ORIGIN, end=vec, color=BLUE)
        arrowText       = Tex(r"$\overrightarrow u$", color=BLUE).scale(1.5).next_to(vecEnd)
        self.add(dot, arrow)
        self.add_fixed_orientation_mobjects(arrowText)
        
        # arcs
        radius = 2
        arc = Arc(radius=radius, start_angle=0, angle=math.pi/2.0, num_components=10, arc_center=[0., 0., 0.], color=GOLD).add_tip()
        arcConj = Arc(radius=radius, start_angle=0, angle=-math.pi/2.0, num_components=10, arc_center=[0., 0., 0.], color=PINK).add_tip()
        self.add(arc, arcConj)
        # arcs text
        thetaText       = Tex(r"$\theta$", color=GOLD).scale(1.5).move_to([1.5,3.0,0.0])
        thetaConjText   = Tex(r"$- \theta$", color=PINK).scale(1.5).move_to([2.0,-2.0,0.0])
        self.add_fixed_orientation_mobjects(thetaText, thetaConjText)

        # quat Text
        quatText        = Tex(r"$q = cos\begin{pmatrix} \frac{\theta}{2} \end{pmatrix} + sin\begin{pmatrix} \frac{\theta}{2} \end{pmatrix} \vec{u}$", color=BLACK).to_corner(RIGHT + DOWN)
        quatConjText    = Tex(r"$q^* = cos\begin{pmatrix} -\frac{\theta}{2} \end{pmatrix} +  sin\begin{pmatrix} -\frac{\theta}{2} \end{pmatrix} \vec{u}$", color=BLACK).to_corner(LEFT + DOWN)
        self.add_fixed_in_frame_mobjects(quatText, quatConjText)
        

class FramesAB(ThreeDScene):
    def construct(self):
        # camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Frame A
        arrow_thickness = 0.03
        unit_length = 2.0
        Ax = Arrow3D(start=ORIGIN, end=[unit_length, 0.0, 0.0], thickness=arrow_thickness, color=BLUE_C)
        Ay = Arrow3D(start=ORIGIN, end=[0.0, unit_length, 0.0], thickness=arrow_thickness, color=BLUE_C)
        Az = Arrow3D(start=ORIGIN, end=[0.0, 0.0, unit_length], thickness=arrow_thickness, color=BLUE_C)
        Ax_text = Tex(r"$A_x ,\; B_x$", color=BLUE_C).move_to([unit_length + 1, 0.0, 0.0])
        Ay_text = Tex(r"$A_y$", color=BLUE_C).move_to([0.0, unit_length + 1, 0.0])
        Az_text = Tex(r"$A_z$", color=BLUE_C).move_to([0.0, 0.0, unit_length + 1])
        self.add(Ax, Ay, Az)
        self.add_fixed_orientation_mobjects(Ax_text, Ay_text, Az_text)

        # Frame B
        By = Arrow3D(start=ORIGIN, end=[0.0, math.sqrt(unit_length**2/2.0), -math.sqrt(unit_length**2/2.0)], thickness=arrow_thickness, color=GOLD)
        Bz = Arrow3D(start=ORIGIN, end=[0.0, math.sqrt(unit_length**2/2.0), math.sqrt(unit_length**2/2.0)], thickness=arrow_thickness, color=GOLD)
        By_text = Tex(r"$B_y$", color=GOLD).move_to([0.0, unit_length, -unit_length])
        Bz_text = Tex(r"$B_z$", color=GOLD).next_to([0.0, unit_length+0.25, unit_length+0.25])
        self.add(By, Bz)
        self.add_fixed_orientation_mobjects(By_text, Bz_text)


class VecB(ThreeDScene):
    def construct(self):
        # axes
        # axes            = ThreeDAxes()
        # axes.color      = GREY
        # self.add(axes)

        # camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Frame B
        arrow_thickness = 0.015
        unit_length = 2.0
        Bx = Arrow3D(start=ORIGIN, end=[unit_length, 0.0, 0.0], thickness=arrow_thickness, color=GOLD)
        By = Arrow3D(start=ORIGIN, end=[0.0, math.sqrt(unit_length**2/2.0), -math.sqrt(unit_length**2/2.0)], thickness=arrow_thickness, color=GOLD)
        Bz = Arrow3D(start=ORIGIN, end=[0.0, math.sqrt(unit_length**2/2.0), math.sqrt(unit_length**2/2.0)], thickness=arrow_thickness, color=GOLD)
        Bx_text = Tex(r"$B_x$", color=GOLD).move_to([unit_length + 1, 0.0, 0.0])
        By_text = Tex(r"$B_y$", color=GOLD).move_to([0.0, unit_length, -unit_length])
        Bz_text = Tex(r"$B_z$", color=GOLD).next_to([0.0, unit_length+0.25, unit_length+0.25])
        self.add(Bx, By, Bz)
        self.add_fixed_orientation_mobjects(Bx_text, By_text, Bz_text)

        # vecB
        vec_length = 1.0
        vecB = Arrow3D(start=ORIGIN, end=[0.0, math.sqrt(vec_length**2/2.0), math.sqrt(vec_length**2/2.0)], thickness=arrow_thickness*2, color=RED)
        vecBText = Tex(r"${}^B\vec{v}$", color=RED).move_to([0.0, 0.25, 1.0])
        self.add(vecB)
        self.add_fixed_orientation_mobjects(vecBText)


class VecA(ThreeDScene):
    def construct(self):
        # axes
        # axes            = ThreeDAxes()
        # axes.color      = GREY
        # self.add(axes)

        # camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Frame B
        arrow_thickness = 0.015
        unit_length = 2.0
        Ax = Arrow3D(start=ORIGIN, end=[unit_length, 0.0, 0.0], thickness=arrow_thickness, color=BLUE_C)
        Ay = Arrow3D(start=ORIGIN, end=[0.0, unit_length, 0.0], thickness=arrow_thickness, color=BLUE_C)
        Az = Arrow3D(start=ORIGIN, end=[0.0, 0.0, unit_length], thickness=arrow_thickness, color=BLUE_C)
        Ax_text = Tex(r"$A_x$", color=BLUE_C).move_to([unit_length + 1, 0.0, 0.0])
        Ay_text = Tex(r"$A_y$", color=BLUE_C).move_to([0.0, unit_length + 1, 0.0])
        Az_text = Tex(r"$A_z$", color=BLUE_C).move_to([0.0, 0.0, unit_length + 1])
        self.add(Ax, Ay, Az)
        self.add_fixed_orientation_mobjects(Ax_text, Ay_text, Az_text)

        # vecB
        vec_length = 1.0
        vecB = Arrow3D(start=ORIGIN, end=[0.0, math.sqrt(vec_length**2/2.0), math.sqrt(vec_length**2/2.0)], thickness=arrow_thickness*2, color=RED)
        vecBText = Tex(r"${}^A\vec{v}$", color=RED).move_to([0.0, 1.25, 1.0])
        self.add(vecB)
        self.add_fixed_orientation_mobjects(vecBText)