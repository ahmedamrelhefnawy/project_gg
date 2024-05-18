'''OpenGL extension SGIX.calligraphic_fragment

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.calligraphic_fragment to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a minimal mechanism to control the copying of
	fragment information to external hardware such as a calligraphic
	display interface.  The initial implementation is intended to support
	the calligraphic interface on InfiniteReality.  On InfiniteReality
	when the interface is enabled, fragment information consisting of
	some color and coverage data is sent to the interface.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/calligraphic_fragment.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.calligraphic_fragment import *
from OpenGL.raw.GL.SGIX.calligraphic_fragment import _EXTENSION_NAME

def glInitCalligraphicFragmentSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION