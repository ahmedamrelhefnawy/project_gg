'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_register_combiners'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_register_combiners',error_checker=_errors._error_checker)
GL_BIAS_BY_NEGATIVE_ONE_HALF_NV=_C('GL_BIAS_BY_NEGATIVE_ONE_HALF_NV',0x8541)
GL_COLOR_SUM_CLAMP_NV=_C('GL_COLOR_SUM_CLAMP_NV',0x854F)
GL_COMBINER0_NV=_C('GL_COMBINER0_NV',0x8550)
GL_COMBINER1_NV=_C('GL_COMBINER1_NV',0x8551)
GL_COMBINER2_NV=_C('GL_COMBINER2_NV',0x8552)
GL_COMBINER3_NV=_C('GL_COMBINER3_NV',0x8553)
GL_COMBINER4_NV=_C('GL_COMBINER4_NV',0x8554)
GL_COMBINER5_NV=_C('GL_COMBINER5_NV',0x8555)
GL_COMBINER6_NV=_C('GL_COMBINER6_NV',0x8556)
GL_COMBINER7_NV=_C('GL_COMBINER7_NV',0x8557)
GL_COMBINER_AB_DOT_PRODUCT_NV=_C('GL_COMBINER_AB_DOT_PRODUCT_NV',0x8545)
GL_COMBINER_AB_OUTPUT_NV=_C('GL_COMBINER_AB_OUTPUT_NV',0x854A)
GL_COMBINER_BIAS_NV=_C('GL_COMBINER_BIAS_NV',0x8549)
GL_COMBINER_CD_DOT_PRODUCT_NV=_C('GL_COMBINER_CD_DOT_PRODUCT_NV',0x8546)
GL_COMBINER_CD_OUTPUT_NV=_C('GL_COMBINER_CD_OUTPUT_NV',0x854B)
GL_COMBINER_COMPONENT_USAGE_NV=_C('GL_COMBINER_COMPONENT_USAGE_NV',0x8544)
GL_COMBINER_INPUT_NV=_C('GL_COMBINER_INPUT_NV',0x8542)
GL_COMBINER_MAPPING_NV=_C('GL_COMBINER_MAPPING_NV',0x8543)
GL_COMBINER_MUX_SUM_NV=_C('GL_COMBINER_MUX_SUM_NV',0x8547)
GL_COMBINER_SCALE_NV=_C('GL_COMBINER_SCALE_NV',0x8548)
GL_COMBINER_SUM_OUTPUT_NV=_C('GL_COMBINER_SUM_OUTPUT_NV',0x854C)
GL_CONSTANT_COLOR0_NV=_C('GL_CONSTANT_COLOR0_NV',0x852A)
GL_CONSTANT_COLOR1_NV=_C('GL_CONSTANT_COLOR1_NV',0x852B)
GL_DISCARD_NV=_C('GL_DISCARD_NV',0x8530)
GL_EXPAND_NEGATE_NV=_C('GL_EXPAND_NEGATE_NV',0x8539)
GL_EXPAND_NORMAL_NV=_C('GL_EXPAND_NORMAL_NV',0x8538)
GL_E_TIMES_F_NV=_C('GL_E_TIMES_F_NV',0x8531)
GL_FOG=_C('GL_FOG',0x0B60)
GL_HALF_BIAS_NEGATE_NV=_C('GL_HALF_BIAS_NEGATE_NV',0x853B)
GL_HALF_BIAS_NORMAL_NV=_C('GL_HALF_BIAS_NORMAL_NV',0x853A)
GL_MAX_GENERAL_COMBINERS_NV=_C('GL_MAX_GENERAL_COMBINERS_NV',0x854D)
GL_NONE=_C('GL_NONE',0)
GL_NUM_GENERAL_COMBINERS_NV=_C('GL_NUM_GENERAL_COMBINERS_NV',0x854E)
GL_PRIMARY_COLOR_NV=_C('GL_PRIMARY_COLOR_NV',0x852C)
GL_REGISTER_COMBINERS_NV=_C('GL_REGISTER_COMBINERS_NV',0x8522)
GL_SCALE_BY_FOUR_NV=_C('GL_SCALE_BY_FOUR_NV',0x853F)
GL_SCALE_BY_ONE_HALF_NV=_C('GL_SCALE_BY_ONE_HALF_NV',0x8540)
GL_SCALE_BY_TWO_NV=_C('GL_SCALE_BY_TWO_NV',0x853E)
GL_SECONDARY_COLOR_NV=_C('GL_SECONDARY_COLOR_NV',0x852D)
GL_SIGNED_IDENTITY_NV=_C('GL_SIGNED_IDENTITY_NV',0x853C)
GL_SIGNED_NEGATE_NV=_C('GL_SIGNED_NEGATE_NV',0x853D)
GL_SPARE0_NV=_C('GL_SPARE0_NV',0x852E)
GL_SPARE0_PLUS_SECONDARY_COLOR_NV=_C('GL_SPARE0_PLUS_SECONDARY_COLOR_NV',0x8532)
GL_SPARE1_NV=_C('GL_SPARE1_NV',0x852F)
GL_TEXTURE0_ARB=_C('GL_TEXTURE0_ARB',0x84C0)
GL_TEXTURE1_ARB=_C('GL_TEXTURE1_ARB',0x84C1)
GL_UNSIGNED_IDENTITY_NV=_C('GL_UNSIGNED_IDENTITY_NV',0x8536)
GL_UNSIGNED_INVERT_NV=_C('GL_UNSIGNED_INVERT_NV',0x8537)
GL_VARIABLE_A_NV=_C('GL_VARIABLE_A_NV',0x8523)
GL_VARIABLE_B_NV=_C('GL_VARIABLE_B_NV',0x8524)
GL_VARIABLE_C_NV=_C('GL_VARIABLE_C_NV',0x8525)
GL_VARIABLE_D_NV=_C('GL_VARIABLE_D_NV',0x8526)
GL_VARIABLE_E_NV=_C('GL_VARIABLE_E_NV',0x8527)
GL_VARIABLE_F_NV=_C('GL_VARIABLE_F_NV',0x8528)
GL_VARIABLE_G_NV=_C('GL_VARIABLE_G_NV',0x8529)
GL_ZERO=_C('GL_ZERO',0)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glCombinerInputNV(stage,portion,variable,input,mapping,componentUsage):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glCombinerOutputNV(stage,portion,abOutput,cdOutput,sumOutput,scale,bias,abDotProduct,cdDotProduct,muxSum):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glCombinerParameterfNV(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glCombinerParameterfvNV(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glCombinerParameteriNV(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glCombinerParameterivNV(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glFinalCombinerInputNV(variable,input,mapping,componentUsage):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetCombinerInputParameterfvNV(stage,portion,variable,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetCombinerInputParameterivNV(stage,portion,variable,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetCombinerOutputParameterfvNV(stage,portion,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetCombinerOutputParameterivNV(stage,portion,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetFinalCombinerInputParameterfvNV(variable,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFinalCombinerInputParameterivNV(variable,pname,params):pass
