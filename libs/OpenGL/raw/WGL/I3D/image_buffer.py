'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_I3D_image_buffer'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.WGL,'WGL_I3D_image_buffer',error_checker=_errors._error_checker)
WGL_IMAGE_BUFFER_LOCK_I3D=_C('WGL_IMAGE_BUFFER_LOCK_I3D',0x00000002)
WGL_IMAGE_BUFFER_MIN_ACCESS_I3D=_C('WGL_IMAGE_BUFFER_MIN_ACCESS_I3D',0x00000001)
@_f
@_p.types(_cs.BOOL,_cs.HDC,ctypes.POINTER(_cs.HANDLE),ctypes.POINTER(_cs.LPVOID),ctypes.POINTER(_cs.DWORD),_cs.UINT)
def wglAssociateImageBufferEventsI3D(hDC,pEvent,pAddress,pSize,count):pass
@_f
@_p.types(_cs.LPVOID,_cs.HDC,_cs.DWORD,_cs.UINT)
def wglCreateImageBufferI3D(hDC,dwSize,uFlags):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.LPVOID)
def wglDestroyImageBufferI3D(hDC,pAddress):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,ctypes.POINTER(_cs.LPVOID),_cs.UINT)
def wglReleaseImageBufferEventsI3D(hDC,pAddress,count):pass
