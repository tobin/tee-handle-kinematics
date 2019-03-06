class Quaternion():
    def __init__(self, qdata=None):
        self.q = np.zeros(4)
        if qdata is None:
            pass
        elif np.isscalar(qdata):
            self.q[0] = qdata
        elif len(qdata) == 3:
            self.q[1:4] = qdata
        elif len(qdata) == 4:
            self.q = qdata
        # TODO(tobin): Throw an exception in other cases.

    def conj(self):
        return Quaternion(np.array([1, -1, -1, -1]) * self.q)

    def inv(self):
        return self.conj() / np.dot(self.q, self.q)

    def __getitem__(self, index):
        return self.q[index]

    def __div__(self, other):
        if np.isscalar(other):
            return Quaternion(self.q / other)
        elif np.instance(other, Quaternion):
            return self * other.inv()

    def __mul__(self, other):
        if np.isscalar(other):
            return Quaternion(self.q * other)
        elif isinstance(other, Quaternion):
            # https://en.wikipedia.org/wiki/Quaternion#Hamilton_product
            a = self
            b = other
            return Quaternion([
                a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3],
                a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2],
                a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1],
                a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]]
            )

    def __abs__(self):
        return np.sqrt(np.dot(self.q, self.q))

    def __str__(self):
        return "quat(" + self.q.__str__() + ")"

    __repr__ = __str__
