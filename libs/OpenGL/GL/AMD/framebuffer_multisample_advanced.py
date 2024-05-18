'''OpenGL extension AMD.framebuffer_multisample_advanced

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.framebuffer_multisample_advanced to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends ARB_framebuffer_object by allowing compromises
	between image quality and memory footprint of multisample
	antialiasing.
	
	ARB_framebuffer_object introduced RenderbufferStorageMultisample
	as a method of defining the parameters for a multisample render
	buffer. This function takes a <samples> parameter that has strict
	requirements on behavior such that no compromises in the final image
	quality are allowed. Additionally, ARB_framebuffer_object requires
	that all framebuffer attachments have the same number of samples.
	
	This extension extends ARB_framebuffer_object by providing a new
	function, RenderbufferStorageMultisampleAdvancedAMD, that
	distinguishes between samples and storage samples for color
	renderbuffers where the number of storage samples can be less than
	the number of samples. This extension also allows non-matching sample
	counts between color and depth/stencil renderbuffers.
	
	This extension does not require any specific combination of sample
	counts to be supported.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/framebuffer_multisample_advanced.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.framebuffer_multisample_advanced import *
from OpenGL.raw.GL.AMD.framebuffer_multisample_advanced import _EXTENSION_NAME

def glInitFramebufferMultisampleAdvancedAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION