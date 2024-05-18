'''OpenGL extension EXT.misc_attribute

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.misc_attribute to provide a more 
Python-friendly API

Overview (from the spec)
	
	EXT_misc_attribute extends the list of attribute groups. It provides
	a miscellaneous group, controlled by the MISC_BIT_EXT bit, that contains
	the attribute state of extensions that don't logically fit in any other
	group. 

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/misc_attribute.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.misc_attribute import *
from OpenGL.raw.GL.EXT.misc_attribute import _EXTENSION_NAME

def glInitMiscAttributeEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION