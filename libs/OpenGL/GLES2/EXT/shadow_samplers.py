'''OpenGL extension EXT.shadow_samplers

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.shadow_samplers to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension supports comparing the texture R coordinate to a depth
	texture value returning the result as a float value in the range [0,1]. 
	This can be used to implement shadow maps.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/shadow_samplers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.shadow_samplers import *
from OpenGL.raw.GLES2.EXT.shadow_samplers import _EXTENSION_NAME

def glInitShadowSamplersEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION