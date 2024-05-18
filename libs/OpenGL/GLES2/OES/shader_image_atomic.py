'''OpenGL extension OES.shader_image_atomic

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.shader_image_atomic to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides built-in functions allowing shaders to perform
	atomic read-modify-write operations to a single level of a texture
	object from any shader stage. These built-in functions are named
	imageAtomic*(), and accept integer texel coordinates to identify the
	texel accessed. These built-in functions extend the Images in ESSL 3.10.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/shader_image_atomic.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.shader_image_atomic import *
from OpenGL.raw.GLES2.OES.shader_image_atomic import _EXTENSION_NAME

def glInitShaderImageAtomicOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION