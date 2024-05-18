'''OpenGL extension AMD.shader_gpu_shader_half_float_fetch

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.shader_gpu_shader_half_float_fetch to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/shader_gpu_shader_half_float_fetch.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.shader_gpu_shader_half_float_fetch import *
from OpenGL.raw.GL.AMD.shader_gpu_shader_half_float_fetch import _EXTENSION_NAME

def glInitShaderGpuShaderHalfFloatFetchAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION