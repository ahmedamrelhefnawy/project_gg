'''OpenGL extension EXT.draw_buffers2

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.draw_buffers2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension builds upon the ARB_draw_buffers extension and provides
	separate blend enables and color write masks for each color output.  In
	ARB_draw_buffers (part of OpenGL 2.0), separate values can be written to
	each color buffer, but the blend enable and color write mask are global
	and apply to all color outputs.
	
	While this extension does provide separate blend enables, it does not
	provide separate blend functions or blend equations per color output.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/draw_buffers2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.draw_buffers2 import *
from OpenGL.raw.GL.EXT.draw_buffers2 import _EXTENSION_NAME

def glInitDrawBuffers2EXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGetBooleanIndexedvEXT=wrapper.wrapper(glGetBooleanIndexedvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='target',orPassIn=True
)
glGetIntegerIndexedvEXT=wrapper.wrapper(glGetIntegerIndexedvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='target',orPassIn=True
)
### END AUTOGENERATED SECTION