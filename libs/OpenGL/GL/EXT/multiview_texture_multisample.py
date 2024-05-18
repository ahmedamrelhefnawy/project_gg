'''OpenGL extension EXT.multiview_texture_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.multiview_texture_multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	OVR_multiview introduced multiview rendering to OpenGL and OpenGL ES.
	
	This extension removes one of the limitations of the OVR_multiview 
	extension by allowing the use of multisample textures during multiview rendering.
	
	This is one of two extensions that allow multisampling when using 
	OVR_multiview. Each supports one of the two different approaches to 
	multisampling in OpenGL and OpenGL ES:
	
	    Core OpenGL and OpenGL ES 3.1+ have explicit support for multisample 
	    texture types, such as TEXTURE_2D_MULTISAMPLE. Applications can access 
	    the values of individual samples and can explicitly "resolve" the 
	    samples of each pixel down to a single color.
	
	    The extension EXT_multisampled_render_to_texture provides support for 
	    multisampled rendering to non-multisample texture types, such as 
	    TEXTURE_2D. The individual samples for each pixel are maintained 
	    internally by the implementation and can not be accessed directly 
	    by applications. These samples are eventually resolved implicitly to 
	    a single color for each pixel.
	
	This extension supports the first multisampling style with multiview 
	rendering; the OVR_multiview_multisampled_render_to_texture extension 
	supports the second style. Note that support for one of these multiview 
	extensions does not imply support for the other.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/multiview_texture_multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.multiview_texture_multisample import *
from OpenGL.raw.GL.EXT.multiview_texture_multisample import _EXTENSION_NAME

def glInitMultiviewTextureMultisampleEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION