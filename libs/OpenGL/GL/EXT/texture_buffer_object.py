'''OpenGL extension EXT.texture_buffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_buffer_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a new texture type, called a buffer texture.
	Buffer textures are one-dimensional arrays of texels whose storage comes
	from an attached buffer object.  When a buffer object is bound to a buffer
	texture, a format is specified, and the data in the buffer object is
	treated as an array of texels of the specified format.
	
	The use of a buffer object to provide storage allows the texture data to
	be specified in a number of different ways:  via buffer object loads
	(BufferData), direct CPU writes (MapBuffer), framebuffer readbacks
	(EXT_pixel_buffer_object extension).  A buffer object can also be loaded
	by transform feedback (NV_transform_feedback extension), which captures
	selected transformed attributes of vertices processed by the GL.  Several
	of these mechanisms do not require an extra data copy, which would be
	required when using conventional TexImage-like entry points.
	
	Buffer textures do not support mipmapping, texture lookups with normalized
	floating-point texture coordinates, and texture filtering of any sort, and
	may not be used in fixed-function fragment processing.  They can be
	accessed via single texel fetch operations in programmable shaders.  For
	assembly shaders (NV_gpu_program4), the TXF instruction is used.  For GLSL
	(EXT_gpu_shader4), a new sampler type and texel fetch function are used.
	
	Buffer textures can be substantially larger than equivalent
	one-dimensional textures; the maximum texture size supported for buffer
	textures in the initial implementation of this extension is 2^27 texels,
	versus 2^13 (8192) texels for otherwise equivalent one-dimensional
	textures.  (Note that this extension only guarantees support for buffer
	textures with 2^16 texels, but we expect most implementations to exceed
	that substantially.)  When a buffer object is attached to a buffer
	texture, a size is not specified; rather, the number of texels in the
	texture is taken by dividing the size of the buffer object by the size of
	each texel.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_buffer_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.texture_buffer_object import *
from OpenGL.raw.GL.EXT.texture_buffer_object import _EXTENSION_NAME

def glInitTextureBufferObjectEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION