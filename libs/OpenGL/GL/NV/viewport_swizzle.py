'''OpenGL extension NV.viewport_swizzle

This module customises the behaviour of the 
OpenGL.raw.GL.NV.viewport_swizzle to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a new per-viewport swizzle that can modify the
	position of primitives sent to each viewport.  New viewport swizzle state
	is added for each viewport, and a new position vector is computed for each
	vertex by selecting from and optionally negating any of the four
	components of the original position vector.
	
	This new viewport swizzle is useful for a number of algorithms, including
	single-pass cubemap rendering (broadcasting a primitive to multiple faces
	and reorienting the vertex position for each face) and voxel
	rasterization.  The per-viewport component remapping and negation provided
	by the swizzle allows application code to re-orient three-dimensional
	geometry with a view along any of the X, Y, or Z axes.  If a perspective
	projection and depth buffering is required, 1/W buffering should be used,
	as described in the single-pass cubemap rendering example in the "Issues"
	section below.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/viewport_swizzle.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.viewport_swizzle import *
from OpenGL.raw.GL.NV.viewport_swizzle import _EXTENSION_NAME

def glInitViewportSwizzleNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION