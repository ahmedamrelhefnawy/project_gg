'''OpenGL extension AMD.compressed_ATC_texture

This module customises the behaviour of the 
OpenGL.raw.GLES2.AMD.compressed_ATC_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables support for ATC compressed texture formats.  ATC is 
	AMD's proprietary compression algorithm for compressing textures for 
	handheld devices to save on power consumption, memory footprint and 
	bandwidth.
	
	Three compression formats are introduced:
	
	- A compression format for RGB textures.
	- A compression format for RGBA textures using explicit alpha encoding.
	- A compression format for RGBA textures using interpolated alpha encoding.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/compressed_ATC_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.AMD.compressed_ATC_texture import *
from OpenGL.raw.GLES2.AMD.compressed_ATC_texture import _EXTENSION_NAME

def glInitCompressedAtcTextureAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION