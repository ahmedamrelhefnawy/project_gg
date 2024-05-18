'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_path_rendering'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_path_rendering',error_checker=_errors._error_checker)
GL_2_BYTES_NV=_C('GL_2_BYTES_NV',0x1407)
GL_3_BYTES_NV=_C('GL_3_BYTES_NV',0x1408)
GL_4_BYTES_NV=_C('GL_4_BYTES_NV',0x1409)
GL_ACCUM_ADJACENT_PAIRS_NV=_C('GL_ACCUM_ADJACENT_PAIRS_NV',0x90AD)
GL_ADJACENT_PAIRS_NV=_C('GL_ADJACENT_PAIRS_NV',0x90AE)
GL_AFFINE_2D_NV=_C('GL_AFFINE_2D_NV',0x9092)
GL_AFFINE_3D_NV=_C('GL_AFFINE_3D_NV',0x9094)
GL_ARC_TO_NV=_C('GL_ARC_TO_NV',0xFE)
GL_BEVEL_NV=_C('GL_BEVEL_NV',0x90A6)
GL_BOLD_BIT_NV=_C('GL_BOLD_BIT_NV',0x01)
GL_BOUNDING_BOX_NV=_C('GL_BOUNDING_BOX_NV',0x908D)
GL_BOUNDING_BOX_OF_BOUNDING_BOXES_NV=_C('GL_BOUNDING_BOX_OF_BOUNDING_BOXES_NV',0x909C)
GL_CIRCULAR_CCW_ARC_TO_NV=_C('GL_CIRCULAR_CCW_ARC_TO_NV',0xF8)
GL_CIRCULAR_CW_ARC_TO_NV=_C('GL_CIRCULAR_CW_ARC_TO_NV',0xFA)
GL_CIRCULAR_TANGENT_ARC_TO_NV=_C('GL_CIRCULAR_TANGENT_ARC_TO_NV',0xFC)
GL_CLOSE_PATH_NV=_C('GL_CLOSE_PATH_NV',0x00)
GL_CONIC_CURVE_TO_NV=_C('GL_CONIC_CURVE_TO_NV',0x1A)
GL_CONSTANT_NV=_C('GL_CONSTANT_NV',0x8576)
GL_CONVEX_HULL_NV=_C('GL_CONVEX_HULL_NV',0x908B)
GL_COUNT_DOWN_NV=_C('GL_COUNT_DOWN_NV',0x9089)
GL_COUNT_UP_NV=_C('GL_COUNT_UP_NV',0x9088)
GL_CUBIC_CURVE_TO_NV=_C('GL_CUBIC_CURVE_TO_NV',0x0C)
GL_DUP_FIRST_CUBIC_CURVE_TO_NV=_C('GL_DUP_FIRST_CUBIC_CURVE_TO_NV',0xF2)
GL_DUP_LAST_CUBIC_CURVE_TO_NV=_C('GL_DUP_LAST_CUBIC_CURVE_TO_NV',0xF4)
GL_EYE_LINEAR_NV=_C('GL_EYE_LINEAR_NV',0x2400)
GL_FILE_NAME_NV=_C('GL_FILE_NAME_NV',0x9074)
GL_FIRST_TO_REST_NV=_C('GL_FIRST_TO_REST_NV',0x90AF)
GL_FONT_ASCENDER_BIT_NV=_C('GL_FONT_ASCENDER_BIT_NV',0x00200000)
GL_FONT_DESCENDER_BIT_NV=_C('GL_FONT_DESCENDER_BIT_NV',0x00400000)
GL_FONT_GLYPHS_AVAILABLE_NV=_C('GL_FONT_GLYPHS_AVAILABLE_NV',0x9368)
GL_FONT_HAS_KERNING_BIT_NV=_C('GL_FONT_HAS_KERNING_BIT_NV',0x10000000)
GL_FONT_HEIGHT_BIT_NV=_C('GL_FONT_HEIGHT_BIT_NV',0x00800000)
GL_FONT_MAX_ADVANCE_HEIGHT_BIT_NV=_C('GL_FONT_MAX_ADVANCE_HEIGHT_BIT_NV',0x02000000)
GL_FONT_MAX_ADVANCE_WIDTH_BIT_NV=_C('GL_FONT_MAX_ADVANCE_WIDTH_BIT_NV',0x01000000)
GL_FONT_NUM_GLYPH_INDICES_BIT_NV=_C('GL_FONT_NUM_GLYPH_INDICES_BIT_NV',0x20000000)
GL_FONT_TARGET_UNAVAILABLE_NV=_C('GL_FONT_TARGET_UNAVAILABLE_NV',0x9369)
GL_FONT_UNAVAILABLE_NV=_C('GL_FONT_UNAVAILABLE_NV',0x936A)
GL_FONT_UNDERLINE_POSITION_BIT_NV=_C('GL_FONT_UNDERLINE_POSITION_BIT_NV',0x04000000)
GL_FONT_UNDERLINE_THICKNESS_BIT_NV=_C('GL_FONT_UNDERLINE_THICKNESS_BIT_NV',0x08000000)
GL_FONT_UNINTELLIGIBLE_NV=_C('GL_FONT_UNINTELLIGIBLE_NV',0x936B)
GL_FONT_UNITS_PER_EM_BIT_NV=_C('GL_FONT_UNITS_PER_EM_BIT_NV',0x00100000)
GL_FONT_X_MAX_BOUNDS_BIT_NV=_C('GL_FONT_X_MAX_BOUNDS_BIT_NV',0x00040000)
GL_FONT_X_MIN_BOUNDS_BIT_NV=_C('GL_FONT_X_MIN_BOUNDS_BIT_NV',0x00010000)
GL_FONT_Y_MAX_BOUNDS_BIT_NV=_C('GL_FONT_Y_MAX_BOUNDS_BIT_NV',0x00080000)
GL_FONT_Y_MIN_BOUNDS_BIT_NV=_C('GL_FONT_Y_MIN_BOUNDS_BIT_NV',0x00020000)
GL_FRAGMENT_INPUT_NV=_C('GL_FRAGMENT_INPUT_NV',0x936D)
GL_GLYPH_HAS_KERNING_BIT_NV=_C('GL_GLYPH_HAS_KERNING_BIT_NV',0x100)
GL_GLYPH_HEIGHT_BIT_NV=_C('GL_GLYPH_HEIGHT_BIT_NV',0x02)
GL_GLYPH_HORIZONTAL_BEARING_ADVANCE_BIT_NV=_C('GL_GLYPH_HORIZONTAL_BEARING_ADVANCE_BIT_NV',0x10)
GL_GLYPH_HORIZONTAL_BEARING_X_BIT_NV=_C('GL_GLYPH_HORIZONTAL_BEARING_X_BIT_NV',0x04)
GL_GLYPH_HORIZONTAL_BEARING_Y_BIT_NV=_C('GL_GLYPH_HORIZONTAL_BEARING_Y_BIT_NV',0x08)
GL_GLYPH_VERTICAL_BEARING_ADVANCE_BIT_NV=_C('GL_GLYPH_VERTICAL_BEARING_ADVANCE_BIT_NV',0x80)
GL_GLYPH_VERTICAL_BEARING_X_BIT_NV=_C('GL_GLYPH_VERTICAL_BEARING_X_BIT_NV',0x20)
GL_GLYPH_VERTICAL_BEARING_Y_BIT_NV=_C('GL_GLYPH_VERTICAL_BEARING_Y_BIT_NV',0x40)
GL_GLYPH_WIDTH_BIT_NV=_C('GL_GLYPH_WIDTH_BIT_NV',0x01)
GL_HORIZONTAL_LINE_TO_NV=_C('GL_HORIZONTAL_LINE_TO_NV',0x06)
GL_ITALIC_BIT_NV=_C('GL_ITALIC_BIT_NV',0x02)
GL_LARGE_CCW_ARC_TO_NV=_C('GL_LARGE_CCW_ARC_TO_NV',0x16)
GL_LARGE_CW_ARC_TO_NV=_C('GL_LARGE_CW_ARC_TO_NV',0x18)
GL_LINE_TO_NV=_C('GL_LINE_TO_NV',0x04)
GL_MITER_REVERT_NV=_C('GL_MITER_REVERT_NV',0x90A7)
GL_MITER_TRUNCATE_NV=_C('GL_MITER_TRUNCATE_NV',0x90A8)
GL_MOVE_TO_CONTINUES_NV=_C('GL_MOVE_TO_CONTINUES_NV',0x90B6)
GL_MOVE_TO_NV=_C('GL_MOVE_TO_NV',0x02)
GL_MOVE_TO_RESETS_NV=_C('GL_MOVE_TO_RESETS_NV',0x90B5)
GL_OBJECT_LINEAR_NV=_C('GL_OBJECT_LINEAR_NV',0x2401)
GL_PATH_CLIENT_LENGTH_NV=_C('GL_PATH_CLIENT_LENGTH_NV',0x907F)
GL_PATH_COMMAND_COUNT_NV=_C('GL_PATH_COMMAND_COUNT_NV',0x909D)
GL_PATH_COMPUTED_LENGTH_NV=_C('GL_PATH_COMPUTED_LENGTH_NV',0x90A0)
GL_PATH_COORD_COUNT_NV=_C('GL_PATH_COORD_COUNT_NV',0x909E)
GL_PATH_COVER_DEPTH_FUNC_NV=_C('GL_PATH_COVER_DEPTH_FUNC_NV',0x90BF)
GL_PATH_DASH_ARRAY_COUNT_NV=_C('GL_PATH_DASH_ARRAY_COUNT_NV',0x909F)
GL_PATH_DASH_CAPS_NV=_C('GL_PATH_DASH_CAPS_NV',0x907B)
GL_PATH_DASH_OFFSET_NV=_C('GL_PATH_DASH_OFFSET_NV',0x907E)
GL_PATH_DASH_OFFSET_RESET_NV=_C('GL_PATH_DASH_OFFSET_RESET_NV',0x90B4)
GL_PATH_END_CAPS_NV=_C('GL_PATH_END_CAPS_NV',0x9076)
GL_PATH_ERROR_POSITION_NV=_C('GL_PATH_ERROR_POSITION_NV',0x90AB)
GL_PATH_FILL_BOUNDING_BOX_NV=_C('GL_PATH_FILL_BOUNDING_BOX_NV',0x90A1)
GL_PATH_FILL_COVER_MODE_NV=_C('GL_PATH_FILL_COVER_MODE_NV',0x9082)
GL_PATH_FILL_MASK_NV=_C('GL_PATH_FILL_MASK_NV',0x9081)
GL_PATH_FILL_MODE_NV=_C('GL_PATH_FILL_MODE_NV',0x9080)
GL_PATH_FOG_GEN_MODE_NV=_C('GL_PATH_FOG_GEN_MODE_NV',0x90AC)
GL_PATH_FORMAT_PS_NV=_C('GL_PATH_FORMAT_PS_NV',0x9071)
GL_PATH_FORMAT_SVG_NV=_C('GL_PATH_FORMAT_SVG_NV',0x9070)
GL_PATH_GEN_COEFF_NV=_C('GL_PATH_GEN_COEFF_NV',0x90B1)
GL_PATH_GEN_COLOR_FORMAT_NV=_C('GL_PATH_GEN_COLOR_FORMAT_NV',0x90B2)
GL_PATH_GEN_COMPONENTS_NV=_C('GL_PATH_GEN_COMPONENTS_NV',0x90B3)
GL_PATH_GEN_MODE_NV=_C('GL_PATH_GEN_MODE_NV',0x90B0)
GL_PATH_INITIAL_DASH_CAP_NV=_C('GL_PATH_INITIAL_DASH_CAP_NV',0x907C)
GL_PATH_INITIAL_END_CAP_NV=_C('GL_PATH_INITIAL_END_CAP_NV',0x9077)
GL_PATH_JOIN_STYLE_NV=_C('GL_PATH_JOIN_STYLE_NV',0x9079)
GL_PATH_MAX_MODELVIEW_STACK_DEPTH_NV=_C('GL_PATH_MAX_MODELVIEW_STACK_DEPTH_NV',0x0D36)
GL_PATH_MAX_PROJECTION_STACK_DEPTH_NV=_C('GL_PATH_MAX_PROJECTION_STACK_DEPTH_NV',0x0D38)
GL_PATH_MITER_LIMIT_NV=_C('GL_PATH_MITER_LIMIT_NV',0x907A)
GL_PATH_MODELVIEW_MATRIX_NV=_C('GL_PATH_MODELVIEW_MATRIX_NV',0x0BA6)
GL_PATH_MODELVIEW_NV=_C('GL_PATH_MODELVIEW_NV',0x1700)
GL_PATH_MODELVIEW_STACK_DEPTH_NV=_C('GL_PATH_MODELVIEW_STACK_DEPTH_NV',0x0BA3)
GL_PATH_OBJECT_BOUNDING_BOX_NV=_C('GL_PATH_OBJECT_BOUNDING_BOX_NV',0x908A)
GL_PATH_PROJECTION_MATRIX_NV=_C('GL_PATH_PROJECTION_MATRIX_NV',0x0BA7)
GL_PATH_PROJECTION_NV=_C('GL_PATH_PROJECTION_NV',0x1701)
GL_PATH_PROJECTION_STACK_DEPTH_NV=_C('GL_PATH_PROJECTION_STACK_DEPTH_NV',0x0BA4)
GL_PATH_STENCIL_DEPTH_OFFSET_FACTOR_NV=_C('GL_PATH_STENCIL_DEPTH_OFFSET_FACTOR_NV',0x90BD)
GL_PATH_STENCIL_DEPTH_OFFSET_UNITS_NV=_C('GL_PATH_STENCIL_DEPTH_OFFSET_UNITS_NV',0x90BE)
GL_PATH_STENCIL_FUNC_NV=_C('GL_PATH_STENCIL_FUNC_NV',0x90B7)
GL_PATH_STENCIL_REF_NV=_C('GL_PATH_STENCIL_REF_NV',0x90B8)
GL_PATH_STENCIL_VALUE_MASK_NV=_C('GL_PATH_STENCIL_VALUE_MASK_NV',0x90B9)
GL_PATH_STROKE_BOUNDING_BOX_NV=_C('GL_PATH_STROKE_BOUNDING_BOX_NV',0x90A2)
GL_PATH_STROKE_COVER_MODE_NV=_C('GL_PATH_STROKE_COVER_MODE_NV',0x9083)
GL_PATH_STROKE_MASK_NV=_C('GL_PATH_STROKE_MASK_NV',0x9084)
GL_PATH_STROKE_WIDTH_NV=_C('GL_PATH_STROKE_WIDTH_NV',0x9075)
GL_PATH_TERMINAL_DASH_CAP_NV=_C('GL_PATH_TERMINAL_DASH_CAP_NV',0x907D)
GL_PATH_TERMINAL_END_CAP_NV=_C('GL_PATH_TERMINAL_END_CAP_NV',0x9078)
GL_PATH_TRANSPOSE_MODELVIEW_MATRIX_NV=_C('GL_PATH_TRANSPOSE_MODELVIEW_MATRIX_NV',0x84E3)
GL_PATH_TRANSPOSE_PROJECTION_MATRIX_NV=_C('GL_PATH_TRANSPOSE_PROJECTION_MATRIX_NV',0x84E4)
GL_PRIMARY_COLOR=_C('GL_PRIMARY_COLOR',0x8577)
GL_PRIMARY_COLOR_NV=_C('GL_PRIMARY_COLOR_NV',0x852C)
GL_QUADRATIC_CURVE_TO_NV=_C('GL_QUADRATIC_CURVE_TO_NV',0x0A)
GL_RECT_NV=_C('GL_RECT_NV',0xF6)
GL_RELATIVE_ARC_TO_NV=_C('GL_RELATIVE_ARC_TO_NV',0xFF)
GL_RELATIVE_CONIC_CURVE_TO_NV=_C('GL_RELATIVE_CONIC_CURVE_TO_NV',0x1B)
GL_RELATIVE_CUBIC_CURVE_TO_NV=_C('GL_RELATIVE_CUBIC_CURVE_TO_NV',0x0D)
GL_RELATIVE_HORIZONTAL_LINE_TO_NV=_C('GL_RELATIVE_HORIZONTAL_LINE_TO_NV',0x07)
GL_RELATIVE_LARGE_CCW_ARC_TO_NV=_C('GL_RELATIVE_LARGE_CCW_ARC_TO_NV',0x17)
GL_RELATIVE_LARGE_CW_ARC_TO_NV=_C('GL_RELATIVE_LARGE_CW_ARC_TO_NV',0x19)
GL_RELATIVE_LINE_TO_NV=_C('GL_RELATIVE_LINE_TO_NV',0x05)
GL_RELATIVE_MOVE_TO_NV=_C('GL_RELATIVE_MOVE_TO_NV',0x03)
GL_RELATIVE_QUADRATIC_CURVE_TO_NV=_C('GL_RELATIVE_QUADRATIC_CURVE_TO_NV',0x0B)
GL_RELATIVE_RECT_NV=_C('GL_RELATIVE_RECT_NV',0xF7)
GL_RELATIVE_ROUNDED_RECT2_NV=_C('GL_RELATIVE_ROUNDED_RECT2_NV',0xEB)
GL_RELATIVE_ROUNDED_RECT4_NV=_C('GL_RELATIVE_ROUNDED_RECT4_NV',0xED)
GL_RELATIVE_ROUNDED_RECT8_NV=_C('GL_RELATIVE_ROUNDED_RECT8_NV',0xEF)
GL_RELATIVE_ROUNDED_RECT_NV=_C('GL_RELATIVE_ROUNDED_RECT_NV',0xE9)
GL_RELATIVE_SMALL_CCW_ARC_TO_NV=_C('GL_RELATIVE_SMALL_CCW_ARC_TO_NV',0x13)
GL_RELATIVE_SMALL_CW_ARC_TO_NV=_C('GL_RELATIVE_SMALL_CW_ARC_TO_NV',0x15)
GL_RELATIVE_SMOOTH_CUBIC_CURVE_TO_NV=_C('GL_RELATIVE_SMOOTH_CUBIC_CURVE_TO_NV',0x11)
GL_RELATIVE_SMOOTH_QUADRATIC_CURVE_TO_NV=_C('GL_RELATIVE_SMOOTH_QUADRATIC_CURVE_TO_NV',0x0F)
GL_RELATIVE_VERTICAL_LINE_TO_NV=_C('GL_RELATIVE_VERTICAL_LINE_TO_NV',0x09)
GL_RESTART_PATH_NV=_C('GL_RESTART_PATH_NV',0xF0)
GL_ROUNDED_RECT2_NV=_C('GL_ROUNDED_RECT2_NV',0xEA)
GL_ROUNDED_RECT4_NV=_C('GL_ROUNDED_RECT4_NV',0xEC)
GL_ROUNDED_RECT8_NV=_C('GL_ROUNDED_RECT8_NV',0xEE)
GL_ROUNDED_RECT_NV=_C('GL_ROUNDED_RECT_NV',0xE8)
GL_ROUND_NV=_C('GL_ROUND_NV',0x90A4)
GL_SECONDARY_COLOR_NV=_C('GL_SECONDARY_COLOR_NV',0x852D)
GL_SKIP_MISSING_GLYPH_NV=_C('GL_SKIP_MISSING_GLYPH_NV',0x90A9)
GL_SMALL_CCW_ARC_TO_NV=_C('GL_SMALL_CCW_ARC_TO_NV',0x12)
GL_SMALL_CW_ARC_TO_NV=_C('GL_SMALL_CW_ARC_TO_NV',0x14)
GL_SMOOTH_CUBIC_CURVE_TO_NV=_C('GL_SMOOTH_CUBIC_CURVE_TO_NV',0x10)
GL_SMOOTH_QUADRATIC_CURVE_TO_NV=_C('GL_SMOOTH_QUADRATIC_CURVE_TO_NV',0x0E)
GL_SQUARE_NV=_C('GL_SQUARE_NV',0x90A3)
GL_STANDARD_FONT_FORMAT_NV=_C('GL_STANDARD_FONT_FORMAT_NV',0x936C)
GL_STANDARD_FONT_NAME_NV=_C('GL_STANDARD_FONT_NAME_NV',0x9072)
GL_SYSTEM_FONT_NAME_NV=_C('GL_SYSTEM_FONT_NAME_NV',0x9073)
GL_TRANSLATE_2D_NV=_C('GL_TRANSLATE_2D_NV',0x9090)
GL_TRANSLATE_3D_NV=_C('GL_TRANSLATE_3D_NV',0x9091)
GL_TRANSLATE_X_NV=_C('GL_TRANSLATE_X_NV',0x908E)
GL_TRANSLATE_Y_NV=_C('GL_TRANSLATE_Y_NV',0x908F)
GL_TRANSPOSE_AFFINE_2D_NV=_C('GL_TRANSPOSE_AFFINE_2D_NV',0x9096)
GL_TRANSPOSE_AFFINE_3D_NV=_C('GL_TRANSPOSE_AFFINE_3D_NV',0x9098)
GL_TRIANGULAR_NV=_C('GL_TRIANGULAR_NV',0x90A5)
GL_USE_MISSING_GLYPH_NV=_C('GL_USE_MISSING_GLYPH_NV',0x90AA)
GL_UTF16_NV=_C('GL_UTF16_NV',0x909B)
GL_UTF8_NV=_C('GL_UTF8_NV',0x909A)
GL_VERTICAL_LINE_TO_NV=_C('GL_VERTICAL_LINE_TO_NV',0x08)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glCopyPathNV(resultPath,srcPath):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glCoverFillPathInstancedNV(numPaths,pathNameType,paths,pathBase,coverMode,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glCoverFillPathNV(path,coverMode):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glCoverStrokePathInstancedNV(numPaths,pathNameType,paths,pathBase,coverMode,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glCoverStrokePathNV(path,coverMode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei)
def glDeletePathsNV(path,range):pass
@_f
@_p.types(_cs.GLuint,_cs.GLsizei)
def glGenPathsNV(range):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetPathColorGenfvNV(color,pname,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetPathColorGenivNV(color,pname,value):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glGetPathCommandsNV(path,commands):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glGetPathCoordsNV(path,coords):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glGetPathDashArrayNV(path,dashArray):pass
@_f
@_p.types(_cs.GLfloat,_cs.GLuint,_cs.GLsizei,_cs.GLsizei)
def glGetPathLengthNV(path,startSegment,numSegments):pass
@_f
@_p.types(None,_cs.GLbitfield,_cs.GLuint,_cs.GLsizei,_cs.GLsizei,arrays.GLfloatArray)
def glGetPathMetricRangeNV(metricQueryMask,firstPathName,numPaths,stride,metrics):pass
@_f
@_p.types(None,_cs.GLbitfield,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glGetPathMetricsNV(metricQueryMask,numPaths,pathNameType,paths,pathBase,stride,metrics):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetPathParameterfvNV(path,pname,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetPathParameterivNV(path,pname,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLenum,arrays.GLfloatArray)
def glGetPathSpacingNV(pathListMode,numPaths,pathNameType,paths,pathBase,advanceScale,kerningScale,transformType,returnedSpacing):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetPathTexGenfvNV(texCoordSet,pname,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetPathTexGenivNV(texCoordSet,pname,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLfloatArray)
def glGetProgramResourcefvNV(program,programInterface,index,propCount,props,bufSize,length,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLfloat)
def glInterpolatePathsNV(resultPath,pathA,pathB,weight):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsPathNV(path):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint,_cs.GLuint,_cs.GLfloat,_cs.GLfloat)
def glIsPointInFillPathNV(path,mask,x,y):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint,_cs.GLfloat,_cs.GLfloat)
def glIsPointInStrokePathNV(path,x,y):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixFrustumEXT(mode,left,right,bottom,top,zNear,zFar):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoad3x2fNV(matrixMode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoad3x3fNV(matrixMode,m):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixLoadIdentityEXT(mode):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoadTranspose3x3fNV(matrixMode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixLoadTransposedEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoadTransposefEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixLoaddEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoadfEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMult3x2fNV(matrixMode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMult3x3fNV(matrixMode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMultTranspose3x3fNV(matrixMode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixMultTransposedEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMultTransposefEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixMultdEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMultfEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixOrthoEXT(mode,left,right,bottom,top,zNear,zFar):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixPopEXT(mode):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixPushEXT(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixRotatedEXT(mode,angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMatrixRotatefEXT(mode,angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixScaledEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMatrixScalefEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixTranslatedEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMatrixTranslatefEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glPathColorGenNV(color,genMode,colorFormat,coeffs):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glPathCommandsNV(path,numCommands,commands,numCoords,coordType,coords):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glPathCoordsNV(path,numCoords,coordType,coords):pass
@_f
@_p.types(None,_cs.GLenum)
def glPathCoverDepthFuncNV(func):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glPathDashArrayNV(path,dashCount,dashArray):pass
@_f
@_p.types(None,_cs.GLenum)
def glPathFogGenNV(genMode):pass
@_f
@_p.types(_cs.GLenum,_cs.GLuint,_cs.GLenum,ctypes.c_void_p,_cs.GLbitfield,_cs.GLuint,_cs.GLsizei,_cs.GLuint,_cs.GLfloat)
def glPathGlyphIndexArrayNV(firstPathName,fontTarget,fontName,fontStyle,firstGlyphIndex,numGlyphs,pathParameterTemplate,emScale):pass
@_f
@_p.types(_cs.GLenum,_cs.GLenum,ctypes.c_void_p,_cs.GLbitfield,_cs.GLuint,_cs.GLfloat,_cs.GLuint)
def glPathGlyphIndexRangeNV(fontTarget,fontName,fontStyle,pathParameterTemplate,emScale,baseAndCount):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p,_cs.GLbitfield,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLuint,_cs.GLfloat)
def glPathGlyphRangeNV(firstPathName,fontTarget,fontName,fontStyle,firstGlyph,numGlyphs,handleMissingGlyphs,pathParameterTemplate,emScale):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p,_cs.GLbitfield,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLenum,_cs.GLuint,_cs.GLfloat)
def glPathGlyphsNV(firstPathName,fontTarget,fontName,fontStyle,numGlyphs,type,charcodes,handleMissingGlyphs,pathParameterTemplate,emScale):pass
@_f
@_p.types(_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLsizei,_cs.GLuint,_cs.GLsizei,_cs.GLuint,_cs.GLfloat)
def glPathMemoryGlyphIndexArrayNV(firstPathName,fontTarget,fontSize,fontData,faceIndex,firstGlyphIndex,numGlyphs,pathParameterTemplate,emScale):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLfloat)
def glPathParameterfNV(path,pname,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glPathParameterfvNV(path,pname,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glPathParameteriNV(path,pname,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glPathParameterivNV(path,pname,value):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glPathStencilDepthOffsetNV(factor,units):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glPathStencilFuncNV(func,ref,mask):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glPathStringNV(path,format,length,pathString):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,arrays.GLubyteArray,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glPathSubCommandsNV(path,commandStart,commandsToDelete,numCommands,commands,numCoords,coordType,coords):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glPathSubCoordsNV(path,coordStart,numCoords,coordType,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,arrays.GLfloatArray)
def glPathTexGenNV(texCoordSet,genMode,components,coeffs):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint,_cs.GLsizei,_cs.GLsizei,_cs.GLfloat,arrays.GLfloatArray,arrays.GLfloatArray,arrays.GLfloatArray,arrays.GLfloatArray)
def glPointAlongPathNV(path,startSegment,numSegments,distance,x,y,tangentX,tangentY):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLint,arrays.GLfloatArray)
def glProgramPathFragmentInputGenNV(program,location,genMode,components,coeffs):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glStencilFillPathInstancedNV(numPaths,pathNameType,paths,pathBase,fillMode,mask,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glStencilFillPathNV(path,fillMode,mask):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLint,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glStencilStrokePathInstancedNV(numPaths,pathNameType,paths,pathBase,reference,mask,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint)
def glStencilStrokePathNV(path,reference,mask):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glStencilThenCoverFillPathInstancedNV(numPaths,pathNameType,paths,pathBase,fillMode,mask,coverMode,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum)
def glStencilThenCoverFillPathNV(path,fillMode,mask,coverMode):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLuint,_cs.GLint,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glStencilThenCoverStrokePathInstancedNV(numPaths,pathNameType,paths,pathBase,reference,mask,coverMode,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint,_cs.GLenum)
def glStencilThenCoverStrokePathNV(path,reference,mask,coverMode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glTransformPathNV(resultPath,srcPath,transformType,transformValues):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,arrays.GLfloatArray)
def glWeightPathsNV(resultPath,numPaths,paths,weights):pass
