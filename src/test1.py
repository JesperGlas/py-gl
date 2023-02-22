import glfw
from OpenGL.GL import *
import numpy as np
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute

VERT_SRC = """
in vec3 a_position;

void main()
{
    gl_Position = vec4(a_position, 1.0);
}
"""

FRAG_SRC ="""
out vec4 fragColor;

void main()
{
    fragColor = vec4(1.0, 1.0, 0.0, 1.0);
}
"""

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)
    
    # scene
    program_ref = OpenGLUtils.initializeProgram(VERT_SRC, FRAG_SRC)
    
    glLineWidth(4)
    
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    
    position_data = [
        [0.8, 0.0, 0.0],    [0.4, 0.6, 0.0],
        [-0.4, 0.6, 0.0],   [-0.8, 0.0, 0.0],
        [-0.4, -0.6, 0.0],  [0.4, -0.6, 0.0]
    ]
    vert_count = len(position_data)

    posAttrib = Attribute("vec3", position_data)
    posAttrib.associateVariable(program_ref, "a_position")
    
    glUseProgram(program_ref)
    
    glClearColor(0, 0.1, 0.1, 1)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_LINE_LOOP, 0, vert_count)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()