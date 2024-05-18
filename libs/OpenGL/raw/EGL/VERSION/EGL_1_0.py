'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_VERSION_EGL_1_0'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_VERSION_EGL_1_0',error_checker=_errors._error_checker)
EGL_ALPHA_SIZE=_C('EGL_ALPHA_SIZE',0x3021)
EGL_BAD_ACCESS=_C('EGL_BAD_ACCESS',0x3002)
EGL_BAD_ALLOC=_C('EGL_BAD_ALLOC',0x3003)
EGL_BAD_ATTRIBUTE=_C('EGL_BAD_ATTRIBUTE',0x3004)
EGL_BAD_CONFIG=_C('EGL_BAD_CONFIG',0x3005)
EGL_BAD_CONTEXT=_C('EGL_BAD_CONTEXT',0x3006)
EGL_BAD_CURRENT_SURFACE=_C('EGL_BAD_CURRENT_SURFACE',0x3007)
EGL_BAD_DISPLAY=_C('EGL_BAD_DISPLAY',0x3008)
EGL_BAD_MATCH=_C('EGL_BAD_MATCH',0x3009)
EGL_BAD_NATIVE_PIXMAP=_C('EGL_BAD_NATIVE_PIXMAP',0x300A)
EGL_BAD_NATIVE_WINDOW=_C('EGL_BAD_NATIVE_WINDOW',0x300B)
EGL_BAD_PARAMETER=_C('EGL_BAD_PARAMETER',0x300C)
EGL_BAD_SURFACE=_C('EGL_BAD_SURFACE',0x300D)
EGL_BLUE_SIZE=_C('EGL_BLUE_SIZE',0x3022)
EGL_BUFFER_SIZE=_C('EGL_BUFFER_SIZE',0x3020)
EGL_CONFIG_CAVEAT=_C('EGL_CONFIG_CAVEAT',0x3027)
EGL_CONFIG_ID=_C('EGL_CONFIG_ID',0x3028)
EGL_CORE_NATIVE_ENGINE=_C('EGL_CORE_NATIVE_ENGINE',0x305B)
EGL_DEPTH_SIZE=_C('EGL_DEPTH_SIZE',0x3025)
# EGL_DONT_CARE=_C('EGL_DONT_CARE',((EGLint)-1))
EGL_DRAW=_C('EGL_DRAW',0x3059)
EGL_EXTENSIONS=_C('EGL_EXTENSIONS',0x3055)
EGL_FALSE=_C('EGL_FALSE',0)
EGL_GREEN_SIZE=_C('EGL_GREEN_SIZE',0x3023)
EGL_HEIGHT=_C('EGL_HEIGHT',0x3056)
EGL_LARGEST_PBUFFER=_C('EGL_LARGEST_PBUFFER',0x3058)
EGL_LEVEL=_C('EGL_LEVEL',0x3029)
EGL_MAX_PBUFFER_HEIGHT=_C('EGL_MAX_PBUFFER_HEIGHT',0x302A)
EGL_MAX_PBUFFER_PIXELS=_C('EGL_MAX_PBUFFER_PIXELS',0x302B)
EGL_MAX_PBUFFER_WIDTH=_C('EGL_MAX_PBUFFER_WIDTH',0x302C)
EGL_NATIVE_RENDERABLE=_C('EGL_NATIVE_RENDERABLE',0x302D)
EGL_NATIVE_VISUAL_ID=_C('EGL_NATIVE_VISUAL_ID',0x302E)
EGL_NATIVE_VISUAL_TYPE=_C('EGL_NATIVE_VISUAL_TYPE',0x302F)
EGL_NONE=_C('EGL_NONE',0x3038)
EGL_NON_CONFORMANT_CONFIG=_C('EGL_NON_CONFORMANT_CONFIG',0x3051)
EGL_NOT_INITIALIZED=_C('EGL_NOT_INITIALIZED',0x3001)
# EGL_NO_CONTEXT=_C('EGL_NO_CONTEXT',((EGLContext)0))
# EGL_NO_DISPLAY=_C('EGL_NO_DISPLAY',((EGLDisplay)0))
# EGL_NO_SURFACE=_C('EGL_NO_SURFACE',((EGLSurface)0))
EGL_PBUFFER_BIT=_C('EGL_PBUFFER_BIT',0x0001)
EGL_PIXMAP_BIT=_C('EGL_PIXMAP_BIT',0x0002)
EGL_READ=_C('EGL_READ',0x305A)
EGL_RED_SIZE=_C('EGL_RED_SIZE',0x3024)
EGL_SAMPLES=_C('EGL_SAMPLES',0x3031)
EGL_SAMPLE_BUFFERS=_C('EGL_SAMPLE_BUFFERS',0x3032)
EGL_SLOW_CONFIG=_C('EGL_SLOW_CONFIG',0x3050)
EGL_STENCIL_SIZE=_C('EGL_STENCIL_SIZE',0x3026)
EGL_SUCCESS=_C('EGL_SUCCESS',0x3000)
EGL_SURFACE_TYPE=_C('EGL_SURFACE_TYPE',0x3033)
EGL_TRANSPARENT_BLUE_VALUE=_C('EGL_TRANSPARENT_BLUE_VALUE',0x3035)
EGL_TRANSPARENT_GREEN_VALUE=_C('EGL_TRANSPARENT_GREEN_VALUE',0x3036)
EGL_TRANSPARENT_RED_VALUE=_C('EGL_TRANSPARENT_RED_VALUE',0x3037)
EGL_TRANSPARENT_RGB=_C('EGL_TRANSPARENT_RGB',0x3052)
EGL_TRANSPARENT_TYPE=_C('EGL_TRANSPARENT_TYPE',0x3034)
EGL_TRUE=_C('EGL_TRUE',1)
EGL_VENDOR=_C('EGL_VENDOR',0x3053)
EGL_VERSION=_C('EGL_VERSION',0x3054)
EGL_WIDTH=_C('EGL_WIDTH',0x3057)
EGL_WINDOW_BIT=_C('EGL_WINDOW_BIT',0x0004)
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,arrays.GLintArray,arrays.GLvoidpArray,_cs.EGLint,arrays.GLintArray)
def eglChooseConfig(dpy,attrib_list,configs,config_size,num_config):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface,_cs.EGLNativePixmapType)
def eglCopyBuffers(dpy,surface,target):pass
@_f
@_p.types(_cs.EGLContext,_cs.EGLDisplay,_cs.EGLConfig,_cs.EGLContext,arrays.GLintArray)
def eglCreateContext(dpy,config,share_context,attrib_list):pass
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,arrays.GLintArray)
def eglCreatePbufferSurface(dpy,config,attrib_list):pass
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,_cs.EGLNativePixmapType,arrays.GLintArray)
def eglCreatePixmapSurface(dpy,config,pixmap,attrib_list):pass
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,_cs.EGLNativeWindowType,arrays.GLintArray)
def eglCreateWindowSurface(dpy,config,win,attrib_list):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLContext)
def eglDestroyContext(dpy,ctx):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface)
def eglDestroySurface(dpy,surface):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLConfig,_cs.EGLint,arrays.GLintArray)
def eglGetConfigAttrib(dpy,config,attribute,value):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,arrays.GLvoidpArray,_cs.EGLint,arrays.GLintArray)
def eglGetConfigs(dpy,configs,config_size,num_config):pass
@_f
@_p.types(_cs.EGLDisplay,)
def eglGetCurrentDisplay():pass
@_f
@_p.types(_cs.EGLSurface,_cs.EGLint)
def eglGetCurrentSurface(readdraw):pass
@_f
@_p.types(_cs.EGLDisplay,_cs.EGLNativeDisplayType)
def eglGetDisplay(display_id):pass
@_f
@_p.types(_cs.EGLint,)
def eglGetError():pass
@_f
@_p.types(ctypes.c_void_p,arrays.GLbyteArray)
def eglGetProcAddress(procname):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,arrays.GLintArray,arrays.GLintArray)
def eglInitialize(dpy,major,minor):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface,_cs.EGLSurface,_cs.EGLContext)
def eglMakeCurrent(dpy,draw,read,ctx):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLContext,_cs.EGLint,arrays.GLintArray)
def eglQueryContext(dpy,ctx,attribute,value):pass
@_f
@_p.types(ctypes.c_char_p,_cs.EGLDisplay,_cs.EGLint)
def eglQueryString(dpy,name):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface,_cs.EGLint,arrays.GLintArray)
def eglQuerySurface(dpy,surface,attribute,value):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface)
def eglSwapBuffers(dpy,surface):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay)
def eglTerminate(dpy):pass
@_f
@_p.types(_cs.EGLBoolean,)
def eglWaitGL():pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLint)
def eglWaitNative(engine):pass
