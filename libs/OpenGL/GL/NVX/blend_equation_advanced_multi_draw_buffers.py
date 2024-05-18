'''OpenGL extension NVX.blend_equation_advanced_multi_draw_buffers

This module customises the behaviour of the 
OpenGL.raw.GL.NVX.blend_equation_advanced_multi_draw_buffers to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds support for using advanced blend equations
	introduced with NV_blend_equation_advanced (and standardized
	by KHR_blend_equation_advanced) in conjunction with multiple
	draw buffers.  The NV_blend_equation_advanced extension supports
	advanced blending equations only when rending to a single color
	buffer using fragment color zero and throws and INVALID_OPERATION
	error when multiple draw buffers are used. This extension removes
	this restriction.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NVX/blend_equation_advanced_multi_draw_buffers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NVX.blend_equation_advanced_multi_draw_buffers import *
from OpenGL.raw.GL.NVX.blend_equation_advanced_multi_draw_buffers import _EXTENSION_NAME

def glInitBlendEquationAdvancedMultiDrawBuffersNVX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION