'''OpenGL extension ARB.spirv_extensions

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.spirv_extensions to provide a more 
Python-friendly API

Overview (from the spec)
	
	ARB_gl_spirv added support for using SPIR-V modules in OpenGL.
	However it only added support for SPIR-V 1.0 concepts that were part of
	the OpenGL 4.5 Core Profile.
	
	There are a great number of additional OpenGL ARB and vendor extensions
	which add shading language concepts and since they were defined prior
	to the existence of SPIR-V support in OpenGL they don't add SPIR-V support
	for their additional features.  Ideally GL_ARB_gl_spirv would have added
	support for them, but as noted in Issue 27 of that extension, support for
	them was left as a future exercise.
	
	Now that at least some of that functionality has been defined via SPIR-V
	extensions, there is currently no way for an OpenGL implementation to
	advertise that is supports additional SPIR-V extensions.
	
	This extension provides a mechanism for an implementation to advertise
	which SPIR-V extensions it supports, and further provides a place where
	the SPIR-V environment for those extensions can be documented for OpenGL.
	
	It is expected that this document can be extended over time as SPIR-V
	support for additional extensions is added. The mapping between GLSL and
	SPIR-V concepts and any other pertinent information can be provided here
	as interactions with the corresponding OpenGL and SPIR-V extensions.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/spirv_extensions.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.spirv_extensions import *
from OpenGL.raw.GL.ARB.spirv_extensions import _EXTENSION_NAME

def glInitSpirvExtensionsARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION