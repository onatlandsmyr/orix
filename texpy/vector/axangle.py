import numpy as np

from .vector3d import Vector3d
from texpy.quaternion.rotation import Rotation
from texpy.scalar.scalar import Scalar


class AxAngle(Vector3d):

    @property
    def angle(self):
        return self.norm

    @property
    def axis(self):
        u = self.unit
        u[u.norm.data == 0] = Vector3d.xvector()
        return u

    def to_rotation(self):
        s = np.sin(self.angle.data / 2)
        a = np.cos(self.angle.data / 2)
        b = s * self.axis.x.data
        c = s * self.axis.y.data
        d = s * self.axis.z.data
        r = Rotation(np.stack([a, b, c, d], axis=-1))
        return r

    @classmethod
    def from_axes_angles(cls, axes, angles):
        axes = Vector3d(axes).unit
        angles = np.array(angles)
        axangle_data = angles[..., np.newaxis] * axes.data
        return AxAngle(axangle_data)
