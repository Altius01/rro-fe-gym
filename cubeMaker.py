from enum import Enum
from panda3d.core import LVecBase4f
from panda3d.egg import EggPolygon, EggVertexPool, EggData, EggVertex, loadEggData, EggCoordinateSystem
from panda3d.core import GeomVertexFormat, GeomVertexData, GeomVertexWriter, GeomTriangles, Geom, GeomNode, NodePath, GeomPoints

class Color(Enum):
    WHITE = LVecBase4f(1.0, 1.0, 1.0, 1.0)
    BLACK = LVecBase4f(0.0, 0.0, 0.0, 1.0)
    RED = LVecBase4f(238.0/255, 39.0/255, 55.0/255, 1.0)
    GREEN = LVecBase4f(68.0/255, 214.0/255, 44.0/255, 1.0)


class CubeMaker:
    def __init__(self, color: Color):
        # self.smooth = True/False
        # self.uv = True/False or Spherical/Box/...
        self.color = color
        # self.subdivide = 0/1/2/...
        self.size = 1.0

    def generate(self):
        format = GeomVertexFormat.getV3()
        data = GeomVertexData("Data", format, Geom.UHStatic)
        vertices = GeomVertexWriter(data, "vertex")

        size = self.size
        vertices.addData3f(-size, -size, -2*size)
        vertices.addData3f(+size, -size, -2*size)
        vertices.addData3f(-size, +size, -2*size)
        vertices.addData3f(+size, +size, -2*size)
        vertices.addData3f(-size, -size, +2*size)
        vertices.addData3f(+size, -size, +2*size)
        vertices.addData3f(-size, +size, +2*size)
        vertices.addData3f(+size, +size, +2*size)

        triangles = GeomTriangles(Geom.UHStatic)

        def addQuad(v0, v1, v2, v3):
            triangles.addVertices(v0, v1, v2)
            triangles.addVertices(v0, v2, v3)
            triangles.closePrimitive()

        addQuad(4, 5, 7, 6) # Z+
        addQuad(0, 2, 3, 1) # Z-
        addQuad(3, 7, 5, 1) # X+
        addQuad(4, 6, 2, 0) # X-
        addQuad(2, 6, 7, 3) # Y+
        addQuad(0, 1, 5, 4) # Y+

        geom = Geom(data)
        geom.addPrimitive(triangles)

        node = GeomNode("CubeMaker")
        node.addGeom(geom)

        node_path = NodePath(node)
        node_path.setColor(self.color.value)
        return node_path

class GroundMaker:
    def __init__(self, color: Color, size = 1.0):
        # self.smooth = True/False
        # self.uv = True/False or Spherical/Box/...
        self.color = color
        # self.subdivide = 0/1/2/...
        self.size = size

    def generate(self):
        format = GeomVertexFormat.getV3()
        data = GeomVertexData("Data", format, Geom.UHStatic)
        vertices = GeomVertexWriter(data, "vertex")

        size = self.size
        vertices.addData3f(-size, -size, 0.0)
        vertices.addData3f(+size, -size, 0.0)
        vertices.addData3f(-size, +size, 0.0)
        vertices.addData3f(+size, +size, 0.0)

        triangles = GeomTriangles(Geom.UHStatic)

        def addQuad(v0, v1, v2, v3):
            triangles.addVertices(v0, v1, v2)
            triangles.addVertices(v0, v2, v3)
            triangles.closePrimitive()

        addQuad(1, 3, 2, 0)

        geom = Geom(data)
        geom.addPrimitive(triangles)

        node = GeomNode("GroundMaker")
        node.addGeom(geom)

        node_path = NodePath(node)
        node_path.setColor(self.color.value)
        return node_path