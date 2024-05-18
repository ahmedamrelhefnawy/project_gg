'''OpenGL extension EXT.multiview_draw_buffers

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.multiview_draw_buffers to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows selecting among draw buffers as the
	rendering target. This may be among multiple primary buffers
	pertaining to platform-specific stereoscopic or multiview displays
	or among offscreen framebuffer object color attachments.
	
	To remove any artificial limitations imposed on the number of
	possible buffers, draw buffers are identified not as individual
	enums, but as pairs of values consisting of an enum representing
	buffer locations such as COLOR_ATTACHMENT_EXT or MULTIVIEW_EXT,
	and an integer representing an identifying index of buffers of this
	location. These (location, index) pairs are used to specify draw
	buffer targets using a new DrawBuffersIndexedEXT call.
	
	Rendering to buffers of location MULTIVIEW_EXT associated with the
	context allows rendering to multiview buffers created by EGL using
	EGL_EXT_multiview_window for stereoscopic displays.
	
	Rendering to COLOR_ATTACHMENT_EXT buffers allows implementations to
	increase the number of potential color attachments indefinitely to
	renderbuffers and textures.
	
	This extension allows the traditional quad buffer stereoscopic
	rendering method that has proven effective by indicating a left or
	right draw buffer and rendering to each accordingly, but is also
	dynamic enough to handle an arbitrary number of color buffer targets
	all using the same shader. This grants the user maximum flexibility
	as well as a familiar interface.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/multiview_draw_buffers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.multiview_draw_buffers import *
from OpenGL.raw.GLES2.EXT.multiview_draw_buffers import _EXTENSION_NAME

def glInitMultiviewDrawBuffersEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDrawBuffersIndexedEXT.indices size not checked against n
# INPUT glDrawBuffersIndexedEXT.location size not checked against n
glDrawBuffersIndexedEXT=wrapper.wrapper(glDrawBuffersIndexedEXT).setInputArraySize(
    'indices', None
).setInputArraySize(
    'location', None
)
### END AUTOGENERATED SECTION