from OpenGL.GL import *
from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

class App(Base):
    
    def __init__(self, window_title="App Window"):
        super().__init__(window_title)
        
        vert_code = """
        in vec3 a_position;

        void main()
        {
            gl_Position = vec4(a_position, 1.0);
        }
        """

        frag_code ="""
        out vec4 fragColor;

        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """
        
        self._ProgramRef = OpenGLUtils.initializeProgram(vert_code, frag_code)

        # set custom line width
        glLineWidth(4)
        
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)
        
        position_data = [
            [0.8, 0.0, 0.0],    [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],   [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],  [0.4, -0.6, 0.0]
        ]
        self._VertCount = len(position_data)

        posAttrib = Attribute("vec3", position_data)
        posAttrib.associateVariable(self._ProgramRef, "a_position")
        
    def update(self):
        glUseProgram(self._ProgramRef)
        glDrawArrays(GL_LINE_LOOP, 0, self._VertCount)
        
App().run()