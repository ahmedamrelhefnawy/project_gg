'''OpenGL extension NV.evaluators

This module customises the behaviour of the 
OpenGL.raw.GL.NV.evaluators to provide a more 
Python-friendly API

Overview (from the spec)
	
	OpenGL evaluators provide applications with the capability to
	specify polynomial or rational curves and surfaces using control
	points relative to the Bezier basis.  The curves and surfaces are
	then drawn by evaluating the polynomials provided at various values
	for the u parameter of a curve or the (u,v) parameters of a surface.
	A tensor product formulation is used for the surfaces.
	
	For various historical reasons, evaluators have not been
	particularly popular as an interface for drawing curves and surfaces.
	This extension proposes a new interface for surfaces that provides a
	number of significant enhancements to the functionality provided by
	the original OpenGL evaluators.
	
	Many implementations never optimized evaluators, so applications
	often implemented their own algorithms instead.  This extension
	relaxes some restrictions that make it difficult to optimize
	evaluators.
	
	Also, new vertex attributes have been added to OpenGL through
	extensions, including multiple sets of texture coordinates, a
	secondary color, a fog coordinate, a vertex weight, and others.
	The extensions which added these vertex attributes never bothered
	to update the functionality of evaluators, since they were used so
	little in the first place.  In turn, evaluators have become more and
	more out of date, making it even less likely that developers will
	want to use them.  Most of the attributes are not a big loss, but
	support for multiple sets of texture coordinates would be absolutely
	essential to developers considering the use of evaluators.
	
	OpenGL evaluators only support rectangular patches, not triangular
	patches.  Although triangular patches can be converted into
	rectangular patches, direct support for triangular patches is likely
	to be more efficient.
	
	The tessellation algorithm used is too inflexible for most purposes;
	only the number of rows and columns can be specified.  Adjacent
	patches must then have identical numbers of rows and columns, or
	severe cracking will occur.  Ideally, a number of subdivisions could
	be specified for all four sides of a rectangular patch and for all
	three of a triangular patch.  This extension goes one step further
	and allows those numbers to be specified in floating-point, providing
	a mechanism for smoothly changing the level of detail of the surface.
	
	Meshes evaluated with EvalMesh are required to match up exactly
	with equivalent meshes evaluated with EvalCoord or EvalPoint.
	This makes it difficult or impossible to use optimizations such as
	forward differencing.
	
	Finally, little attention is given to some of the difficult problems
	that can arise when multiple patches are drawn.  Depending on the
	way evaluators are implemented, and depending on the orientation of
	edges, numerical accuracy problems can cause cracks to appear between
	patches with the same boundary control points.  This extension makes
	guarantees that an edge shared between two patches will match up
	exactly under certain conditions.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/evaluators.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.evaluators import *
from OpenGL.raw.GL.NV.evaluators import _EXTENSION_NAME

def glInitEvaluatorsNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glMapControlPointsNV.points size not checked against 'target,uorder,vorder'
glMapControlPointsNV=wrapper.wrapper(glMapControlPointsNV).setInputArraySize(
    'points', None
)
# INPUT glMapParameterivNV.params size not checked against 'target,pname'
glMapParameterivNV=wrapper.wrapper(glMapParameterivNV).setInputArraySize(
    'params', None
)
# INPUT glMapParameterfvNV.params size not checked against 'target,pname'
glMapParameterfvNV=wrapper.wrapper(glMapParameterfvNV).setInputArraySize(
    'params', None
)
glGetMapControlPointsNV=wrapper.wrapper(glGetMapControlPointsNV).setOutput(
    'points',size=_glgets._glget_size_mapping,pnameArg='target',orPassIn=True
)
# OUTPUT glGetMapParameterivNV.params COMPSIZE(target, pname) 
# OUTPUT glGetMapParameterfvNV.params COMPSIZE(target, pname) 
glGetMapAttribParameterivNV=wrapper.wrapper(glGetMapAttribParameterivNV).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetMapAttribParameterfvNV=wrapper.wrapper(glGetMapAttribParameterfvNV).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
### END AUTOGENERATED SECTION