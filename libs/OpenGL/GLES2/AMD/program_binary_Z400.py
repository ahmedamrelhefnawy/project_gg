'''OpenGL extension AMD.program_binary_Z400

This module customises the behaviour of the 
OpenGL.raw.GLES2.AMD.program_binary_Z400 to provide a more 
Python-friendly API

Overview (from the spec)
	
	AMD provides an offline shader compiler as part of its suite of SDK tools
	for AMD's Z400 family of embedded graphics accelerator IP.  This extension
	makes available a program binary format, Z400_BINARY_AMD.
	
	The offline shader compiler accepts a pair of OpenGL Shading Language 
	(GLSL) source shaders: one vertex shader and one fragment shader.  It
	outputs a compiled, optimized, and pre-linked program binary which can then
	be loaded into a program objects via the ProgramBinaryOES command.
	
	Applications are recommended to use the OES_get_program_binary extension's
	program binary retrieval mechanism for install-time shader compilation where
	applicable.  That cross-vendor extension provides the performance benefits
	of loading pre-compiled program binaries, while providing the portability of
	deploying GLSL source shaders with the application rather than vendor-
	specific binaries.  The details of this extension are obviated by the use
	of that extension.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/program_binary_Z400.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.AMD.program_binary_Z400 import *
from OpenGL.raw.GLES2.AMD.program_binary_Z400 import _EXTENSION_NAME

def glInitProgramBinaryZ400AMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION