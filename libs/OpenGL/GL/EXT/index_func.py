'''OpenGL extension EXT.index_func

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.index_func to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a way to discard fragments when a comparison
	between the fragment's index value and a reference index fails.  This
	may be used similarly to the alpha test which is available in RGBA mode.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/index_func.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.index_func import *
from OpenGL.raw.GL.EXT.index_func import _EXTENSION_NAME

def glInitIndexFuncEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION