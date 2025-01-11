# creates a circle that always faces the camera

from manim import *

class AlwaysFaceCamera(ThreeDScene):
    def construct(self):
        np = NumberPlane()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)  # slow rotation
        self.play(Create(np))

        circle = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)
        circle.move_to([0, 0, 1])
        circle.rotate(angle=90 * DEGREES, axis=[0, 1, 0])

        circle.saved_state = circle.copy()

        def face_camera(mob, dt):
            mob.become(mob.saved_state)
            mob.rotate(-self.renderer.camera.get_theta(), axis=UP)
            mob.rotate(self.renderer.camera.get_phi(), axis=LEFT)

        circle.add_updater(face_camera)
        self.add(circle)

        self.wait(20)
