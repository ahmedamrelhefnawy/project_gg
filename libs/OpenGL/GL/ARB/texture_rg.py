'''OpenGL extension ARB.texture_rg

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_rg to provide a more 
Python-friendly API

Overview (from the spec)
	
	Historically one- and two- component textures have been specified in OpenGL
	using the intensity, luminance or luminance-alpha (I/L/LA) formats.
	With the advent of programmable shaders and render-to-texture capabilites
	these legacy formats carry some historical artifacts which are no longer
	useful.
	
	For example, when sampling from such textures, the luminance values
	are replicated across the color components, and the intensity values are
	replicated across both the color and alpha components. This is no
	longer necessary with programmable shaders.
	
	It is also desirable to be able to render to one- and two-
	component format textures using capabilities such as framebuffer
	objects (FBO), but rendering to I/L/LA formats is under-specified
	(specifically how to map R/G/B/A values to I/L/A texture channels).
	
	This extension adds new base internal formats for the one-component RED
	and two-component RG (red green) texture formats as well as sized
	internal formats for fixed-point, floating-point and pure integer texture
	formats. The new texure formats can be used for texturing as well
	as for rendering into with framebuffer objects.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_rg.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.texture_rg import *
from OpenGL.raw.GL.ARB.texture_rg import _EXTENSION_NAME

def glInitTextureRgARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
from OpenGL import images as _images
_images.COMPONENT_COUNTS.update( {
GL_R16:1,
GL_R16F:1,
GL_R16I:1,
GL_R16UI:1,
GL_R32F:1,
GL_R32I:1,
GL_R32UI:1,
GL_R8:1,
GL_R8I:1,
GL_R8UI:1,

GL_RG:2,
GL_RG16:2,
GL_RG16F:2,
GL_RG16I:2,
GL_RG16UI:2,
GL_RG32F:2,
GL_RG32I:2,
GL_RG32UI:2,
GL_RG8:2,
GL_RG8I:2,
GL_RG8UI:2,
GL_RG_INTEGER:2,
})

