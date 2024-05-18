'''OpenGL extension ARB.ES3_2_compatibility

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.ES3_2_compatibility to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds support for features of OpenGL ES 3.2 that are
	missing from OpenGL 4.5. Enabling these features will ease the process
	of porting applications from OpenGL ES 3.2 to OpenGL.
	
	In particular this adds the following features:
	
	- Bounding box used to optimization tessellation processing
	  (OES_primitive_bounding_box)
	- query for MULTISAMPLE_LINE_WIDTH_RANGE_ARB
	- support for the OpenGL ES 3.20 shading language
	
	For full OpenGL ES 3.2 compatibility the implementation must support
	KHR_blend_equation_advanced and KHR_texture_compression_astc_ldr. Those
	features are not defined in this extension spec since they are already
	defined at the KHR level.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/ES3_2_compatibility.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.ES3_2_compatibility import *
from OpenGL.raw.GL.ARB.ES3_2_compatibility import _EXTENSION_NAME

def glInitEs32CompatibilityARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION