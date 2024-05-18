'''OpenGL extension EXT.coordinate_frame

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.coordinate_frame to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows specifying a per-vertex tangent and binormal
	vector in addition to the normal vector, defining a coordinate frame.
	The coordinate frame is used in additional extensions which also build
	on fragment lighting to achieve bump mapping.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/coordinate_frame.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.coordinate_frame import *
from OpenGL.raw.GL.EXT.coordinate_frame import _EXTENSION_NAME

def glInitCoordinateFrameEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glTangent3bvEXT=wrapper.wrapper(glTangent3bvEXT).setInputArraySize(
    'v', 3
)
glTangent3dvEXT=wrapper.wrapper(glTangent3dvEXT).setInputArraySize(
    'v', 3
)
glTangent3fvEXT=wrapper.wrapper(glTangent3fvEXT).setInputArraySize(
    'v', 3
)
glTangent3ivEXT=wrapper.wrapper(glTangent3ivEXT).setInputArraySize(
    'v', 3
)
glTangent3svEXT=wrapper.wrapper(glTangent3svEXT).setInputArraySize(
    'v', 3
)
glBinormal3bvEXT=wrapper.wrapper(glBinormal3bvEXT).setInputArraySize(
    'v', 3
)
glBinormal3dvEXT=wrapper.wrapper(glBinormal3dvEXT).setInputArraySize(
    'v', 3
)
glBinormal3fvEXT=wrapper.wrapper(glBinormal3fvEXT).setInputArraySize(
    'v', 3
)
glBinormal3ivEXT=wrapper.wrapper(glBinormal3ivEXT).setInputArraySize(
    'v', 3
)
glBinormal3svEXT=wrapper.wrapper(glBinormal3svEXT).setInputArraySize(
    'v', 3
)
# INPUT glTangentPointerEXT.pointer size not checked against 'type,stride'
glTangentPointerEXT=wrapper.wrapper(glTangentPointerEXT).setInputArraySize(
    'pointer', None
)
# INPUT glBinormalPointerEXT.pointer size not checked against 'type,stride'
glBinormalPointerEXT=wrapper.wrapper(glBinormalPointerEXT).setInputArraySize(
    'pointer', None
)
### END AUTOGENERATED SECTION