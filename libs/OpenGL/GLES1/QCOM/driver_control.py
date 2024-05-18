'''OpenGL extension QCOM.driver_control

This module customises the behaviour of the 
OpenGL.raw.GLES1.QCOM.driver_control to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension exposes special control features in a driver to a
	developer. A use of these controls would be to override state or
	implement special modes of operation. One common example might be an
	IFH or infinitely fast hardware mode. In this mode none of draw
	commands would be sent to the GPU so no image would be displayed,
	but all the driver software overhead would still happen thus
	enabling developers to analyze driver overhead separate from GPU
	performance. Some uses of this extension could invalidate future
	rendering and thus should only be used by developers for debugging
	and performance profiling purposes.
	
	The extension is general enough to allow the implementation to
	choose which controls to expose and to provide a textual description
	of those controls to developers.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/QCOM/driver_control.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.QCOM.driver_control import *
from OpenGL.raw.GLES1.QCOM.driver_control import _EXTENSION_NAME

def glInitDriverControlQCOM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glGetDriverControlsQCOM.driverControls size not checked against size
glGetDriverControlsQCOM=wrapper.wrapper(glGetDriverControlsQCOM).setInputArraySize(
    'driverControls', None
)
# INPUT glGetDriverControlStringQCOM.driverControlString size not checked against bufSize
glGetDriverControlStringQCOM=wrapper.wrapper(glGetDriverControlStringQCOM).setInputArraySize(
    'driverControlString', None
)
### END AUTOGENERATED SECTION