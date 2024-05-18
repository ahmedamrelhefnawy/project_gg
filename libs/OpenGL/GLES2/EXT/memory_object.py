'''OpenGL extension EXT.memory_object

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.memory_object to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/memory_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.memory_object import *
from OpenGL.raw.GLES2.EXT.memory_object import _EXTENSION_NAME

def glInitMemoryObjectEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glGetUnsignedBytevEXT.data size not checked against 'pname'
glGetUnsignedBytevEXT=wrapper.wrapper(glGetUnsignedBytevEXT).setInputArraySize(
    'data', None
)
# INPUT glGetUnsignedBytei_vEXT.data size not checked against 'target'
glGetUnsignedBytei_vEXT=wrapper.wrapper(glGetUnsignedBytei_vEXT).setInputArraySize(
    'data', None
)
# INPUT glDeleteMemoryObjectsEXT.memoryObjects size not checked against n
glDeleteMemoryObjectsEXT=wrapper.wrapper(glDeleteMemoryObjectsEXT).setInputArraySize(
    'memoryObjects', None
)
### END AUTOGENERATED SECTION