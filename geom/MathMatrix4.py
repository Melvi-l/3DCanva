from math import cos, sin
from typing import List

from geom.MathMatrix3 import MathMatrix3


class MathMatrix4:
    def __init__(self, 
                 ax=0, bx=0, cx=0, dx=0,
                 ay=0, by=0, cy=0, dy=0,
                 az=0, bz=0, cz=0, dz=0,
                 aw=0, bw=0, cw=0, dw=1
                ) -> None:
        self.ax = ax
        self.bx = bx
        self.cx = cx
        self.dx = dx

        self.ay = ay
        self.by = by
        self.cy = cy
        self.dy = dy

        self.az = az
        self.bz = bz
        self.cz = cz
        self.dz = dz

        self.aw = aw
        self.bw = bw
        self.cw = cw
        self.dw = dw

    @classmethod
    def fromList(cls, listMatrix):

        if len(listMatrix) != 4 or any(len(row) != 4 for row in listMatrix):
            raise ValueError("Must be a 4x4 matrix !")

        matrix = cls()

        matrix.ax, matrix.bx, matrix.cx, matrix.dx = listMatrix[0]
        matrix.ay, matrix.by, matrix.cy, matrix.dy = listMatrix[1]
        matrix.az, matrix.bz, matrix.cz, matrix.dz = listMatrix[2]
        matrix.aw, matrix.bw, matrix.cw, matrix.dw = listMatrix[3]

        return matrix

    # to delete maybe
    @classmethod
    def fromQuaternion(cls, quaternion):
        w, x, y, z = quaternion.w, quaternion.x, quaternion.y, quaternion.z
        return MathMatrix4(
            1 - 2*y**2 - 2*z**2, 2*x*y + 2*w*z, 2*x*z - 2*w*y, 0,
            2*x*y - 2*w*z, 1 - 2*x**2 -2*z**2, 2*y*z + 2*w*x, 0,
            2*x*z + 2*w*y, 2*y*z - 2*w*x, 1 - 2*x**2 - 2*y**2, 0,
            0, 0, 0, 1
        )

    @classmethod
    def scale(matrixClass, scale):
        return matrixClass(
            scale,0,0,0,
            0,scale,0,0,
            0,0,scale,0,
            0,0,0,1
        )
    
    @classmethod
    def translation(matrixClass, translationVector):
        return matrixClass(
            1,0,0,translationVector.x,
            0,1,0,translationVector.y,
            0,0,1,translationVector.z,
            0,0,0,1
        ) 
    
    @classmethod
    def rotation(matrixClass, rotationAxis, angle):
        result = matrixClass(
            rotationAxis.x**2,rotationAxis.x*rotationAxis.y,rotationAxis.x*rotationAxis.z,0,
            rotationAxis.y*rotationAxis.y, rotationAxis.y**2, rotationAxis.y*rotationAxis.z,0,
            rotationAxis.x*rotationAxis.z, rotationAxis.y*rotationAxis.z, rotationAxis.z**2,0,
            0,0,0,0
        )
        result.multiplyScalar(1-cos(angle))
        result.addMatrix(MathMatrix4(
            cos(angle), rotationAxis.z*sin(angle), -rotationAxis.y*sin(angle),0,
            -rotationAxis.z*sin(angle), cos(angle), rotationAxis.x*sin(angle),0,
            rotationAxis.y*sin(angle), -rotationAxis.x*sin(angle), cos(angle),0,
            0,0,0,1
        ))
        return result

    @classmethod
    def identity(matrixClass):
        return matrixClass(
            1,0,0,0,
            0,1,0,0,
            0,0,1,0,
            0,0,0,1
        )

    def getTrace(self):
        return self.ax + self.by +self.cz + self.dw
    def getDeterminant(self) -> float:
        matrixList = self.toList()
        determinant = 0.

        for i in range(4):
            # for j in range(4):
            j=0
            submatrix = [[matrixList[m][n] for n in range(4) if n != j] for m in range(4) if m != i]
            subDeterminant = getSubmatrixDeterminant(submatrix)
            sign = 1 if (i + j) % 2 == 0 else -1
            determinant += sign * matrixList[i][j] * subDeterminant
            # if subDeterminant != 0 and matrixList[i][j] != 0: 
            #     print("sub", matrixList[i][j], subDeterminant)
        return determinant

    def multiplyScalar(self, scalar: float):
        self.ax *= scalar
        self.bx *= scalar
        self.cx *= scalar
        self.dx *= scalar

        self.ay *= scalar
        self.by *= scalar
        self.cy *= scalar
        self.dy *= scalar

        self.az *= scalar
        self.bz *= scalar
        self.cz *= scalar
        self.dz *= scalar

        self.aw *= scalar
        self.bw *= scalar
        self.cw *= scalar
        self.dw *= scalar

        return self

    def multiplyMatrix(self, matrix: 'MathMatrix4'):
        temp = MathMatrix4()
        temp.ax = self.ax * matrix.ax + self.bx * matrix.ay + self.cx * matrix.az + self.dx * matrix.aw
        temp.bx = self.ax * matrix.bx + self.bx * matrix.by + self.cx * matrix.bz + self.dx * matrix.bw
        temp.cx = self.ax * matrix.cx + self.bx * matrix.cy + self.cx * matrix.cz + self.dx * matrix.cw
        temp.dx = self.ax * matrix.dx + self.bx * matrix.dy + self.cx * matrix.dz + self.dx * matrix.dw

        temp.ay = self.ay * matrix.ax + self.by * matrix.ay + self.cy * matrix.az + self.dy * matrix.aw
        temp.by = self.ay * matrix.bx + self.by * matrix.by + self.cy * matrix.bz + self.dy * matrix.bw
        temp.cy = self.ay * matrix.cx + self.by * matrix.cy + self.cy * matrix.cz + self.dy * matrix.cw
        temp.dy = self.ay * matrix.dx + self.by * matrix.dy + self.cy * matrix.dz + self.dy * matrix.dw

        temp.az = self.az * matrix.ax + self.bz * matrix.ay + self.cz * matrix.az + self.dz * matrix.aw
        temp.bz = self.az * matrix.bx + self.bz * matrix.by + self.cz * matrix.bz + self.dz * matrix.bw
        temp.cz = self.az * matrix.cx + self.bz * matrix.cy + self.cz * matrix.cz + self.dz * matrix.cw
        temp.dz = self.az * matrix.dx + self.bz * matrix.dy + self.cz * matrix.dz + self.dz * matrix.dw

        temp.aw = self.aw * matrix.ax + self.bw * matrix.ay + self.cw * matrix.az + self.dw * matrix.aw
        temp.bw = self.aw * matrix.bx + self.bw * matrix.by + self.cw * matrix.bz + self.dw * matrix.bw
        temp.cw = self.aw * matrix.cx + self.bw * matrix.cy + self.cw * matrix.cz + self.dw * matrix.cw
        temp.dw = self.aw * matrix.dx + self.bw * matrix.dy + self.cw * matrix.dz + self.dw * matrix.dw

        self.copy(temp)

        return self

    def addMatrix(self, matrix: 'MathMatrix4'):
        self.ax += matrix.ax
        self.bx += matrix.bx
        self.cx += matrix.cx
        self.dx += matrix.dx

        self.ay += matrix.ay
        self.by += matrix.by
        self.cy += matrix.cy
        self.dy += matrix.dy

        self.az += matrix.az
        self.bz += matrix.bz
        self.cz += matrix.cz
        self.dz += matrix.dz

        self.aw += matrix.aw
        self.bw += matrix.bw
        self.cw += matrix.cw
        self.dw += matrix.dw

        return self

    def getTranspose(self):
        return MathMatrix4 (
            self.ax, self.ay, self.az, self.aw,
            self.bx, self.by, self.bz, self.bw,
            self.cx, self.cy, self.cz, self.cw,
            self.dx, self.dy, self.dz, self.dw
        )

    def getInverse(self) -> 'MathMatrix4':
        # print("get inverse of \n", self)
        determinant = self.getDeterminant()
        # print(determinant) 
        if determinant == 0:
            raise ValueError("InversionError: Null determinant")

        inverse = self.getCofactorMatrix()

        inverse.multiplyScalar(1/determinant)

        return inverse
    
    def getCofactorMatrix(self) -> 'MathMatrix4':
        # print("\n\n\n\n")
        matrixList = self.toList()
        cofactorMatrixList = [[0.0] * 4 for _ in range(4)]
        # print("MATRIX", self)
        for i in range(4):
            for j in range(4):
                # print(f"SUB {i},{j}")
                submatrix = [[matrixList[m][n] for n in range(4) if n != j] for m in range(4) if m != i]
                # print(MathMatrix3.fromList(submatrix))
                submatrixDeterminant = getSubmatrixDeterminant(submatrix)
                sign = 1 if (i + j) % 2 == 0 else -1
                cofactorMatrixList[j][i] = submatrixDeterminant * sign
                # print(MathMatrix4.fromList(cofactorMatrixList))
        # print("\n\n\n\n")
        return MathMatrix4.fromList(cofactorMatrixList)

    def copy(self, matrix: 'MathMatrix4'):    
        self.ax = matrix.ax
        self.bx = matrix.bx
        self.cx = matrix.cx
        self.dx = matrix.dx

        self.ay = matrix.ay
        self.by = matrix.by
        self.cy = matrix.cy
        self.dy = matrix.dy

        self.az = matrix.az
        self.bz = matrix.bz
        self.cz = matrix.cz
        self.dz = matrix.dz

        self.aw = matrix.aw
        self.bw = matrix.bw
        self.cw = matrix.cw
        self.dw = matrix.dw
        return self
    
    def toList(self) -> List[List[float]]:
        return [
            [self.ax, self.bx, self.cx, self.dx],
            [self.ay, self.by, self.cy, self.dy],
            [self.az, self.bz, self.cz, self.dz],
            [self.aw, self.bw, self.cw, self.dw]
        ]

    def __str__(self) -> str:
        return f"Matrix4: [{'{:.2f}'.format(self.ax)}, {'{:.2f}'.format(self.bx)}, {'{:.2f}'.format(self.cx)}, {'{:.2f}'.format(self.dx)}]\n" \
               f"         [{'{:.2f}'.format(self.ay)}, {'{:.2f}'.format(self.by)}, {'{:.2f}'.format(self.cy)}, {'{:.2f}'.format(self.dy)}]\n" \
               f"         [{'{:.2f}'.format(self.az)}, {'{:.2f}'.format(self.bz)}, {'{:.2f}'.format(self.cz)}, {'{:.2f}'.format(self.dz)}]\n" \
               f"         [{'{:.2f}'.format(self.aw)}, {'{:.2f}'.format(self.bw)}, {'{:.2f}'.format(self.cw)}, {'{:.2f}'.format(self.dw)}]"
    
    @staticmethod
    def multiply(matrixA, matrixB):
        result = MathMatrix4()
        
        result.ax = matrixA.ax * matrixB.ax + matrixA.bx * matrixB.ay + matrixA.cx * matrixB.az + matrixA.dx * matrixB.aw
        result.bx = matrixA.ax * matrixB.bx + matrixA.bx * matrixB.by + matrixA.cx * matrixB.bz + matrixA.dx * matrixB.bw
        result.cx = matrixA.ax * matrixB.cx + matrixA.bx * matrixB.cy + matrixA.cx * matrixB.cz + matrixA.dx * matrixB.cw
        result.dx = matrixA.ax * matrixB.dx + matrixA.bx * matrixB.dy + matrixA.cx * matrixB.dz + matrixA.dx * matrixB.dw

        result.ay = matrixA.ay * matrixB.ax + matrixA.by * matrixB.ay + matrixA.cy * matrixB.az + matrixA.dy * matrixB.aw
        result.by = matrixA.ay * matrixB.bx + matrixA.by * matrixB.by + matrixA.cy * matrixB.bz + matrixA.dy * matrixB.bw
        result.cy = matrixA.ay * matrixB.cx + matrixA.by * matrixB.cy + matrixA.cy * matrixB.cz + matrixA.dy * matrixB.cw
        result.dy = matrixA.ay * matrixB.dx + matrixA.by * matrixB.dy + matrixA.cy * matrixB.dz + matrixA.dy * matrixB.dw

        result.az = matrixA.az * matrixB.ax + matrixA.bz * matrixB.ay + matrixA.cz * matrixB.az + matrixA.dz * matrixB.aw
        result.bz = matrixA.az * matrixB.bx + matrixA.bz * matrixB.by + matrixA.cz * matrixB.bz + matrixA.dz * matrixB.bw
        result.cz = matrixA.az * matrixB.cx + matrixA.bz * matrixB.cy + matrixA.cz * matrixB.cz + matrixA.dz * matrixB.cw
        result.dz = matrixA.az * matrixB.dx + matrixA.bz * matrixB.dy + matrixA.cz * matrixB.dz + matrixA.dz * matrixB.dw

        result.aw = matrixA.aw * matrixB.ax + matrixA.bw * matrixB.ay + matrixA.cw * matrixB.az + matrixA.dw * matrixB.aw
        result.bw = matrixA.aw * matrixB.bx + matrixA.bw * matrixB.by + matrixA.cw * matrixB.bz + matrixA.dw * matrixB.bw
        result.cw = matrixA.aw * matrixB.cx + matrixA.bw * matrixB.cy + matrixA.cw * matrixB.cz + matrixA.dw * matrixB.cw
        result.dw = matrixA.aw * matrixB.dx + matrixA.bw * matrixB.dy + matrixA.cw * matrixB.dz + matrixA.dw * matrixB.dw

        return result
    

def getSubmatrixDeterminant(matrix: List[List[float]]):
    return (
            (matrix[0][0] * matrix[1][1] * matrix[2][2] + 
             matrix[0][1] * matrix[1][2] * matrix[2][0] +
             matrix[0][2] * matrix[1][0] * matrix[2][1]) -
            (matrix[2][0] * matrix[1][1] * matrix[0][2] +
             matrix[2][1] * matrix[1][2] * matrix[0][0] +
             matrix[2][2] * matrix[1][0] * matrix[0][1])
           )


    
# print("\n")
# matrixList = [
#     [1, 3, 4],
#     [8, 5, 6],
#     [7, 9, 5],
# ]         
# matrix = MathMatrix3.fromList(matrixList)
# print(matrix)
# det = getSubmatrixDeterminant(matrixList)
# print(det)
