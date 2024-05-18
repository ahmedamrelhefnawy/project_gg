'''OpenGL extension NV.scissor_exclusive

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.scissor_exclusive to provide a more 
Python-friendly API

Overview (from the spec)
	
	In unextended OpenGL, applications can enable a per-viewport scissor test
	(SCISSOR_TEST) where fragments are discarded if their (x,y) coordinates
	lie outside the corresponding scissor rectangle.  In this extension, we
	provide a separate per-viewport exclusive scissor test, where fragments
	are discarded if their (x,y) coordinates lie *inside* the corresponding
	exclusive scissor rectangle.
	
	The regular (inclusive) scissor test and exclusive scissor test are
	orthogonal; applications can enable either or both tests for each
	viewport. If both tests are enabled, fragments will be discarded unless
	their (x,y) coordinates are both inside the regular scissor rectangle and
	outside the exclusive scissor rectangle.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/scissor_exclusive.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.scissor_exclusive import *
from OpenGL.raw.GLES2.NV.scissor_exclusive import _EXTENSION_NAME

def glInitScissorExclusiveNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glScissorExclusiveArrayvNV.v size not checked against 'count'
glScissorExclusiveArrayvNV=wrapper.wrapper(glScissorExclusiveArrayvNV).setInputArraySize(
    'v', None
)
### END AUTOGENERATED SECTION