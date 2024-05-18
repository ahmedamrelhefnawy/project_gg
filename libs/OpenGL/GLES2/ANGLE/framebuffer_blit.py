'''OpenGL extension ANGLE.framebuffer_blit

This module customises the behaviour of the 
OpenGL.raw.GLES2.ANGLE.framebuffer_blit to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension modifies framebuffer objects by splitting the
	framebuffer object binding point into separate DRAW and READ
	bindings.  This allows copying directly from one framebuffer to
	another.  In addition, a new high performance blit function is
	added to facilitate these blits and perform some data conversion
	where allowed.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANGLE/framebuffer_blit.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.ANGLE.framebuffer_blit import *
from OpenGL.raw.GLES2.ANGLE.framebuffer_blit import _EXTENSION_NAME

def glInitFramebufferBlitANGLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION