'''OpenGL extension SGI.make_current_read

This module customises the behaviour of the 
OpenGL.raw.GLX.SGI.make_current_read to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGI/make_current_read.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.SGI.make_current_read import *
from OpenGL.raw.GLX.SGI.make_current_read import _EXTENSION_NAME

def glInitMakeCurrentReadSGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION