from OpenGL.GL import *
import numpy

class Attribute():
    
    def __init__(self, data_type, data):
        
        # allowed data types
        # int | float | vec2 | vec3 | vec4
        self._DataType = data_type
        
        # data for buffer
        self._Data = data
        
        # generate buffer
        self._BufferReference = glGenBuffers(1)
        
        # upload data to GPU
        self.uploadData()
        
    def uploadData(self):
        
        # convert data to numpy format
        data = numpy.array(self._Data).astype(numpy.float32)

        # select appropriate buffer for data
        glBindBuffer(GL_ARRAY_BUFFER, self._BufferReference)

        # store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        
    def associateVariable(self, program_ref, variable_name):
        
        # get reference for program variable with given name
        variable_ref = glGetAttribLocation(program_ref, variable_name)
        
        # exit if program does not reference variable
        if variable_ref == -1:
            return
        
        # select buffer
        glBindBuffer(GL_ARRAY_BUFFER, self._BufferReference)

        # specify how data in handled from currently bound buffer
        if self._DataType == "int":
            glVertexAttribPointer(variable_ref, 1, GL_INT, GL_FALSE, 0, None)
        elif self._DataType == "float":
            glVertexAttribPointer(variable_ref, 1, GL_FLOAT, GL_FALSE, 0, None)
        elif self._DataType == "vec2":
            glVertexAttribPointer(variable_ref, 2, GL_FLOAT, GL_FALSE, 0, None)
        elif self._DataType == "vec3":
            glVertexAttribPointer(variable_ref, 3, GL_FLOAT, GL_FALSE, 0, None)
        elif self._DataType == "vec4":
            glVertexAttribPointer(variable_ref, 4, GL_FLOAT, GL_FALSE, 0, None)
        else:
            raise Exception(f"Attribute {variable_name} has unknown type {self._DataType}")
        
        # stream data to variable
        glEnableVertexAttribArray(variable_ref)