'''OpenGL extension VERSION.EGL_1_4

This module customises the behaviour of the 
OpenGL.raw.EGL.VERSION.EGL_1_4 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/EGL_1_4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.VERSION.EGL_1_4 import *
from OpenGL.raw.EGL.VERSION.EGL_1_4 import _EXTENSION_NAME

def glInitEgl14VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION