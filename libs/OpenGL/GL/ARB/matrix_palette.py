'''OpenGL extension ARB.matrix_palette

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.matrix_palette to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends the abilities of ARB_vertex_blend to include 
	a palette of modelview matrices.  The n vertex units use a palette
	of m modelview matrices.  (Where n and m are constrained to
	implementation defined maxima.)  Each vertex has a set of n
	indices into the palette, and a corresponding set of n weights.
	Matrix indices can be changed for each vertex (between Begin and
	End).  
	
	When this extension is utilized, the enabled units transform each
	vertex by the modelview matrices specified by the vertices'
	respective indices.  These results are subsequently scaled by the
	weights of the respective units and then summed to create the
	eyespace vertex.   
	
	A similar procedure is followed for normals.  Normals, however,
	are transformed by the inverse transpose of the modelview matrix.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/matrix_palette.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.matrix_palette import *
from OpenGL.raw.GL.ARB.matrix_palette import _EXTENSION_NAME

def glInitMatrixPaletteARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glMatrixIndexubvARB.indices size not checked against size
glMatrixIndexubvARB=wrapper.wrapper(glMatrixIndexubvARB).setInputArraySize(
    'indices', None
)
# INPUT glMatrixIndexusvARB.indices size not checked against size
glMatrixIndexusvARB=wrapper.wrapper(glMatrixIndexusvARB).setInputArraySize(
    'indices', None
)
# INPUT glMatrixIndexuivARB.indices size not checked against size
glMatrixIndexuivARB=wrapper.wrapper(glMatrixIndexuivARB).setInputArraySize(
    'indices', None
)
# INPUT glMatrixIndexPointerARB.pointer size not checked against 'size,type,stride'
glMatrixIndexPointerARB=wrapper.wrapper(glMatrixIndexPointerARB).setInputArraySize(
    'pointer', None
)
### END AUTOGENERATED SECTION