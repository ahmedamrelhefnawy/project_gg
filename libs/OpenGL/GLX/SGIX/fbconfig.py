'''OpenGL extension SGIX.fbconfig

This module customises the behaviour of the 
OpenGL.raw.GLX.SGIX.fbconfig to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/fbconfig.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.SGIX.fbconfig import *
from OpenGL.raw.GLX.SGIX.fbconfig import _EXTENSION_NAME

def glInitFbconfigSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION