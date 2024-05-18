'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_QCOM_binning_control'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_QCOM_binning_control',error_checker=_errors._error_checker)
GL_BINNING_CONTROL_HINT_QCOM=_C('GL_BINNING_CONTROL_HINT_QCOM',0x8FB0)
GL_CPU_OPTIMIZED_QCOM=_C('GL_CPU_OPTIMIZED_QCOM',0x8FB1)
GL_GPU_OPTIMIZED_QCOM=_C('GL_GPU_OPTIMIZED_QCOM',0x8FB2)
GL_RENDER_DIRECT_TO_FRAMEBUFFER_QCOM=_C('GL_RENDER_DIRECT_TO_FRAMEBUFFER_QCOM',0x8FB3)

