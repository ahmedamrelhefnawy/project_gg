'''OpenGL extension EXT.raster_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.raster_multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows rendering to a non-multisample color buffer while
	rasterizing with more than one sample. The result of rasterization
	(coverage) is available in the gl_SampleMaskIn[] fragment shader input,
	multisample rasterization is enabled for all primitives, and several per-
	fragment operations operate at the raster sample rate.
	
	When using the functionality provided by this extension, depth, stencil,
	and depth bounds tests must be disabled, and a multisample draw
	framebuffer must not be used.
	
	A fragment's "coverage", or "effective raster samples" is considered to
	have "N bits" (as opposed to "one bit" corresponding to the single color
	sample) through the fragment shader, in the sample mask output, through
	the multisample fragment operations and occlusion query, until the coverage
	is finally "reduced" to a single bit in a new "Coverage Reduction" stage
	that occurs before blending.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/raster_multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.raster_multisample import *
from OpenGL.raw.GL.EXT.raster_multisample import _EXTENSION_NAME

def glInitRasterMultisampleEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION