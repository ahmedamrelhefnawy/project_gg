'''OpenGL extension NV.deep_texture3D

This module customises the behaviour of the 
OpenGL.raw.GL.NV.deep_texture3D to provide a more 
Python-friendly API

Overview (from the spec)
	
	Some applications require 3D textures that have a significant number of
	slices, but less resolution in width and height. In the current spec, the
	maximum value for the size of all three dimensions is specified by a
	single value. This extension adds a second set of limits against which 3D
	textures can be checked if an application needs deeper textures than would
	be allowed by the symmetric texture limits.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/deep_texture3D.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.deep_texture3D import *
from OpenGL.raw.GL.NV.deep_texture3D import _EXTENSION_NAME

def glInitDeepTexture3DNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION