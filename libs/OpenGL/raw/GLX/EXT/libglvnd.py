'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_EXT_libglvnd'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_EXT_libglvnd',error_checker=_errors._error_checker)
GLX_VENDOR_NAMES_EXT=_C('GLX_VENDOR_NAMES_EXT',0x20F6)

