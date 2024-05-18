'''OpenGL extension NV.framebuffer_multisample_coverage

This module customises the behaviour of the 
OpenGL.raw.GL.NV.framebuffer_multisample_coverage to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends the EXT_framebuffer_multisample 
	specification by providing a new function,
	RenderBufferStorageMultisampleCoverageNV, that distinguishes 
	between color samples and coverage samples.
	
	EXT_framebuffer_multisample introduced the function 
	RenderbufferStorageMultisampleEXT as a method of defining the 
	storage parameters for a multisample render buffer.  This function 
	takes a <samples> parameter.  Using rules provided by the 
	specification, the <samples> parameter is resolved to an actual 
	number of samples that is supported by the underlying hardware.  
	EXT_framebuffer_multisample does not specify whether <samples>
	refers to coverage samples or color samples.
	
	This extension adds the function 
	RenderbufferStorageMultisamplCoverageNV, which takes a 
	<coverageSamples> parameter as well as a <colorSamples> parameter.  
	These two parameters give developers more fine grained control over
	the quality of multisampled images.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/framebuffer_multisample_coverage.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.framebuffer_multisample_coverage import *
from OpenGL.raw.GL.NV.framebuffer_multisample_coverage import _EXTENSION_NAME

def glInitFramebufferMultisampleCoverageNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION