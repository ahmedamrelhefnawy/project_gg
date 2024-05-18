'''OpenGL extension NV.shader_texture_footprint

This module customises the behaviour of the 
OpenGL.raw.GL.NV.shader_texture_footprint to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds OpenGL API support for the OpenGL Shading Language
	(GLSL) extension "NV_shader_texture_footprint".  That extension adds a new
	set of texture query functions ("textureFootprint*NV") to GLSL.  These
	built-in functions prepare to perform a filtered texture lookup based on
	coordinates and other parameters passed in by the calling code.  However,
	instead of returning data from the provided texture image, these query
	functions instead return data identifying the _texture footprint_ for an
	equivalent texture access.  The texture footprint identifies a set of
	texels that may be accessed in order to return a filtered result for the
	texture access.
	
	The footprint itself is a structure that includes integer values that
	identify a small neighborhood of texels in the texture being accessed and
	a bitfield that indicates which texels in that neighborhood would be used.
	Each bit in the returned bitfield identifies whether any texel in a small
	aligned block of texels would be fetched by the texture lookup.  The size
	of each block is specified by an access _granularity_ provided by the
	shader.  The minimum granularity supported by this extension is 2x2 (for
	2D textures) and 2x2x2 (for 3D textures); the maximum granularity is
	256x256 (for 2D textures) or 64x32x32 (for 3D textures).  Each footprint
	query returns the footprint from a single texture level.  When using
	minification filters that combine accesses from multiple mipmap levels,
	shaders must perform separate queries for the two levels accessed ("fine"
	and "coarse").  The footprint query also returns a flag indicating if the
	texture lookup would access texels from only one mipmap level or from two
	neighboring levels.
	
	This extension should be useful for multi-pass rendering operations that
	do an initial expensive rendering pass to produce a first image that is
	then used as a texture for a second pass.  If the second pass ends up
	accessing only portions of the first image (e.g., due to visibility), the
	work spent rendering the non-accessed portion of the first image was
	wasted.  With this feature, an application can limit this waste using an
	initial pass over the geometry in the second image that performs a
	footprint query for each visible pixel to determine the set of pixels that
	it needs from the first image.  This pass would accumulate an aggregate
	footprint of all visible pixels into a separate "footprint texture" using
	shader atomics.  Then, when rendering the first image, the application can
	kill all shading work for pixels not in this aggregate footprint.
	
	The implementation of this extension has a number of limitations.  The
	texture footprint query functions are only supported for two- and
	three-dimensional textures (TEXTURE_2D, TEXTURE_3D).  Texture footprint
	evaluation only supports the CLAMP_TO_EDGE wrap mode; results are
	undefined for all other wrap modes.  The implementation supports only a
	limited set of granularity values and does not support separate coverage
	information for each texel in the original texture.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/shader_texture_footprint.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.shader_texture_footprint import *
from OpenGL.raw.GL.NV.shader_texture_footprint import _EXTENSION_NAME

def glInitShaderTextureFootprintNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION