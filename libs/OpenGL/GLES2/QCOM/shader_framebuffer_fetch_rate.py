'''OpenGL extension QCOM.shader_framebuffer_fetch_rate

This module customises the behaviour of the 
OpenGL.raw.GLES2.QCOM.shader_framebuffer_fetch_rate to provide a more 
Python-friendly API

Overview (from the spec)
	
	When certain built-ins (e.g. gl_LastFragData, gl_LastFragStencilARM)
	are referenced in the shader, the shader is required to execute at sample-rate
	if the attachments are multisampled.  In some use-cases executing such shaders
	at fragment-rate is actually the preferred behavior.  When this extension is
	enabled, such GLSL shaders will execute at fragment-rate and the built-in
	will return a per-fragment value.  This avoids the significant performance
	penalty that would otherwise be incurred with sample-rate shading.
	
	The following built-ins are affected when the this extension is enabled:
	
	    gl_LastFragData      (from EXT_shader_framebuffer_fetch)
	    gl_LastFragDepthARM  (from ARM_shader_framebuffer_fetch_depth_stencil)
	
	The following built-ins are disallowed when this extension is enabled:
	
	    gl_SampleID
	    gl_SamplePosition
	    interpolateAtSample()

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/QCOM/shader_framebuffer_fetch_rate.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.QCOM.shader_framebuffer_fetch_rate import *
from OpenGL.raw.GLES2.QCOM.shader_framebuffer_fetch_rate import _EXTENSION_NAME

def glInitShaderFramebufferFetchRateQCOM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION