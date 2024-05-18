'''OpenGL extension EXT.sparse_texture

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.sparse_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	Recent advances in application complexity and a desire for higher
	resolutions have pushed texture sizes up considerably. Often, the amount
	of physical memory available to a graphics processor is a limiting factor
	in the performance of texture-heavy applications. Once the available
	physical memory is exhausted, paging may occur bringing performance down
	considerably - or worse, the application may fail. Nevertheless, the amount
	of address space available to the graphics processor has increased to the
	point where many gigabytes - or even terabytes of address space may be
	usable even though that amount of physical memory is not present.
	
	This extension allows the separation of the graphics processor's address
	space (reservation) from the requirement that all textures must be
	physically backed (commitment). This exposes a limited form of
	virtualization for textures. Use cases include sparse (or partially
	resident) textures, texture paging, on-demand and delayed loading of
	texture assets and application controlled level of detail.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/sparse_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.sparse_texture import *
from OpenGL.raw.GLES2.EXT.sparse_texture import _EXTENSION_NAME

def glInitSparseTextureEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION