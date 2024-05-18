'''OpenGL extension AMD.performance_monitor

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.performance_monitor to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables the capture and reporting of performance monitors.
	Performance monitors contain groups of counters which hold arbitrary counted 
	data.  Typically, the counters hold information on performance-related
	counters in the underlying hardware.  The extension is general enough to
	allow the implementation to choose which counters to expose and pick the
	data type and range of the counters.  The extension also allows counting to 
	start and end on arbitrary boundaries during rendering.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/performance_monitor.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.performance_monitor import *
from OpenGL.raw.GL.AMD.performance_monitor import _EXTENSION_NAME

def glInitPerformanceMonitorAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGetPerfMonitorGroupsAMD=wrapper.wrapper(glGetPerfMonitorGroupsAMD).setOutput(
    'groups',size=lambda x:(x,),pnameArg='groupsSize',orPassIn=True
).setOutput(
    'numGroups',size=(1,),orPassIn=True
)
glGetPerfMonitorCountersAMD=wrapper.wrapper(glGetPerfMonitorCountersAMD).setOutput(
    'counters',size=lambda x:(x,),pnameArg='counterSize',orPassIn=True
).setOutput(
    'maxActiveCounters',size=(1,),orPassIn=True
).setOutput(
    'numCounters',size=(1,),orPassIn=True
)
glGetPerfMonitorGroupStringAMD=wrapper.wrapper(glGetPerfMonitorGroupStringAMD).setOutput(
    'groupString',size=lambda x:(x,),pnameArg='bufSize',orPassIn=True
).setOutput(
    'length',size=(1,),orPassIn=True
)
glGetPerfMonitorCounterStringAMD=wrapper.wrapper(glGetPerfMonitorCounterStringAMD).setOutput(
    'counterString',size=lambda x:(x,),pnameArg='bufSize',orPassIn=True
).setOutput(
    'length',size=(1,),orPassIn=True
)
glGetPerfMonitorCounterInfoAMD=wrapper.wrapper(glGetPerfMonitorCounterInfoAMD).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGenPerfMonitorsAMD=wrapper.wrapper(glGenPerfMonitorsAMD).setOutput(
    'monitors',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glDeletePerfMonitorsAMD=wrapper.wrapper(glDeletePerfMonitorsAMD).setOutput(
    'monitors',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glSelectPerfMonitorCountersAMD=wrapper.wrapper(glSelectPerfMonitorCountersAMD).setOutput(
    'counterList',size=lambda x:(x,),pnameArg='numCounters',orPassIn=True
)
glGetPerfMonitorCounterDataAMD=wrapper.wrapper(glGetPerfMonitorCounterDataAMD).setOutput(
    'bytesWritten',size=(1,),orPassIn=True
).setOutput(
    'data',size=lambda x:(x,),pnameArg='dataSize',orPassIn=True
)
### END AUTOGENERATED SECTION