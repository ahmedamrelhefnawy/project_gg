'''OpenGL extension EXT.multiview_timer_query

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.multiview_timer_query to provide a more 
Python-friendly API

Overview (from the spec)
	
	OVR_multiview introduced multiview rendering to OpenGL and OpenGL ES.
	This extension removes one of the limitations of the OVR_multiview 
	extension by allowing the use of timer queries during multiview rendering. 
	OVR_multiview does not specify defined behavior for such usage
	(if implemented in OpenGL or if EXT_disjoint_timer_query is present).
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/multiview_timer_query.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.multiview_timer_query import *
from OpenGL.raw.GL.EXT.multiview_timer_query import _EXTENSION_NAME

def glInitMultiviewTimerQueryEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION