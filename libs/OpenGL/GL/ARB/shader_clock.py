'''OpenGL extension ARB.shader_clock

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_clock to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension exposes a 64-bit monotonically incrementing shader
	counter which may be used to derive local timing information within
	a single shader invocation.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_clock.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.shader_clock import *
from OpenGL.raw.GL.ARB.shader_clock import _EXTENSION_NAME

def glInitShaderClockARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION