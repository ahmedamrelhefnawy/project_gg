'''OpenGL extension OES.single_precision

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.single_precision to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds commands with single-precision floating-point
	parameters corresponding to the commands that only variants that
	accept double-precision floating-point input.  This allows an
	application to avoid using double-precision floating-point
	data types.  New commands are added with an 'f' prefix.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/single_precision.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.single_precision import *
from OpenGL.raw.GLES1.OES.single_precision import _EXTENSION_NAME

def glInitSinglePrecisionOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glClipPlanefOES=wrapper.wrapper(glClipPlanefOES).setInputArraySize(
    'equation', 4
)
glGetClipPlanefOES=wrapper.wrapper(glGetClipPlanefOES).setOutput(
    'equation',size=(4,),orPassIn=True
)
### END AUTOGENERATED SECTION