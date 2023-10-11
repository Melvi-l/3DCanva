from typing import List


class MathMatrix3:
    def __init__(self, 
                ax=0, bx=0, cx=0,
                ay=0, by=0, cy=0,
                az=0, bz=0, cz=0,
        ):
        self.ax = ax
        self.bx = bx
        self.cx = cx

        self.ay = ay
        self.by = by
        self.cy = cy

        self.az = az
        self.bz = bz
        self.cz = cz

    @classmethod
    def fromList(cls, listMatrix):

        if len(listMatrix) != 3 or any(len(row) != 3 for row in listMatrix):
            raise ValueError("Must be a 4x4 matrix !")

        matrix = cls()

        matrix.ax, matrix.bx, matrix.cx = listMatrix[0]
        matrix.ay, matrix.by, matrix.cy = listMatrix[1]
        matrix.az, matrix.bz, matrix.cz = listMatrix[2]

        return matrix
        
    def toList(self) -> List[List[float]]:
        return [
            [self.ax, self.bx, self.cx],
            [self.ay, self.by, self.cy],
            [self.az, self.bz, self.cz],
        ]
    
    
    def __str__(self) -> str:
        return f"Matrix3: [{'{:.2f}'.format(self.ax)}, {'{:.2f}'.format(self.bx)}, {'{:.2f}'.format(self.cx)}]\n" \
               f"         [{'{:.2f}'.format(self.ay)}, {'{:.2f}'.format(self.by)}, {'{:.2f}'.format(self.cy)}]\n" \
               f"         [{'{:.2f}'.format(self.az)}, {'{:.2f}'.format(self.bz)}, {'{:.2f}'.format(self.cz)}]"
    