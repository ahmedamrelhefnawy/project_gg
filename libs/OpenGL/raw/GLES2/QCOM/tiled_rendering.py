'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_QCOM_tiled_rendering'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_QCOM_tiled_rendering',error_checker=_errors._error_checker)
GL_COLOR_BUFFER_BIT0_QCOM=_C('GL_COLOR_BUFFER_BIT0_QCOM',0x00000001)
GL_COLOR_BUFFER_BIT1_QCOM=_C('GL_COLOR_BUFFER_BIT1_QCOM',0x00000002)
GL_COLOR_BUFFER_BIT2_QCOM=_C('GL_COLOR_BUFFER_BIT2_QCOM',0x00000004)
GL_COLOR_BUFFER_BIT3_QCOM=_C('GL_COLOR_BUFFER_BIT3_QCOM',0x00000008)
GL_COLOR_BUFFER_BIT4_QCOM=_C('GL_COLOR_BUFFER_BIT4_QCOM',0x00000010)
GL_COLOR_BUFFER_BIT5_QCOM=_C('GL_COLOR_BUFFER_BIT5_QCOM',0x00000020)
GL_COLOR_BUFFER_BIT6_QCOM=_C('GL_COLOR_BUFFER_BIT6_QCOM',0x00000040)
GL_COLOR_BUFFER_BIT7_QCOM=_C('GL_COLOR_BUFFER_BIT7_QCOM',0x00000080)
GL_DEPTH_BUFFER_BIT0_QCOM=_C('GL_DEPTH_BUFFER_BIT0_QCOM',0x00000100)
GL_DEPTH_BUFFER_BIT1_QCOM=_C('GL_DEPTH_BUFFER_BIT1_QCOM',0x00000200)
GL_DEPTH_BUFFER_BIT2_QCOM=_C('GL_DEPTH_BUFFER_BIT2_QCOM',0x00000400)
GL_DEPTH_BUFFER_BIT3_QCOM=_C('GL_DEPTH_BUFFER_BIT3_QCOM',0x00000800)
GL_DEPTH_BUFFER_BIT4_QCOM=_C('GL_DEPTH_BUFFER_BIT4_QCOM',0x00001000)
GL_DEPTH_BUFFER_BIT5_QCOM=_C('GL_DEPTH_BUFFER_BIT5_QCOM',0x00002000)
GL_DEPTH_BUFFER_BIT6_QCOM=_C('GL_DEPTH_BUFFER_BIT6_QCOM',0x00004000)
GL_DEPTH_BUFFER_BIT7_QCOM=_C('GL_DEPTH_BUFFER_BIT7_QCOM',0x00008000)
GL_MULTISAMPLE_BUFFER_BIT0_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT0_QCOM',0x01000000)
GL_MULTISAMPLE_BUFFER_BIT1_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT1_QCOM',0x02000000)
GL_MULTISAMPLE_BUFFER_BIT2_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT2_QCOM',0x04000000)
GL_MULTISAMPLE_BUFFER_BIT3_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT3_QCOM',0x08000000)
GL_MULTISAMPLE_BUFFER_BIT4_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT4_QCOM',0x10000000)
GL_MULTISAMPLE_BUFFER_BIT5_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT5_QCOM',0x20000000)
GL_MULTISAMPLE_BUFFER_BIT6_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT6_QCOM',0x40000000)
GL_MULTISAMPLE_BUFFER_BIT7_QCOM=_C('GL_MULTISAMPLE_BUFFER_BIT7_QCOM',0x80000000)
GL_STENCIL_BUFFER_BIT0_QCOM=_C('GL_STENCIL_BUFFER_BIT0_QCOM',0x00010000)
GL_STENCIL_BUFFER_BIT1_QCOM=_C('GL_STENCIL_BUFFER_BIT1_QCOM',0x00020000)
GL_STENCIL_BUFFER_BIT2_QCOM=_C('GL_STENCIL_BUFFER_BIT2_QCOM',0x00040000)
GL_STENCIL_BUFFER_BIT3_QCOM=_C('GL_STENCIL_BUFFER_BIT3_QCOM',0x00080000)
GL_STENCIL_BUFFER_BIT4_QCOM=_C('GL_STENCIL_BUFFER_BIT4_QCOM',0x00100000)
GL_STENCIL_BUFFER_BIT5_QCOM=_C('GL_STENCIL_BUFFER_BIT5_QCOM',0x00200000)
GL_STENCIL_BUFFER_BIT6_QCOM=_C('GL_STENCIL_BUFFER_BIT6_QCOM',0x00400000)
GL_STENCIL_BUFFER_BIT7_QCOM=_C('GL_STENCIL_BUFFER_BIT7_QCOM',0x00800000)
@_f
@_p.types(None,_cs.GLbitfield)
def glEndTilingQCOM(preserveMask):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLbitfield)
def glStartTilingQCOM(x,y,width,height,preserveMask):pass
