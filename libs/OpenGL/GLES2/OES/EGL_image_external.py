'''OpenGL extension OES.EGL_image_external

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.EGL_image_external to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism for creating EGLImage texture targets
	from EGLImages.  This extension defines a new texture target,
	TEXTURE_EXTERNAL_OES.  This texture target can only be specified using an
	EGLImage.  There is no support for most of the functions that manipulate
	other texture targets (e.g. you cannot use gl*Tex*Image*() functions with
	TEXTURE_EXTERNAL_OES).  Also, TEXTURE_EXTERNAL_OES targets never have more
	than a single LOD level.  Because of these restrictions, it is possible to
	bind EGLImages which have internal formats not otherwise supported by
	OpenGL ES.  For example some implementations may allow EGLImages with
	planar or interleaved YUV data to be GLES texture target siblings.  It is
	up to the implementation exactly what formats are accepted.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/EGL_image_external.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.EGL_image_external import *
from OpenGL.raw.GLES2.OES.EGL_image_external import _EXTENSION_NAME

def glInitEglImageExternalOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION