'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_vertex_shader'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_vertex_shader',error_checker=_errors._error_checker)
GL_CURRENT_VERTEX_EXT=_C('GL_CURRENT_VERTEX_EXT',0x87E2)
GL_FULL_RANGE_EXT=_C('GL_FULL_RANGE_EXT',0x87E1)
GL_INVARIANT_DATATYPE_EXT=_C('GL_INVARIANT_DATATYPE_EXT',0x87EB)
GL_INVARIANT_EXT=_C('GL_INVARIANT_EXT',0x87C2)
GL_INVARIANT_VALUE_EXT=_C('GL_INVARIANT_VALUE_EXT',0x87EA)
GL_LOCAL_CONSTANT_DATATYPE_EXT=_C('GL_LOCAL_CONSTANT_DATATYPE_EXT',0x87ED)
GL_LOCAL_CONSTANT_EXT=_C('GL_LOCAL_CONSTANT_EXT',0x87C3)
GL_LOCAL_CONSTANT_VALUE_EXT=_C('GL_LOCAL_CONSTANT_VALUE_EXT',0x87EC)
GL_LOCAL_EXT=_C('GL_LOCAL_EXT',0x87C4)
GL_MATRIX_EXT=_C('GL_MATRIX_EXT',0x87C0)
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT=_C('GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT',0x87CA)
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT=_C('GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT',0x87CD)
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT=_C('GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT',0x87CE)
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT=_C('GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT',0x87CC)
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT=_C('GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT',0x87CB)
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT=_C('GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT',0x87C5)
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT=_C('GL_MAX_VERTEX_SHADER_INVARIANTS_EXT',0x87C7)
GL_MAX_VERTEX_SHADER_LOCALS_EXT=_C('GL_MAX_VERTEX_SHADER_LOCALS_EXT',0x87C9)
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT=_C('GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT',0x87C8)
GL_MAX_VERTEX_SHADER_VARIANTS_EXT=_C('GL_MAX_VERTEX_SHADER_VARIANTS_EXT',0x87C6)
GL_MVP_MATRIX_EXT=_C('GL_MVP_MATRIX_EXT',0x87E3)
GL_NEGATIVE_ONE_EXT=_C('GL_NEGATIVE_ONE_EXT',0x87DF)
GL_NEGATIVE_W_EXT=_C('GL_NEGATIVE_W_EXT',0x87DC)
GL_NEGATIVE_X_EXT=_C('GL_NEGATIVE_X_EXT',0x87D9)
GL_NEGATIVE_Y_EXT=_C('GL_NEGATIVE_Y_EXT',0x87DA)
GL_NEGATIVE_Z_EXT=_C('GL_NEGATIVE_Z_EXT',0x87DB)
GL_NORMALIZED_RANGE_EXT=_C('GL_NORMALIZED_RANGE_EXT',0x87E0)
GL_ONE_EXT=_C('GL_ONE_EXT',0x87DE)
GL_OP_ADD_EXT=_C('GL_OP_ADD_EXT',0x8787)
GL_OP_CLAMP_EXT=_C('GL_OP_CLAMP_EXT',0x878E)
GL_OP_CROSS_PRODUCT_EXT=_C('GL_OP_CROSS_PRODUCT_EXT',0x8797)
GL_OP_DOT3_EXT=_C('GL_OP_DOT3_EXT',0x8784)
GL_OP_DOT4_EXT=_C('GL_OP_DOT4_EXT',0x8785)
GL_OP_EXP_BASE_2_EXT=_C('GL_OP_EXP_BASE_2_EXT',0x8791)
GL_OP_FLOOR_EXT=_C('GL_OP_FLOOR_EXT',0x878F)
GL_OP_FRAC_EXT=_C('GL_OP_FRAC_EXT',0x8789)
GL_OP_INDEX_EXT=_C('GL_OP_INDEX_EXT',0x8782)
GL_OP_LOG_BASE_2_EXT=_C('GL_OP_LOG_BASE_2_EXT',0x8792)
GL_OP_MADD_EXT=_C('GL_OP_MADD_EXT',0x8788)
GL_OP_MAX_EXT=_C('GL_OP_MAX_EXT',0x878A)
GL_OP_MIN_EXT=_C('GL_OP_MIN_EXT',0x878B)
GL_OP_MOV_EXT=_C('GL_OP_MOV_EXT',0x8799)
GL_OP_MULTIPLY_MATRIX_EXT=_C('GL_OP_MULTIPLY_MATRIX_EXT',0x8798)
GL_OP_MUL_EXT=_C('GL_OP_MUL_EXT',0x8786)
GL_OP_NEGATE_EXT=_C('GL_OP_NEGATE_EXT',0x8783)
GL_OP_POWER_EXT=_C('GL_OP_POWER_EXT',0x8793)
GL_OP_RECIP_EXT=_C('GL_OP_RECIP_EXT',0x8794)
GL_OP_RECIP_SQRT_EXT=_C('GL_OP_RECIP_SQRT_EXT',0x8795)
GL_OP_ROUND_EXT=_C('GL_OP_ROUND_EXT',0x8790)
GL_OP_SET_GE_EXT=_C('GL_OP_SET_GE_EXT',0x878C)
GL_OP_SET_LT_EXT=_C('GL_OP_SET_LT_EXT',0x878D)
GL_OP_SUB_EXT=_C('GL_OP_SUB_EXT',0x8796)
GL_OUTPUT_COLOR0_EXT=_C('GL_OUTPUT_COLOR0_EXT',0x879B)
GL_OUTPUT_COLOR1_EXT=_C('GL_OUTPUT_COLOR1_EXT',0x879C)
GL_OUTPUT_FOG_EXT=_C('GL_OUTPUT_FOG_EXT',0x87BD)
GL_OUTPUT_TEXTURE_COORD0_EXT=_C('GL_OUTPUT_TEXTURE_COORD0_EXT',0x879D)
GL_OUTPUT_TEXTURE_COORD10_EXT=_C('GL_OUTPUT_TEXTURE_COORD10_EXT',0x87A7)
GL_OUTPUT_TEXTURE_COORD11_EXT=_C('GL_OUTPUT_TEXTURE_COORD11_EXT',0x87A8)
GL_OUTPUT_TEXTURE_COORD12_EXT=_C('GL_OUTPUT_TEXTURE_COORD12_EXT',0x87A9)
GL_OUTPUT_TEXTURE_COORD13_EXT=_C('GL_OUTPUT_TEXTURE_COORD13_EXT',0x87AA)
GL_OUTPUT_TEXTURE_COORD14_EXT=_C('GL_OUTPUT_TEXTURE_COORD14_EXT',0x87AB)
GL_OUTPUT_TEXTURE_COORD15_EXT=_C('GL_OUTPUT_TEXTURE_COORD15_EXT',0x87AC)
GL_OUTPUT_TEXTURE_COORD16_EXT=_C('GL_OUTPUT_TEXTURE_COORD16_EXT',0x87AD)
GL_OUTPUT_TEXTURE_COORD17_EXT=_C('GL_OUTPUT_TEXTURE_COORD17_EXT',0x87AE)
GL_OUTPUT_TEXTURE_COORD18_EXT=_C('GL_OUTPUT_TEXTURE_COORD18_EXT',0x87AF)
GL_OUTPUT_TEXTURE_COORD19_EXT=_C('GL_OUTPUT_TEXTURE_COORD19_EXT',0x87B0)
GL_OUTPUT_TEXTURE_COORD1_EXT=_C('GL_OUTPUT_TEXTURE_COORD1_EXT',0x879E)
GL_OUTPUT_TEXTURE_COORD20_EXT=_C('GL_OUTPUT_TEXTURE_COORD20_EXT',0x87B1)
GL_OUTPUT_TEXTURE_COORD21_EXT=_C('GL_OUTPUT_TEXTURE_COORD21_EXT',0x87B2)
GL_OUTPUT_TEXTURE_COORD22_EXT=_C('GL_OUTPUT_TEXTURE_COORD22_EXT',0x87B3)
GL_OUTPUT_TEXTURE_COORD23_EXT=_C('GL_OUTPUT_TEXTURE_COORD23_EXT',0x87B4)
GL_OUTPUT_TEXTURE_COORD24_EXT=_C('GL_OUTPUT_TEXTURE_COORD24_EXT',0x87B5)
GL_OUTPUT_TEXTURE_COORD25_EXT=_C('GL_OUTPUT_TEXTURE_COORD25_EXT',0x87B6)
GL_OUTPUT_TEXTURE_COORD26_EXT=_C('GL_OUTPUT_TEXTURE_COORD26_EXT',0x87B7)
GL_OUTPUT_TEXTURE_COORD27_EXT=_C('GL_OUTPUT_TEXTURE_COORD27_EXT',0x87B8)
GL_OUTPUT_TEXTURE_COORD28_EXT=_C('GL_OUTPUT_TEXTURE_COORD28_EXT',0x87B9)
GL_OUTPUT_TEXTURE_COORD29_EXT=_C('GL_OUTPUT_TEXTURE_COORD29_EXT',0x87BA)
GL_OUTPUT_TEXTURE_COORD2_EXT=_C('GL_OUTPUT_TEXTURE_COORD2_EXT',0x879F)
GL_OUTPUT_TEXTURE_COORD30_EXT=_C('GL_OUTPUT_TEXTURE_COORD30_EXT',0x87BB)
GL_OUTPUT_TEXTURE_COORD31_EXT=_C('GL_OUTPUT_TEXTURE_COORD31_EXT',0x87BC)
GL_OUTPUT_TEXTURE_COORD3_EXT=_C('GL_OUTPUT_TEXTURE_COORD3_EXT',0x87A0)
GL_OUTPUT_TEXTURE_COORD4_EXT=_C('GL_OUTPUT_TEXTURE_COORD4_EXT',0x87A1)
GL_OUTPUT_TEXTURE_COORD5_EXT=_C('GL_OUTPUT_TEXTURE_COORD5_EXT',0x87A2)
GL_OUTPUT_TEXTURE_COORD6_EXT=_C('GL_OUTPUT_TEXTURE_COORD6_EXT',0x87A3)
GL_OUTPUT_TEXTURE_COORD7_EXT=_C('GL_OUTPUT_TEXTURE_COORD7_EXT',0x87A4)
GL_OUTPUT_TEXTURE_COORD8_EXT=_C('GL_OUTPUT_TEXTURE_COORD8_EXT',0x87A5)
GL_OUTPUT_TEXTURE_COORD9_EXT=_C('GL_OUTPUT_TEXTURE_COORD9_EXT',0x87A6)
GL_OUTPUT_VERTEX_EXT=_C('GL_OUTPUT_VERTEX_EXT',0x879A)
GL_SCALAR_EXT=_C('GL_SCALAR_EXT',0x87BE)
GL_VARIANT_ARRAY_EXT=_C('GL_VARIANT_ARRAY_EXT',0x87E8)
GL_VARIANT_ARRAY_POINTER_EXT=_C('GL_VARIANT_ARRAY_POINTER_EXT',0x87E9)
GL_VARIANT_ARRAY_STRIDE_EXT=_C('GL_VARIANT_ARRAY_STRIDE_EXT',0x87E6)
GL_VARIANT_ARRAY_TYPE_EXT=_C('GL_VARIANT_ARRAY_TYPE_EXT',0x87E7)
GL_VARIANT_DATATYPE_EXT=_C('GL_VARIANT_DATATYPE_EXT',0x87E5)
GL_VARIANT_EXT=_C('GL_VARIANT_EXT',0x87C1)
GL_VARIANT_VALUE_EXT=_C('GL_VARIANT_VALUE_EXT',0x87E4)
GL_VECTOR_EXT=_C('GL_VECTOR_EXT',0x87BF)
GL_VERTEX_SHADER_BINDING_EXT=_C('GL_VERTEX_SHADER_BINDING_EXT',0x8781)
GL_VERTEX_SHADER_EXT=_C('GL_VERTEX_SHADER_EXT',0x8780)
GL_VERTEX_SHADER_INSTRUCTIONS_EXT=_C('GL_VERTEX_SHADER_INSTRUCTIONS_EXT',0x87CF)
GL_VERTEX_SHADER_INVARIANTS_EXT=_C('GL_VERTEX_SHADER_INVARIANTS_EXT',0x87D1)
GL_VERTEX_SHADER_LOCALS_EXT=_C('GL_VERTEX_SHADER_LOCALS_EXT',0x87D3)
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT=_C('GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT',0x87D2)
GL_VERTEX_SHADER_OPTIMIZED_EXT=_C('GL_VERTEX_SHADER_OPTIMIZED_EXT',0x87D4)
GL_VERTEX_SHADER_VARIANTS_EXT=_C('GL_VERTEX_SHADER_VARIANTS_EXT',0x87D0)
GL_W_EXT=_C('GL_W_EXT',0x87D8)
GL_X_EXT=_C('GL_X_EXT',0x87D5)
GL_Y_EXT=_C('GL_Y_EXT',0x87D6)
GL_ZERO_EXT=_C('GL_ZERO_EXT',0x87DD)
GL_Z_EXT=_C('GL_Z_EXT',0x87D7)
@_f
@_p.types(None,)
def glBeginVertexShaderEXT():pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBindLightParameterEXT(light,value):pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBindMaterialParameterEXT(face,value):pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum)
def glBindParameterEXT(value):pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glBindTexGenParameterEXT(unit,coord,value):pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBindTextureUnitParameterEXT(unit,value):pass
@_f
@_p.types(None,_cs.GLuint)
def glBindVertexShaderEXT(id):pass
@_f
@_p.types(None,_cs.GLuint)
def glDeleteVertexShaderEXT(id):pass
@_f
@_p.types(None,_cs.GLuint)
def glDisableVariantClientStateEXT(id):pass
@_f
@_p.types(None,_cs.GLuint)
def glEnableVariantClientStateEXT(id):pass
@_f
@_p.types(None,)
def glEndVertexShaderEXT():pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glExtractComponentEXT(res,src,num):pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glGenSymbolsEXT(datatype,storagetype,range,components):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint)
def glGenVertexShadersEXT(range):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLbooleanArray)
def glGetInvariantBooleanvEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetInvariantFloatvEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetInvariantIntegervEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLbooleanArray)
def glGetLocalConstantBooleanvEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetLocalConstantFloatvEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetLocalConstantIntegervEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLbooleanArray)
def glGetVariantBooleanvEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetVariantFloatvEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVariantIntegervEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLvoidpArray)
def glGetVariantPointervEXT(id,value,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glInsertComponentEXT(res,src,num):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint,_cs.GLenum)
def glIsVariantEnabledEXT(id,cap):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p)
def glSetInvariantEXT(id,type,addr):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p)
def glSetLocalConstantEXT(id,type,addr):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glShaderOp1EXT(op,res,arg1):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glShaderOp2EXT(op,res,arg1,arg2):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glShaderOp3EXT(op,res,arg1,arg2,arg3):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glSwizzleEXT(res,in_,outX,outY,outZ,outW):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,ctypes.c_void_p)
def glVariantPointerEXT(id,type,stride,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLbyteArray)
def glVariantbvEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVariantdvEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVariantfvEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVariantivEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVariantsvEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glVariantubvEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVariantuivEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVariantusvEXT(id,addr):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glWriteMaskEXT(res,in_,outX,outY,outZ,outW):pass
