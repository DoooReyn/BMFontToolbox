# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide6.QtOpenGL, except for defaults which are replaced by "...".
"""

# Module PySide6.QtOpenGL
import PySide6
try:
    import typing
except ImportError:
    from PySide6.support.signature import typing
from PySide6.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken6 as Shiboken
Shiboken.Object = Object

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtOpenGL


class QAbstractOpenGLFunctions(Shiboken.Object):

    def __init__(self) -> None: ...

    def initializeOpenGLFunctions(self) -> bool: ...
    def isInitialized(self) -> bool: ...
    def owningContext(self) -> PySide6.QtGui.QOpenGLContext: ...
    def setOwningContext(self, context:PySide6.QtGui.QOpenGLContext) -> None: ...


class QOpenGLBuffer(Shiboken.Object):
    ReadOnly                 : QOpenGLBuffer.Access = ... # 0x88b8
    WriteOnly                : QOpenGLBuffer.Access = ... # 0x88b9
    ReadWrite                : QOpenGLBuffer.Access = ... # 0x88ba
    RangeRead                : QOpenGLBuffer.RangeAccessFlag = ... # 0x1
    RangeWrite               : QOpenGLBuffer.RangeAccessFlag = ... # 0x2
    RangeInvalidate          : QOpenGLBuffer.RangeAccessFlag = ... # 0x4
    RangeInvalidateBuffer    : QOpenGLBuffer.RangeAccessFlag = ... # 0x8
    RangeFlushExplicit       : QOpenGLBuffer.RangeAccessFlag = ... # 0x10
    RangeUnsynchronized      : QOpenGLBuffer.RangeAccessFlag = ... # 0x20
    VertexBuffer             : QOpenGLBuffer.Type = ... # 0x8892
    IndexBuffer              : QOpenGLBuffer.Type = ... # 0x8893
    PixelPackBuffer          : QOpenGLBuffer.Type = ... # 0x88eb
    PixelUnpackBuffer        : QOpenGLBuffer.Type = ... # 0x88ec
    StreamDraw               : QOpenGLBuffer.UsagePattern = ... # 0x88e0
    StreamRead               : QOpenGLBuffer.UsagePattern = ... # 0x88e1
    StreamCopy               : QOpenGLBuffer.UsagePattern = ... # 0x88e2
    StaticDraw               : QOpenGLBuffer.UsagePattern = ... # 0x88e4
    StaticRead               : QOpenGLBuffer.UsagePattern = ... # 0x88e5
    StaticCopy               : QOpenGLBuffer.UsagePattern = ... # 0x88e6
    DynamicDraw              : QOpenGLBuffer.UsagePattern = ... # 0x88e8
    DynamicRead              : QOpenGLBuffer.UsagePattern = ... # 0x88e9
    DynamicCopy              : QOpenGLBuffer.UsagePattern = ... # 0x88ea

    class Access(Shiboken.Enum):
        ReadOnly                 : QOpenGLBuffer.Access = ... # 0x88b8
        WriteOnly                : QOpenGLBuffer.Access = ... # 0x88b9
        ReadWrite                : QOpenGLBuffer.Access = ... # 0x88ba

    class RangeAccessFlag(Shiboken.Enum):
        RangeRead                : QOpenGLBuffer.RangeAccessFlag = ... # 0x1
        RangeWrite               : QOpenGLBuffer.RangeAccessFlag = ... # 0x2
        RangeInvalidate          : QOpenGLBuffer.RangeAccessFlag = ... # 0x4
        RangeInvalidateBuffer    : QOpenGLBuffer.RangeAccessFlag = ... # 0x8
        RangeFlushExplicit       : QOpenGLBuffer.RangeAccessFlag = ... # 0x10
        RangeUnsynchronized      : QOpenGLBuffer.RangeAccessFlag = ... # 0x20

    class RangeAccessFlags(object): ...

    class Type(Shiboken.Enum):
        VertexBuffer             : QOpenGLBuffer.Type = ... # 0x8892
        IndexBuffer              : QOpenGLBuffer.Type = ... # 0x8893
        PixelPackBuffer          : QOpenGLBuffer.Type = ... # 0x88eb
        PixelUnpackBuffer        : QOpenGLBuffer.Type = ... # 0x88ec

    class UsagePattern(Shiboken.Enum):
        StreamDraw               : QOpenGLBuffer.UsagePattern = ... # 0x88e0
        StreamRead               : QOpenGLBuffer.UsagePattern = ... # 0x88e1
        StreamCopy               : QOpenGLBuffer.UsagePattern = ... # 0x88e2
        StaticDraw               : QOpenGLBuffer.UsagePattern = ... # 0x88e4
        StaticRead               : QOpenGLBuffer.UsagePattern = ... # 0x88e5
        StaticCopy               : QOpenGLBuffer.UsagePattern = ... # 0x88e6
        DynamicDraw              : QOpenGLBuffer.UsagePattern = ... # 0x88e8
        DynamicRead              : QOpenGLBuffer.UsagePattern = ... # 0x88e9
        DynamicCopy              : QOpenGLBuffer.UsagePattern = ... # 0x88ea

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other:PySide6.QtOpenGL.QOpenGLBuffer) -> None: ...
    @typing.overload
    def __init__(self, type:PySide6.QtOpenGL.QOpenGLBuffer.Type) -> None: ...

    @typing.overload
    def allocate(self, count:int) -> None: ...
    @typing.overload
    def allocate(self, data:int, count:int) -> None: ...
    def bind(self) -> bool: ...
    def bufferId(self) -> int: ...
    def create(self) -> bool: ...
    def destroy(self) -> None: ...
    def isCreated(self) -> bool: ...
    def map(self, access:PySide6.QtOpenGL.QOpenGLBuffer.Access) -> int: ...
    def mapRange(self, offset:int, count:int, access:PySide6.QtOpenGL.QOpenGLBuffer.RangeAccessFlags) -> int: ...
    def read(self, offset:int, data:int, count:int) -> bool: ...
    @typing.overload
    def release(self) -> None: ...
    @typing.overload
    @staticmethod
    def release(type:PySide6.QtOpenGL.QOpenGLBuffer.Type) -> None: ...
    def setUsagePattern(self, value:PySide6.QtOpenGL.QOpenGLBuffer.UsagePattern) -> None: ...
    def size(self) -> int: ...
    def type(self) -> PySide6.QtOpenGL.QOpenGLBuffer.Type: ...
    def unmap(self) -> bool: ...
    def usagePattern(self) -> PySide6.QtOpenGL.QOpenGLBuffer.UsagePattern: ...
    def write(self, offset:int, data:int, count:int) -> None: ...


class QOpenGLDebugLogger(PySide6.QtCore.QObject):
    AsynchronousLogging      : QOpenGLDebugLogger.LoggingMode = ... # 0x0
    SynchronousLogging       : QOpenGLDebugLogger.LoggingMode = ... # 0x1

    class LoggingMode(Shiboken.Enum):
        AsynchronousLogging      : QOpenGLDebugLogger.LoggingMode = ... # 0x0
        SynchronousLogging       : QOpenGLDebugLogger.LoggingMode = ... # 0x1

    def __init__(self, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    @typing.overload
    def disableMessages(self, ids:typing.Sequence, sources:PySide6.QtOpenGL.QOpenGLDebugMessage.Sources=..., types:PySide6.QtOpenGL.QOpenGLDebugMessage.Types=...) -> None: ...
    @typing.overload
    def disableMessages(self, sources:PySide6.QtOpenGL.QOpenGLDebugMessage.Sources=..., types:PySide6.QtOpenGL.QOpenGLDebugMessage.Types=..., severities:PySide6.QtOpenGL.QOpenGLDebugMessage.Severities=...) -> None: ...
    @typing.overload
    def enableMessages(self, ids:typing.Sequence, sources:PySide6.QtOpenGL.QOpenGLDebugMessage.Sources=..., types:PySide6.QtOpenGL.QOpenGLDebugMessage.Types=...) -> None: ...
    @typing.overload
    def enableMessages(self, sources:PySide6.QtOpenGL.QOpenGLDebugMessage.Sources=..., types:PySide6.QtOpenGL.QOpenGLDebugMessage.Types=..., severities:PySide6.QtOpenGL.QOpenGLDebugMessage.Severities=...) -> None: ...
    def initialize(self) -> bool: ...
    def isLogging(self) -> bool: ...
    def logMessage(self, debugMessage:PySide6.QtOpenGL.QOpenGLDebugMessage) -> None: ...
    def loggedMessages(self) -> typing.List: ...
    def loggingMode(self) -> PySide6.QtOpenGL.QOpenGLDebugLogger.LoggingMode: ...
    def maximumMessageLength(self) -> int: ...
    def popGroup(self) -> None: ...
    def pushGroup(self, name:str, id:int=..., source:PySide6.QtOpenGL.QOpenGLDebugMessage.Source=...) -> None: ...
    def startLogging(self, loggingMode:PySide6.QtOpenGL.QOpenGLDebugLogger.LoggingMode=...) -> None: ...
    def stopLogging(self) -> None: ...


class QOpenGLDebugMessage(Shiboken.Object):
    AnySeverity              : QOpenGLDebugMessage.Severity = ... # -0x1
    InvalidSeverity          : QOpenGLDebugMessage.Severity = ... # 0x0
    HighSeverity             : QOpenGLDebugMessage.Severity = ... # 0x1
    MediumSeverity           : QOpenGLDebugMessage.Severity = ... # 0x2
    LowSeverity              : QOpenGLDebugMessage.Severity = ... # 0x4
    LastSeverity             : QOpenGLDebugMessage.Severity = ... # 0x8
    NotificationSeverity     : QOpenGLDebugMessage.Severity = ... # 0x8
    AnySource                : QOpenGLDebugMessage.Source = ... # -0x1
    InvalidSource            : QOpenGLDebugMessage.Source = ... # 0x0
    APISource                : QOpenGLDebugMessage.Source = ... # 0x1
    WindowSystemSource       : QOpenGLDebugMessage.Source = ... # 0x2
    ShaderCompilerSource     : QOpenGLDebugMessage.Source = ... # 0x4
    ThirdPartySource         : QOpenGLDebugMessage.Source = ... # 0x8
    ApplicationSource        : QOpenGLDebugMessage.Source = ... # 0x10
    LastSource               : QOpenGLDebugMessage.Source = ... # 0x20
    OtherSource              : QOpenGLDebugMessage.Source = ... # 0x20
    AnyType                  : QOpenGLDebugMessage.Type = ... # -0x1
    InvalidType              : QOpenGLDebugMessage.Type = ... # 0x0
    ErrorType                : QOpenGLDebugMessage.Type = ... # 0x1
    DeprecatedBehaviorType   : QOpenGLDebugMessage.Type = ... # 0x2
    UndefinedBehaviorType    : QOpenGLDebugMessage.Type = ... # 0x4
    PortabilityType          : QOpenGLDebugMessage.Type = ... # 0x8
    PerformanceType          : QOpenGLDebugMessage.Type = ... # 0x10
    OtherType                : QOpenGLDebugMessage.Type = ... # 0x20
    MarkerType               : QOpenGLDebugMessage.Type = ... # 0x40
    GroupPushType            : QOpenGLDebugMessage.Type = ... # 0x80
    GroupPopType             : QOpenGLDebugMessage.Type = ... # 0x100
    LastType                 : QOpenGLDebugMessage.Type = ... # 0x100

    class Severities(object): ...

    class Severity(Shiboken.Enum):
        AnySeverity              : QOpenGLDebugMessage.Severity = ... # -0x1
        InvalidSeverity          : QOpenGLDebugMessage.Severity = ... # 0x0
        HighSeverity             : QOpenGLDebugMessage.Severity = ... # 0x1
        MediumSeverity           : QOpenGLDebugMessage.Severity = ... # 0x2
        LowSeverity              : QOpenGLDebugMessage.Severity = ... # 0x4
        LastSeverity             : QOpenGLDebugMessage.Severity = ... # 0x8
        NotificationSeverity     : QOpenGLDebugMessage.Severity = ... # 0x8

    class Source(Shiboken.Enum):
        AnySource                : QOpenGLDebugMessage.Source = ... # -0x1
        InvalidSource            : QOpenGLDebugMessage.Source = ... # 0x0
        APISource                : QOpenGLDebugMessage.Source = ... # 0x1
        WindowSystemSource       : QOpenGLDebugMessage.Source = ... # 0x2
        ShaderCompilerSource     : QOpenGLDebugMessage.Source = ... # 0x4
        ThirdPartySource         : QOpenGLDebugMessage.Source = ... # 0x8
        ApplicationSource        : QOpenGLDebugMessage.Source = ... # 0x10
        LastSource               : QOpenGLDebugMessage.Source = ... # 0x20
        OtherSource              : QOpenGLDebugMessage.Source = ... # 0x20

    class Sources(object): ...

    class Type(Shiboken.Enum):
        AnyType                  : QOpenGLDebugMessage.Type = ... # -0x1
        InvalidType              : QOpenGLDebugMessage.Type = ... # 0x0
        ErrorType                : QOpenGLDebugMessage.Type = ... # 0x1
        DeprecatedBehaviorType   : QOpenGLDebugMessage.Type = ... # 0x2
        UndefinedBehaviorType    : QOpenGLDebugMessage.Type = ... # 0x4
        PortabilityType          : QOpenGLDebugMessage.Type = ... # 0x8
        PerformanceType          : QOpenGLDebugMessage.Type = ... # 0x10
        OtherType                : QOpenGLDebugMessage.Type = ... # 0x20
        MarkerType               : QOpenGLDebugMessage.Type = ... # 0x40
        GroupPushType            : QOpenGLDebugMessage.Type = ... # 0x80
        GroupPopType             : QOpenGLDebugMessage.Type = ... # 0x100
        LastType                 : QOpenGLDebugMessage.Type = ... # 0x100

    class Types(object): ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, debugMessage:PySide6.QtOpenGL.QOpenGLDebugMessage) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def createApplicationMessage(text:str, id:int=..., severity:PySide6.QtOpenGL.QOpenGLDebugMessage.Severity=..., type:PySide6.QtOpenGL.QOpenGLDebugMessage.Type=...) -> PySide6.QtOpenGL.QOpenGLDebugMessage: ...
    @staticmethod
    def createThirdPartyMessage(text:str, id:int=..., severity:PySide6.QtOpenGL.QOpenGLDebugMessage.Severity=..., type:PySide6.QtOpenGL.QOpenGLDebugMessage.Type=...) -> PySide6.QtOpenGL.QOpenGLDebugMessage: ...
    def id(self) -> int: ...
    def message(self) -> str: ...
    def severity(self) -> PySide6.QtOpenGL.QOpenGLDebugMessage.Severity: ...
    def source(self) -> PySide6.QtOpenGL.QOpenGLDebugMessage.Source: ...
    def swap(self, other:PySide6.QtOpenGL.QOpenGLDebugMessage) -> None: ...
    def type(self) -> PySide6.QtOpenGL.QOpenGLDebugMessage.Type: ...


class QOpenGLFramebufferObject(Shiboken.Object):
    NoAttachment             : QOpenGLFramebufferObject.Attachment = ... # 0x0
    CombinedDepthStencil     : QOpenGLFramebufferObject.Attachment = ... # 0x1
    Depth                    : QOpenGLFramebufferObject.Attachment = ... # 0x2
    DontRestoreFramebufferBinding: QOpenGLFramebufferObject.FramebufferRestorePolicy = ... # 0x0
    RestoreFramebufferBindingToDefault: QOpenGLFramebufferObject.FramebufferRestorePolicy = ... # 0x1
    RestoreFrameBufferBinding: QOpenGLFramebufferObject.FramebufferRestorePolicy = ... # 0x2

    class Attachment(Shiboken.Enum):
        NoAttachment             : QOpenGLFramebufferObject.Attachment = ... # 0x0
        CombinedDepthStencil     : QOpenGLFramebufferObject.Attachment = ... # 0x1
        Depth                    : QOpenGLFramebufferObject.Attachment = ... # 0x2

    class FramebufferRestorePolicy(Shiboken.Enum):
        DontRestoreFramebufferBinding: QOpenGLFramebufferObject.FramebufferRestorePolicy = ... # 0x0
        RestoreFramebufferBindingToDefault: QOpenGLFramebufferObject.FramebufferRestorePolicy = ... # 0x1
        RestoreFrameBufferBinding: QOpenGLFramebufferObject.FramebufferRestorePolicy = ... # 0x2

    @typing.overload
    def __init__(self, size:PySide6.QtCore.QSize, attachment:PySide6.QtOpenGL.QOpenGLFramebufferObject.Attachment, target:int=..., internalFormat:int=...) -> None: ...
    @typing.overload
    def __init__(self, size:PySide6.QtCore.QSize, format:PySide6.QtOpenGL.QOpenGLFramebufferObjectFormat) -> None: ...
    @typing.overload
    def __init__(self, size:PySide6.QtCore.QSize, target:int=...) -> None: ...
    @typing.overload
    def __init__(self, width:int, height:int, attachment:PySide6.QtOpenGL.QOpenGLFramebufferObject.Attachment, target:int=..., internalFormat:int=...) -> None: ...
    @typing.overload
    def __init__(self, width:int, height:int, format:PySide6.QtOpenGL.QOpenGLFramebufferObjectFormat) -> None: ...
    @typing.overload
    def __init__(self, width:int, height:int, target:int=...) -> None: ...

    @typing.overload
    def addColorAttachment(self, size:PySide6.QtCore.QSize, internalFormat:int=...) -> None: ...
    @typing.overload
    def addColorAttachment(self, width:int, height:int, internalFormat:int=...) -> None: ...
    def attachment(self) -> PySide6.QtOpenGL.QOpenGLFramebufferObject.Attachment: ...
    def bind(self) -> bool: ...
    @staticmethod
    def bindDefault() -> bool: ...
    @typing.overload
    @staticmethod
    def blitFramebuffer(target:PySide6.QtOpenGL.QOpenGLFramebufferObject, source:PySide6.QtOpenGL.QOpenGLFramebufferObject, buffers:int=..., filter:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def blitFramebuffer(target:PySide6.QtOpenGL.QOpenGLFramebufferObject, targetRect:PySide6.QtCore.QRect, source:PySide6.QtOpenGL.QOpenGLFramebufferObject, sourceRect:PySide6.QtCore.QRect, buffers:int, filter:int, readColorAttachmentIndex:int, drawColorAttachmentIndex:int) -> None: ...
    @typing.overload
    @staticmethod
    def blitFramebuffer(target:PySide6.QtOpenGL.QOpenGLFramebufferObject, targetRect:PySide6.QtCore.QRect, source:PySide6.QtOpenGL.QOpenGLFramebufferObject, sourceRect:PySide6.QtCore.QRect, buffers:int, filter:int, readColorAttachmentIndex:int, drawColorAttachmentIndex:int, restorePolicy:PySide6.QtOpenGL.QOpenGLFramebufferObject.FramebufferRestorePolicy) -> None: ...
    @typing.overload
    @staticmethod
    def blitFramebuffer(target:PySide6.QtOpenGL.QOpenGLFramebufferObject, targetRect:PySide6.QtCore.QRect, source:PySide6.QtOpenGL.QOpenGLFramebufferObject, sourceRect:PySide6.QtCore.QRect, buffers:int=..., filter:int=...) -> None: ...
    def format(self) -> PySide6.QtOpenGL.QOpenGLFramebufferObjectFormat: ...
    def handle(self) -> int: ...
    @staticmethod
    def hasOpenGLFramebufferBlit() -> bool: ...
    @staticmethod
    def hasOpenGLFramebufferObjects() -> bool: ...
    def height(self) -> int: ...
    def isBound(self) -> bool: ...
    def isValid(self) -> bool: ...
    def release(self) -> bool: ...
    def setAttachment(self, attachment:PySide6.QtOpenGL.QOpenGLFramebufferObject.Attachment) -> None: ...
    def size(self) -> PySide6.QtCore.QSize: ...
    def sizes(self) -> typing.List: ...
    @typing.overload
    def takeTexture(self) -> int: ...
    @typing.overload
    def takeTexture(self, colorAttachmentIndex:int) -> int: ...
    def texture(self) -> int: ...
    def textures(self) -> typing.List: ...
    @typing.overload
    def toImage(self, flipped:bool, colorAttachmentIndex:int) -> PySide6.QtGui.QImage: ...
    @typing.overload
    def toImage(self, flipped:bool=...) -> PySide6.QtGui.QImage: ...
    def width(self) -> int: ...


class QOpenGLFramebufferObjectFormat(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other:PySide6.QtOpenGL.QOpenGLFramebufferObjectFormat) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def attachment(self) -> PySide6.QtOpenGL.QOpenGLFramebufferObject.Attachment: ...
    def internalTextureFormat(self) -> int: ...
    def mipmap(self) -> bool: ...
    def samples(self) -> int: ...
    def setAttachment(self, attachment:PySide6.QtOpenGL.QOpenGLFramebufferObject.Attachment) -> None: ...
    def setInternalTextureFormat(self, internalTextureFormat:int) -> None: ...
    def setMipmap(self, enabled:bool) -> None: ...
    def setSamples(self, samples:int) -> None: ...
    def setTextureTarget(self, target:int) -> None: ...
    def textureTarget(self) -> int: ...


class QOpenGLPixelTransferOptions(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg__1:PySide6.QtOpenGL.QOpenGLPixelTransferOptions) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def alignment(self) -> int: ...
    def imageHeight(self) -> int: ...
    def isLeastSignificantBitFirst(self) -> bool: ...
    def isSwapBytesEnabled(self) -> bool: ...
    def rowLength(self) -> int: ...
    def setAlignment(self, alignment:int) -> None: ...
    def setImageHeight(self, imageHeight:int) -> None: ...
    def setLeastSignificantByteFirst(self, lsbFirst:bool) -> None: ...
    def setRowLength(self, rowLength:int) -> None: ...
    def setSkipImages(self, skipImages:int) -> None: ...
    def setSkipPixels(self, skipPixels:int) -> None: ...
    def setSkipRows(self, skipRows:int) -> None: ...
    def setSwapBytesEnabled(self, swapBytes:bool) -> None: ...
    def skipImages(self) -> int: ...
    def skipPixels(self) -> int: ...
    def skipRows(self) -> int: ...
    def swap(self, other:PySide6.QtOpenGL.QOpenGLPixelTransferOptions) -> None: ...


class QOpenGLShader(PySide6.QtCore.QObject):
    Vertex                   : QOpenGLShader.ShaderTypeBit = ... # 0x1
    Fragment                 : QOpenGLShader.ShaderTypeBit = ... # 0x2
    Geometry                 : QOpenGLShader.ShaderTypeBit = ... # 0x4
    TessellationControl      : QOpenGLShader.ShaderTypeBit = ... # 0x8
    TessellationEvaluation   : QOpenGLShader.ShaderTypeBit = ... # 0x10
    Compute                  : QOpenGLShader.ShaderTypeBit = ... # 0x20

    class ShaderType(object): ...

    class ShaderTypeBit(Shiboken.Enum):
        Vertex                   : QOpenGLShader.ShaderTypeBit = ... # 0x1
        Fragment                 : QOpenGLShader.ShaderTypeBit = ... # 0x2
        Geometry                 : QOpenGLShader.ShaderTypeBit = ... # 0x4
        TessellationControl      : QOpenGLShader.ShaderTypeBit = ... # 0x8
        TessellationEvaluation   : QOpenGLShader.ShaderTypeBit = ... # 0x10
        Compute                  : QOpenGLShader.ShaderTypeBit = ... # 0x20

    def __init__(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    @typing.overload
    def compileSourceCode(self, source:PySide6.QtCore.QByteArray) -> bool: ...
    @typing.overload
    def compileSourceCode(self, source:str) -> bool: ...
    @typing.overload
    def compileSourceCode(self, source:bytes) -> bool: ...
    def compileSourceFile(self, fileName:str) -> bool: ...
    @staticmethod
    def hasOpenGLShaders(type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, context:typing.Optional[PySide6.QtGui.QOpenGLContext]=...) -> bool: ...
    def isCompiled(self) -> bool: ...
    def log(self) -> str: ...
    def shaderId(self) -> int: ...
    def shaderType(self) -> PySide6.QtOpenGL.QOpenGLShader.ShaderType: ...
    def sourceCode(self) -> PySide6.QtCore.QByteArray: ...


class QOpenGLShaderProgram(PySide6.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    @typing.overload
    def addCacheableShaderFromSourceCode(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, source:PySide6.QtCore.QByteArray) -> bool: ...
    @typing.overload
    def addCacheableShaderFromSourceCode(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, source:str) -> bool: ...
    @typing.overload
    def addCacheableShaderFromSourceCode(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, source:bytes) -> bool: ...
    def addCacheableShaderFromSourceFile(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, fileName:str) -> bool: ...
    def addShader(self, shader:PySide6.QtOpenGL.QOpenGLShader) -> bool: ...
    @typing.overload
    def addShaderFromSourceCode(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, source:PySide6.QtCore.QByteArray) -> bool: ...
    @typing.overload
    def addShaderFromSourceCode(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, source:str) -> bool: ...
    @typing.overload
    def addShaderFromSourceCode(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, source:bytes) -> bool: ...
    def addShaderFromSourceFile(self, type:PySide6.QtOpenGL.QOpenGLShader.ShaderType, fileName:str) -> bool: ...
    @typing.overload
    def attributeLocation(self, name:PySide6.QtCore.QByteArray) -> int: ...
    @typing.overload
    def attributeLocation(self, name:str) -> int: ...
    @typing.overload
    def attributeLocation(self, name:bytes) -> int: ...
    def bind(self) -> bool: ...
    @typing.overload
    def bindAttributeLocation(self, name:PySide6.QtCore.QByteArray, location:int) -> None: ...
    @typing.overload
    def bindAttributeLocation(self, name:str, location:int) -> None: ...
    @typing.overload
    def bindAttributeLocation(self, name:bytes, location:int) -> None: ...
    def create(self) -> bool: ...
    def defaultInnerTessellationLevels(self) -> typing.List: ...
    def defaultOuterTessellationLevels(self) -> typing.List: ...
    @typing.overload
    def disableAttributeArray(self, location:int) -> None: ...
    @typing.overload
    def disableAttributeArray(self, name:bytes) -> None: ...
    @typing.overload
    def enableAttributeArray(self, location:int) -> None: ...
    @typing.overload
    def enableAttributeArray(self, name:bytes) -> None: ...
    @staticmethod
    def hasOpenGLShaderPrograms(context:typing.Optional[PySide6.QtGui.QOpenGLContext]=...) -> bool: ...
    def isLinked(self) -> bool: ...
    def link(self) -> bool: ...
    def log(self) -> str: ...
    def maxGeometryOutputVertices(self) -> int: ...
    def patchVertexCount(self) -> int: ...
    def programId(self) -> int: ...
    def release(self) -> None: ...
    def removeAllShaders(self) -> None: ...
    def removeShader(self, shader:PySide6.QtOpenGL.QOpenGLShader) -> None: ...
    @typing.overload
    def setAttributeArray(self, location:int, type:int, values:int, tupleSize:int, stride:int=...) -> None: ...
    @typing.overload
    def setAttributeArray(self, location:int, values:typing.Sequence, tupleSize:int, stride:int=...) -> None: ...
    @typing.overload
    def setAttributeArray(self, name:bytes, type:int, values:int, tupleSize:int, stride:int=...) -> None: ...
    @typing.overload
    def setAttributeArray(self, name:bytes, values:typing.Sequence, tupleSize:int, stride:int=...) -> None: ...
    @typing.overload
    def setAttributeBuffer(self, location:int, type:int, offset:int, tupleSize:int, stride:int=...) -> None: ...
    @typing.overload
    def setAttributeBuffer(self, name:bytes, type:int, offset:int, tupleSize:int, stride:int=...) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, value:PySide6.QtGui.QColor) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, value:PySide6.QtGui.QVector2D) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, value:PySide6.QtGui.QVector3D) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, value:PySide6.QtGui.QVector4D) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, value:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, values:typing.Sequence, columns:int, rows:int) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, x:float, y:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, x:float, y:float, z:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location:int, x:float, y:float, z:float, w:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, value:PySide6.QtGui.QColor) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, value:PySide6.QtGui.QVector2D) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, value:PySide6.QtGui.QVector3D) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, value:PySide6.QtGui.QVector4D) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, value:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, values:typing.Sequence, columns:int, rows:int) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, x:float, y:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, x:float, y:float, z:float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name:bytes, x:float, y:float, z:float, w:float) -> None: ...
    def setDefaultInnerTessellationLevels(self, levels:typing.Sequence) -> None: ...
    def setDefaultOuterTessellationLevels(self, levels:typing.Sequence) -> None: ...
    def setPatchVertexCount(self, count:int) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, color:PySide6.QtGui.QColor) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, point:PySide6.QtCore.QPoint) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, point:PySide6.QtCore.QPointF) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, size:PySide6.QtCore.QSize) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, size:PySide6.QtCore.QSizeF) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix2x2) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix2x3) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix2x4) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix3x2) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix3x3) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix3x4) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix4x2) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix4x3) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QMatrix4x4) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QTransform) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QVector2D) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QVector3D) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:PySide6.QtGui.QVector4D) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:float) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:typing.Tuple) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:typing.Tuple) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:typing.Tuple) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:int) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, value:int) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, x:float, y:float) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, x:float, y:float, z:float) -> None: ...
    @typing.overload
    def setUniformValue(self, location:int, x:float, y:float, z:float, w:float) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, color:PySide6.QtGui.QColor) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, point:PySide6.QtCore.QPoint) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, point:PySide6.QtCore.QPointF) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, size:PySide6.QtCore.QSize) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, size:PySide6.QtCore.QSizeF) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix2x2) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix2x3) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix2x4) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix3x2) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix3x3) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix3x4) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix4x2) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix4x3) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QMatrix4x4) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QTransform) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QVector2D) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QVector3D) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:PySide6.QtGui.QVector4D) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:typing.Tuple) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:typing.Tuple) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, value:typing.Tuple) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, x:float, y:float) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, x:float, y:float, z:float) -> None: ...
    @typing.overload
    def setUniformValue(self, name:bytes, x:float, y:float, z:float, w:float) -> None: ...
    @typing.overload
    def setUniformValue1f(self, arg__1:bytes, arg__2:float) -> None: ...
    @typing.overload
    def setUniformValue1f(self, arg__1:int, arg__2:float) -> None: ...
    @typing.overload
    def setUniformValue1i(self, arg__1:bytes, arg__2:int) -> None: ...
    @typing.overload
    def setUniformValue1i(self, arg__1:int, arg__2:int) -> None: ...
    @typing.overload
    def setUniformValueArray(self, location:int, values:typing.Sequence, count:int, tupleSize:int) -> None: ...
    @typing.overload
    def setUniformValueArray(self, location:int, values:typing.Sequence, count:int) -> None: ...
    @typing.overload
    def setUniformValueArray(self, location:int, values:typing.Sequence, count:int) -> None: ...
    @typing.overload
    def setUniformValueArray(self, name:bytes, values:typing.Sequence, count:int, tupleSize:int) -> None: ...
    @typing.overload
    def setUniformValueArray(self, name:bytes, values:typing.Sequence, count:int) -> None: ...
    @typing.overload
    def setUniformValueArray(self, name:bytes, values:typing.Sequence, count:int) -> None: ...
    def shaders(self) -> typing.List: ...
    @typing.overload
    def uniformLocation(self, name:PySide6.QtCore.QByteArray) -> int: ...
    @typing.overload
    def uniformLocation(self, name:str) -> int: ...
    @typing.overload
    def uniformLocation(self, name:bytes) -> int: ...


class QOpenGLTexture(Shiboken.Object):
    BindingTarget1D          : QOpenGLTexture.BindingTarget = ... # 0x8068
    BindingTarget2D          : QOpenGLTexture.BindingTarget = ... # 0x8069
    BindingTarget3D          : QOpenGLTexture.BindingTarget = ... # 0x806a
    BindingTargetRectangle   : QOpenGLTexture.BindingTarget = ... # 0x84f6
    BindingTargetCubeMap     : QOpenGLTexture.BindingTarget = ... # 0x8514
    BindingTarget1DArray     : QOpenGLTexture.BindingTarget = ... # 0x8c1c
    BindingTarget2DArray     : QOpenGLTexture.BindingTarget = ... # 0x8c1d
    BindingTargetBuffer      : QOpenGLTexture.BindingTarget = ... # 0x8c2c
    BindingTargetCubeMapArray: QOpenGLTexture.BindingTarget = ... # 0x900a
    BindingTarget2DMultisample: QOpenGLTexture.BindingTarget = ... # 0x9104
    BindingTarget2DMultisampleArray: QOpenGLTexture.BindingTarget = ... # 0x9105
    CompareNever             : QOpenGLTexture.ComparisonFunction = ... # 0x200
    CompareLess              : QOpenGLTexture.ComparisonFunction = ... # 0x201
    CompareEqual             : QOpenGLTexture.ComparisonFunction = ... # 0x202
    CompareLessEqual         : QOpenGLTexture.ComparisonFunction = ... # 0x203
    CompareGreater           : QOpenGLTexture.ComparisonFunction = ... # 0x204
    CommpareNotEqual         : QOpenGLTexture.ComparisonFunction = ... # 0x205
    CompareGreaterEqual      : QOpenGLTexture.ComparisonFunction = ... # 0x206
    CompareAlways            : QOpenGLTexture.ComparisonFunction = ... # 0x207
    CompareNone              : QOpenGLTexture.ComparisonMode = ... # 0x0
    CompareRefToTexture      : QOpenGLTexture.ComparisonMode = ... # 0x884e
    DirectionS               : QOpenGLTexture.CoordinateDirection = ... # 0x2802
    DirectionT               : QOpenGLTexture.CoordinateDirection = ... # 0x2803
    DirectionR               : QOpenGLTexture.CoordinateDirection = ... # 0x8072
    CubeMapPositiveX         : QOpenGLTexture.CubeMapFace = ... # 0x8515
    CubeMapNegativeX         : QOpenGLTexture.CubeMapFace = ... # 0x8516
    CubeMapPositiveY         : QOpenGLTexture.CubeMapFace = ... # 0x8517
    CubeMapNegativeY         : QOpenGLTexture.CubeMapFace = ... # 0x8518
    CubeMapPositiveZ         : QOpenGLTexture.CubeMapFace = ... # 0x8519
    CubeMapNegativeZ         : QOpenGLTexture.CubeMapFace = ... # 0x851a
    StencilMode              : QOpenGLTexture.DepthStencilMode = ... # 0x1901
    DepthMode                : QOpenGLTexture.DepthStencilMode = ... # 0x1902
    ImmutableStorage         : QOpenGLTexture.Feature = ... # 0x1
    ImmutableMultisampleStorage: QOpenGLTexture.Feature = ... # 0x2
    TextureRectangle         : QOpenGLTexture.Feature = ... # 0x4
    TextureArrays            : QOpenGLTexture.Feature = ... # 0x8
    Texture3D                : QOpenGLTexture.Feature = ... # 0x10
    TextureMultisample       : QOpenGLTexture.Feature = ... # 0x20
    TextureBuffer            : QOpenGLTexture.Feature = ... # 0x40
    TextureCubeMapArrays     : QOpenGLTexture.Feature = ... # 0x80
    Swizzle                  : QOpenGLTexture.Feature = ... # 0x100
    StencilTexturing         : QOpenGLTexture.Feature = ... # 0x200
    AnisotropicFiltering     : QOpenGLTexture.Feature = ... # 0x400
    NPOTTextures             : QOpenGLTexture.Feature = ... # 0x800
    NPOTTextureRepeat        : QOpenGLTexture.Feature = ... # 0x1000
    Texture1D                : QOpenGLTexture.Feature = ... # 0x2000
    TextureComparisonOperators: QOpenGLTexture.Feature = ... # 0x4000
    TextureMipMapLevel       : QOpenGLTexture.Feature = ... # 0x8000
    MaxFeatureFlag           : QOpenGLTexture.Feature = ... # 0x10000
    Nearest                  : QOpenGLTexture.Filter = ... # 0x2600
    Linear                   : QOpenGLTexture.Filter = ... # 0x2601
    NearestMipMapNearest     : QOpenGLTexture.Filter = ... # 0x2700
    LinearMipMapNearest      : QOpenGLTexture.Filter = ... # 0x2701
    NearestMipMapLinear      : QOpenGLTexture.Filter = ... # 0x2702
    LinearMipMapLinear       : QOpenGLTexture.Filter = ... # 0x2703
    GenerateMipMaps          : QOpenGLTexture.MipMapGeneration = ... # 0x0
    DontGenerateMipMaps      : QOpenGLTexture.MipMapGeneration = ... # 0x1
    NoSourceFormat           : QOpenGLTexture.PixelFormat = ... # 0x0
    Stencil                  : QOpenGLTexture.PixelFormat = ... # 0x1901
    Depth                    : QOpenGLTexture.PixelFormat = ... # 0x1902
    Red                      : QOpenGLTexture.PixelFormat = ... # 0x1903
    Alpha                    : QOpenGLTexture.PixelFormat = ... # 0x1906
    RGB                      : QOpenGLTexture.PixelFormat = ... # 0x1907
    RGBA                     : QOpenGLTexture.PixelFormat = ... # 0x1908
    Luminance                : QOpenGLTexture.PixelFormat = ... # 0x1909
    LuminanceAlpha           : QOpenGLTexture.PixelFormat = ... # 0x190a
    BGR                      : QOpenGLTexture.PixelFormat = ... # 0x80e0
    BGRA                     : QOpenGLTexture.PixelFormat = ... # 0x80e1
    RG                       : QOpenGLTexture.PixelFormat = ... # 0x8227
    RG_Integer               : QOpenGLTexture.PixelFormat = ... # 0x8228
    DepthStencil             : QOpenGLTexture.PixelFormat = ... # 0x84f9
    Red_Integer              : QOpenGLTexture.PixelFormat = ... # 0x8d94
    RGB_Integer              : QOpenGLTexture.PixelFormat = ... # 0x8d98
    RGBA_Integer             : QOpenGLTexture.PixelFormat = ... # 0x8d99
    BGR_Integer              : QOpenGLTexture.PixelFormat = ... # 0x8d9a
    BGRA_Integer             : QOpenGLTexture.PixelFormat = ... # 0x8d9b
    NoPixelType              : QOpenGLTexture.PixelType = ... # 0x0
    Int8                     : QOpenGLTexture.PixelType = ... # 0x1400
    UInt8                    : QOpenGLTexture.PixelType = ... # 0x1401
    Int16                    : QOpenGLTexture.PixelType = ... # 0x1402
    UInt16                   : QOpenGLTexture.PixelType = ... # 0x1403
    Int32                    : QOpenGLTexture.PixelType = ... # 0x1404
    UInt32                   : QOpenGLTexture.PixelType = ... # 0x1405
    Float32                  : QOpenGLTexture.PixelType = ... # 0x1406
    Float16                  : QOpenGLTexture.PixelType = ... # 0x140b
    UInt8_RG3B2              : QOpenGLTexture.PixelType = ... # 0x8032
    UInt16_RGBA4             : QOpenGLTexture.PixelType = ... # 0x8033
    UInt16_RGB5A1            : QOpenGLTexture.PixelType = ... # 0x8034
    UInt32_RGBA8             : QOpenGLTexture.PixelType = ... # 0x8035
    UInt32_RGB10A2           : QOpenGLTexture.PixelType = ... # 0x8036
    UInt8_RG3B2_Rev          : QOpenGLTexture.PixelType = ... # 0x8362
    UInt16_R5G6B5            : QOpenGLTexture.PixelType = ... # 0x8363
    UInt16_R5G6B5_Rev        : QOpenGLTexture.PixelType = ... # 0x8364
    UInt16_RGBA4_Rev         : QOpenGLTexture.PixelType = ... # 0x8365
    UInt16_RGB5A1_Rev        : QOpenGLTexture.PixelType = ... # 0x8366
    UInt32_RGBA8_Rev         : QOpenGLTexture.PixelType = ... # 0x8367
    UInt32_RGB10A2_Rev       : QOpenGLTexture.PixelType = ... # 0x8368
    UInt32_D24S8             : QOpenGLTexture.PixelType = ... # 0x84fa
    UInt32_RG11B10F          : QOpenGLTexture.PixelType = ... # 0x8c3b
    UInt32_RGB9_E5           : QOpenGLTexture.PixelType = ... # 0x8c3e
    Float16OES               : QOpenGLTexture.PixelType = ... # 0x8d61
    Float32_D32_UInt32_S8_X24: QOpenGLTexture.PixelType = ... # 0x8dad
    SwizzleRed               : QOpenGLTexture.SwizzleComponent = ... # 0x8e42
    SwizzleGreen             : QOpenGLTexture.SwizzleComponent = ... # 0x8e43
    SwizzleBlue              : QOpenGLTexture.SwizzleComponent = ... # 0x8e44
    SwizzleAlpha             : QOpenGLTexture.SwizzleComponent = ... # 0x8e45
    ZeroValue                : QOpenGLTexture.SwizzleValue = ... # 0x0
    OneValue                 : QOpenGLTexture.SwizzleValue = ... # 0x1
    RedValue                 : QOpenGLTexture.SwizzleValue = ... # 0x1903
    GreenValue               : QOpenGLTexture.SwizzleValue = ... # 0x1904
    BlueValue                : QOpenGLTexture.SwizzleValue = ... # 0x1905
    AlphaValue               : QOpenGLTexture.SwizzleValue = ... # 0x1906
    Target1D                 : QOpenGLTexture.Target = ... # 0xde0
    Target2D                 : QOpenGLTexture.Target = ... # 0xde1
    Target3D                 : QOpenGLTexture.Target = ... # 0x806f
    TargetRectangle          : QOpenGLTexture.Target = ... # 0x84f5
    TargetCubeMap            : QOpenGLTexture.Target = ... # 0x8513
    Target1DArray            : QOpenGLTexture.Target = ... # 0x8c18
    Target2DArray            : QOpenGLTexture.Target = ... # 0x8c1a
    TargetBuffer             : QOpenGLTexture.Target = ... # 0x8c2a
    TargetCubeMapArray       : QOpenGLTexture.Target = ... # 0x9009
    Target2DMultisample      : QOpenGLTexture.Target = ... # 0x9100
    Target2DMultisampleArray : QOpenGLTexture.Target = ... # 0x9102
    NoFormat                 : QOpenGLTexture.TextureFormat = ... # 0x0
    DepthFormat              : QOpenGLTexture.TextureFormat = ... # 0x1902
    AlphaFormat              : QOpenGLTexture.TextureFormat = ... # 0x1906
    RGBFormat                : QOpenGLTexture.TextureFormat = ... # 0x1907
    RGBAFormat               : QOpenGLTexture.TextureFormat = ... # 0x1908
    LuminanceFormat          : QOpenGLTexture.TextureFormat = ... # 0x1909
    LuminanceAlphaFormat     : QOpenGLTexture.TextureFormat = ... # 0x190a
    RG3B2                    : QOpenGLTexture.TextureFormat = ... # 0x2a10
    RGB8_UNorm               : QOpenGLTexture.TextureFormat = ... # 0x8051
    RGB16_UNorm              : QOpenGLTexture.TextureFormat = ... # 0x8054
    RGBA4                    : QOpenGLTexture.TextureFormat = ... # 0x8056
    RGB5A1                   : QOpenGLTexture.TextureFormat = ... # 0x8057
    RGBA8_UNorm              : QOpenGLTexture.TextureFormat = ... # 0x8058
    RGBA16_UNorm             : QOpenGLTexture.TextureFormat = ... # 0x805b
    D16                      : QOpenGLTexture.TextureFormat = ... # 0x81a5
    D24                      : QOpenGLTexture.TextureFormat = ... # 0x81a6
    D32                      : QOpenGLTexture.TextureFormat = ... # 0x81a7
    R8_UNorm                 : QOpenGLTexture.TextureFormat = ... # 0x8229
    R16_UNorm                : QOpenGLTexture.TextureFormat = ... # 0x822a
    RG8_UNorm                : QOpenGLTexture.TextureFormat = ... # 0x822b
    RG16_UNorm               : QOpenGLTexture.TextureFormat = ... # 0x822c
    R16F                     : QOpenGLTexture.TextureFormat = ... # 0x822d
    R32F                     : QOpenGLTexture.TextureFormat = ... # 0x822e
    RG16F                    : QOpenGLTexture.TextureFormat = ... # 0x822f
    RG32F                    : QOpenGLTexture.TextureFormat = ... # 0x8230
    R8I                      : QOpenGLTexture.TextureFormat = ... # 0x8231
    R8U                      : QOpenGLTexture.TextureFormat = ... # 0x8232
    R16I                     : QOpenGLTexture.TextureFormat = ... # 0x8233
    R16U                     : QOpenGLTexture.TextureFormat = ... # 0x8234
    R32I                     : QOpenGLTexture.TextureFormat = ... # 0x8235
    R32U                     : QOpenGLTexture.TextureFormat = ... # 0x8236
    RG8I                     : QOpenGLTexture.TextureFormat = ... # 0x8237
    RG8U                     : QOpenGLTexture.TextureFormat = ... # 0x8238
    RG16I                    : QOpenGLTexture.TextureFormat = ... # 0x8239
    RG16U                    : QOpenGLTexture.TextureFormat = ... # 0x823a
    RG32I                    : QOpenGLTexture.TextureFormat = ... # 0x823b
    RG32U                    : QOpenGLTexture.TextureFormat = ... # 0x823c
    RGB_DXT1                 : QOpenGLTexture.TextureFormat = ... # 0x83f0
    RGBA_DXT1                : QOpenGLTexture.TextureFormat = ... # 0x83f1
    RGBA_DXT3                : QOpenGLTexture.TextureFormat = ... # 0x83f2
    RGBA_DXT5                : QOpenGLTexture.TextureFormat = ... # 0x83f3
    RGBA32F                  : QOpenGLTexture.TextureFormat = ... # 0x8814
    RGB32F                   : QOpenGLTexture.TextureFormat = ... # 0x8815
    RGBA16F                  : QOpenGLTexture.TextureFormat = ... # 0x881a
    RGB16F                   : QOpenGLTexture.TextureFormat = ... # 0x881b
    D24S8                    : QOpenGLTexture.TextureFormat = ... # 0x88f0
    RG11B10F                 : QOpenGLTexture.TextureFormat = ... # 0x8c3a
    RGB9E5                   : QOpenGLTexture.TextureFormat = ... # 0x8c3d
    SRGB8                    : QOpenGLTexture.TextureFormat = ... # 0x8c41
    SRGB8_Alpha8             : QOpenGLTexture.TextureFormat = ... # 0x8c43
    SRGB_DXT1                : QOpenGLTexture.TextureFormat = ... # 0x8c4c
    SRGB_Alpha_DXT1          : QOpenGLTexture.TextureFormat = ... # 0x8c4d
    SRGB_Alpha_DXT3          : QOpenGLTexture.TextureFormat = ... # 0x8c4e
    SRGB_Alpha_DXT5          : QOpenGLTexture.TextureFormat = ... # 0x8c4f
    D32F                     : QOpenGLTexture.TextureFormat = ... # 0x8cac
    D32FS8X24                : QOpenGLTexture.TextureFormat = ... # 0x8cad
    S8                       : QOpenGLTexture.TextureFormat = ... # 0x8d48
    R5G6B5                   : QOpenGLTexture.TextureFormat = ... # 0x8d62
    RGB8_ETC1                : QOpenGLTexture.TextureFormat = ... # 0x8d64
    RGBA32U                  : QOpenGLTexture.TextureFormat = ... # 0x8d70
    RGB32U                   : QOpenGLTexture.TextureFormat = ... # 0x8d71
    RGBA16U                  : QOpenGLTexture.TextureFormat = ... # 0x8d76
    RGB16U                   : QOpenGLTexture.TextureFormat = ... # 0x8d77
    RGBA8U                   : QOpenGLTexture.TextureFormat = ... # 0x8d7c
    RGB8U                    : QOpenGLTexture.TextureFormat = ... # 0x8d7d
    RGBA32I                  : QOpenGLTexture.TextureFormat = ... # 0x8d82
    RGB32I                   : QOpenGLTexture.TextureFormat = ... # 0x8d83
    RGBA16I                  : QOpenGLTexture.TextureFormat = ... # 0x8d88
    RGB16I                   : QOpenGLTexture.TextureFormat = ... # 0x8d89
    RGBA8I                   : QOpenGLTexture.TextureFormat = ... # 0x8d8e
    RGB8I                    : QOpenGLTexture.TextureFormat = ... # 0x8d8f
    R_ATI1N_UNorm            : QOpenGLTexture.TextureFormat = ... # 0x8dbb
    R_ATI1N_SNorm            : QOpenGLTexture.TextureFormat = ... # 0x8dbc
    RG_ATI2N_UNorm           : QOpenGLTexture.TextureFormat = ... # 0x8dbd
    RG_ATI2N_SNorm           : QOpenGLTexture.TextureFormat = ... # 0x8dbe
    RGB_BP_UNorm             : QOpenGLTexture.TextureFormat = ... # 0x8e8c
    SRGB_BP_UNorm            : QOpenGLTexture.TextureFormat = ... # 0x8e8d
    RGB_BP_SIGNED_FLOAT      : QOpenGLTexture.TextureFormat = ... # 0x8e8e
    RGB_BP_UNSIGNED_FLOAT    : QOpenGLTexture.TextureFormat = ... # 0x8e8f
    R8_SNorm                 : QOpenGLTexture.TextureFormat = ... # 0x8f94
    RG8_SNorm                : QOpenGLTexture.TextureFormat = ... # 0x8f95
    RGB8_SNorm               : QOpenGLTexture.TextureFormat = ... # 0x8f96
    RGBA8_SNorm              : QOpenGLTexture.TextureFormat = ... # 0x8f97
    R16_SNorm                : QOpenGLTexture.TextureFormat = ... # 0x8f98
    RG16_SNorm               : QOpenGLTexture.TextureFormat = ... # 0x8f99
    RGB16_SNorm              : QOpenGLTexture.TextureFormat = ... # 0x8f9a
    RGBA16_SNorm             : QOpenGLTexture.TextureFormat = ... # 0x8f9b
    RGB10A2                  : QOpenGLTexture.TextureFormat = ... # 0x906f
    R11_EAC_UNorm            : QOpenGLTexture.TextureFormat = ... # 0x9270
    R11_EAC_SNorm            : QOpenGLTexture.TextureFormat = ... # 0x9271
    RG11_EAC_UNorm           : QOpenGLTexture.TextureFormat = ... # 0x9272
    RG11_EAC_SNorm           : QOpenGLTexture.TextureFormat = ... # 0x9273
    RGB8_ETC2                : QOpenGLTexture.TextureFormat = ... # 0x9274
    SRGB8_ETC2               : QOpenGLTexture.TextureFormat = ... # 0x9275
    RGB8_PunchThrough_Alpha1_ETC2: QOpenGLTexture.TextureFormat = ... # 0x9276
    SRGB8_PunchThrough_Alpha1_ETC2: QOpenGLTexture.TextureFormat = ... # 0x9277
    RGBA8_ETC2_EAC           : QOpenGLTexture.TextureFormat = ... # 0x9278
    SRGB8_Alpha8_ETC2_EAC    : QOpenGLTexture.TextureFormat = ... # 0x9279
    RGBA_ASTC_4x4            : QOpenGLTexture.TextureFormat = ... # 0x93b0
    RGBA_ASTC_5x4            : QOpenGLTexture.TextureFormat = ... # 0x93b1
    RGBA_ASTC_5x5            : QOpenGLTexture.TextureFormat = ... # 0x93b2
    RGBA_ASTC_6x5            : QOpenGLTexture.TextureFormat = ... # 0x93b3
    RGBA_ASTC_6x6            : QOpenGLTexture.TextureFormat = ... # 0x93b4
    RGBA_ASTC_8x5            : QOpenGLTexture.TextureFormat = ... # 0x93b5
    RGBA_ASTC_8x6            : QOpenGLTexture.TextureFormat = ... # 0x93b6
    RGBA_ASTC_8x8            : QOpenGLTexture.TextureFormat = ... # 0x93b7
    RGBA_ASTC_10x5           : QOpenGLTexture.TextureFormat = ... # 0x93b8
    RGBA_ASTC_10x6           : QOpenGLTexture.TextureFormat = ... # 0x93b9
    RGBA_ASTC_10x8           : QOpenGLTexture.TextureFormat = ... # 0x93ba
    RGBA_ASTC_10x10          : QOpenGLTexture.TextureFormat = ... # 0x93bb
    RGBA_ASTC_12x10          : QOpenGLTexture.TextureFormat = ... # 0x93bc
    RGBA_ASTC_12x12          : QOpenGLTexture.TextureFormat = ... # 0x93bd
    SRGB8_Alpha8_ASTC_4x4    : QOpenGLTexture.TextureFormat = ... # 0x93d0
    SRGB8_Alpha8_ASTC_5x4    : QOpenGLTexture.TextureFormat = ... # 0x93d1
    SRGB8_Alpha8_ASTC_5x5    : QOpenGLTexture.TextureFormat = ... # 0x93d2
    SRGB8_Alpha8_ASTC_6x5    : QOpenGLTexture.TextureFormat = ... # 0x93d3
    SRGB8_Alpha8_ASTC_6x6    : QOpenGLTexture.TextureFormat = ... # 0x93d4
    SRGB8_Alpha8_ASTC_8x5    : QOpenGLTexture.TextureFormat = ... # 0x93d5
    SRGB8_Alpha8_ASTC_8x6    : QOpenGLTexture.TextureFormat = ... # 0x93d6
    SRGB8_Alpha8_ASTC_8x8    : QOpenGLTexture.TextureFormat = ... # 0x93d7
    SRGB8_Alpha8_ASTC_10x5   : QOpenGLTexture.TextureFormat = ... # 0x93d8
    SRGB8_Alpha8_ASTC_10x6   : QOpenGLTexture.TextureFormat = ... # 0x93d9
    SRGB8_Alpha8_ASTC_10x8   : QOpenGLTexture.TextureFormat = ... # 0x93da
    SRGB8_Alpha8_ASTC_10x10  : QOpenGLTexture.TextureFormat = ... # 0x93db
    SRGB8_Alpha8_ASTC_12x10  : QOpenGLTexture.TextureFormat = ... # 0x93dc
    SRGB8_Alpha8_ASTC_12x12  : QOpenGLTexture.TextureFormat = ... # 0x93dd
    NoFormatClass            : QOpenGLTexture.TextureFormatClass = ... # 0x0
    FormatClass_128Bit       : QOpenGLTexture.TextureFormatClass = ... # 0x1
    FormatClass_96Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x2
    FormatClass_64Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x3
    FormatClass_48Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x4
    FormatClass_32Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x5
    FormatClass_24Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x6
    FormatClass_16Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x7
    FormatClass_8Bit         : QOpenGLTexture.TextureFormatClass = ... # 0x8
    FormatClass_RGTC1_R      : QOpenGLTexture.TextureFormatClass = ... # 0x9
    FormatClass_RGTC2_RG     : QOpenGLTexture.TextureFormatClass = ... # 0xa
    FormatClass_BPTC_Unorm   : QOpenGLTexture.TextureFormatClass = ... # 0xb
    FormatClass_BPTC_Float   : QOpenGLTexture.TextureFormatClass = ... # 0xc
    FormatClass_S3TC_DXT1_RGB: QOpenGLTexture.TextureFormatClass = ... # 0xd
    FormatClass_S3TC_DXT1_RGBA: QOpenGLTexture.TextureFormatClass = ... # 0xe
    FormatClass_S3TC_DXT3_RGBA: QOpenGLTexture.TextureFormatClass = ... # 0xf
    FormatClass_S3TC_DXT5_RGBA: QOpenGLTexture.TextureFormatClass = ... # 0x10
    FormatClass_Unique       : QOpenGLTexture.TextureFormatClass = ... # 0x11
    ResetTextureUnit         : QOpenGLTexture.TextureUnitReset = ... # 0x0
    DontResetTextureUnit     : QOpenGLTexture.TextureUnitReset = ... # 0x1
    Repeat                   : QOpenGLTexture.WrapMode = ... # 0x2901
    ClampToBorder            : QOpenGLTexture.WrapMode = ... # 0x812d
    ClampToEdge              : QOpenGLTexture.WrapMode = ... # 0x812f
    MirroredRepeat           : QOpenGLTexture.WrapMode = ... # 0x8370

    class BindingTarget(Shiboken.Enum):
        BindingTarget1D          : QOpenGLTexture.BindingTarget = ... # 0x8068
        BindingTarget2D          : QOpenGLTexture.BindingTarget = ... # 0x8069
        BindingTarget3D          : QOpenGLTexture.BindingTarget = ... # 0x806a
        BindingTargetRectangle   : QOpenGLTexture.BindingTarget = ... # 0x84f6
        BindingTargetCubeMap     : QOpenGLTexture.BindingTarget = ... # 0x8514
        BindingTarget1DArray     : QOpenGLTexture.BindingTarget = ... # 0x8c1c
        BindingTarget2DArray     : QOpenGLTexture.BindingTarget = ... # 0x8c1d
        BindingTargetBuffer      : QOpenGLTexture.BindingTarget = ... # 0x8c2c
        BindingTargetCubeMapArray: QOpenGLTexture.BindingTarget = ... # 0x900a
        BindingTarget2DMultisample: QOpenGLTexture.BindingTarget = ... # 0x9104
        BindingTarget2DMultisampleArray: QOpenGLTexture.BindingTarget = ... # 0x9105

    class ComparisonFunction(Shiboken.Enum):
        CompareNever             : QOpenGLTexture.ComparisonFunction = ... # 0x200
        CompareLess              : QOpenGLTexture.ComparisonFunction = ... # 0x201
        CompareEqual             : QOpenGLTexture.ComparisonFunction = ... # 0x202
        CompareLessEqual         : QOpenGLTexture.ComparisonFunction = ... # 0x203
        CompareGreater           : QOpenGLTexture.ComparisonFunction = ... # 0x204
        CommpareNotEqual         : QOpenGLTexture.ComparisonFunction = ... # 0x205
        CompareGreaterEqual      : QOpenGLTexture.ComparisonFunction = ... # 0x206
        CompareAlways            : QOpenGLTexture.ComparisonFunction = ... # 0x207

    class ComparisonMode(Shiboken.Enum):
        CompareNone              : QOpenGLTexture.ComparisonMode = ... # 0x0
        CompareRefToTexture      : QOpenGLTexture.ComparisonMode = ... # 0x884e

    class CoordinateDirection(Shiboken.Enum):
        DirectionS               : QOpenGLTexture.CoordinateDirection = ... # 0x2802
        DirectionT               : QOpenGLTexture.CoordinateDirection = ... # 0x2803
        DirectionR               : QOpenGLTexture.CoordinateDirection = ... # 0x8072

    class CubeMapFace(Shiboken.Enum):
        CubeMapPositiveX         : QOpenGLTexture.CubeMapFace = ... # 0x8515
        CubeMapNegativeX         : QOpenGLTexture.CubeMapFace = ... # 0x8516
        CubeMapPositiveY         : QOpenGLTexture.CubeMapFace = ... # 0x8517
        CubeMapNegativeY         : QOpenGLTexture.CubeMapFace = ... # 0x8518
        CubeMapPositiveZ         : QOpenGLTexture.CubeMapFace = ... # 0x8519
        CubeMapNegativeZ         : QOpenGLTexture.CubeMapFace = ... # 0x851a

    class DepthStencilMode(Shiboken.Enum):
        StencilMode              : QOpenGLTexture.DepthStencilMode = ... # 0x1901
        DepthMode                : QOpenGLTexture.DepthStencilMode = ... # 0x1902

    class Feature(Shiboken.Enum):
        ImmutableStorage         : QOpenGLTexture.Feature = ... # 0x1
        ImmutableMultisampleStorage: QOpenGLTexture.Feature = ... # 0x2
        TextureRectangle         : QOpenGLTexture.Feature = ... # 0x4
        TextureArrays            : QOpenGLTexture.Feature = ... # 0x8
        Texture3D                : QOpenGLTexture.Feature = ... # 0x10
        TextureMultisample       : QOpenGLTexture.Feature = ... # 0x20
        TextureBuffer            : QOpenGLTexture.Feature = ... # 0x40
        TextureCubeMapArrays     : QOpenGLTexture.Feature = ... # 0x80
        Swizzle                  : QOpenGLTexture.Feature = ... # 0x100
        StencilTexturing         : QOpenGLTexture.Feature = ... # 0x200
        AnisotropicFiltering     : QOpenGLTexture.Feature = ... # 0x400
        NPOTTextures             : QOpenGLTexture.Feature = ... # 0x800
        NPOTTextureRepeat        : QOpenGLTexture.Feature = ... # 0x1000
        Texture1D                : QOpenGLTexture.Feature = ... # 0x2000
        TextureComparisonOperators: QOpenGLTexture.Feature = ... # 0x4000
        TextureMipMapLevel       : QOpenGLTexture.Feature = ... # 0x8000
        MaxFeatureFlag           : QOpenGLTexture.Feature = ... # 0x10000

    class Features(object): ...

    class Filter(Shiboken.Enum):
        Nearest                  : QOpenGLTexture.Filter = ... # 0x2600
        Linear                   : QOpenGLTexture.Filter = ... # 0x2601
        NearestMipMapNearest     : QOpenGLTexture.Filter = ... # 0x2700
        LinearMipMapNearest      : QOpenGLTexture.Filter = ... # 0x2701
        NearestMipMapLinear      : QOpenGLTexture.Filter = ... # 0x2702
        LinearMipMapLinear       : QOpenGLTexture.Filter = ... # 0x2703

    class MipMapGeneration(Shiboken.Enum):
        GenerateMipMaps          : QOpenGLTexture.MipMapGeneration = ... # 0x0
        DontGenerateMipMaps      : QOpenGLTexture.MipMapGeneration = ... # 0x1

    class PixelFormat(Shiboken.Enum):
        NoSourceFormat           : QOpenGLTexture.PixelFormat = ... # 0x0
        Stencil                  : QOpenGLTexture.PixelFormat = ... # 0x1901
        Depth                    : QOpenGLTexture.PixelFormat = ... # 0x1902
        Red                      : QOpenGLTexture.PixelFormat = ... # 0x1903
        Alpha                    : QOpenGLTexture.PixelFormat = ... # 0x1906
        RGB                      : QOpenGLTexture.PixelFormat = ... # 0x1907
        RGBA                     : QOpenGLTexture.PixelFormat = ... # 0x1908
        Luminance                : QOpenGLTexture.PixelFormat = ... # 0x1909
        LuminanceAlpha           : QOpenGLTexture.PixelFormat = ... # 0x190a
        BGR                      : QOpenGLTexture.PixelFormat = ... # 0x80e0
        BGRA                     : QOpenGLTexture.PixelFormat = ... # 0x80e1
        RG                       : QOpenGLTexture.PixelFormat = ... # 0x8227
        RG_Integer               : QOpenGLTexture.PixelFormat = ... # 0x8228
        DepthStencil             : QOpenGLTexture.PixelFormat = ... # 0x84f9
        Red_Integer              : QOpenGLTexture.PixelFormat = ... # 0x8d94
        RGB_Integer              : QOpenGLTexture.PixelFormat = ... # 0x8d98
        RGBA_Integer             : QOpenGLTexture.PixelFormat = ... # 0x8d99
        BGR_Integer              : QOpenGLTexture.PixelFormat = ... # 0x8d9a
        BGRA_Integer             : QOpenGLTexture.PixelFormat = ... # 0x8d9b

    class PixelType(Shiboken.Enum):
        NoPixelType              : QOpenGLTexture.PixelType = ... # 0x0
        Int8                     : QOpenGLTexture.PixelType = ... # 0x1400
        UInt8                    : QOpenGLTexture.PixelType = ... # 0x1401
        Int16                    : QOpenGLTexture.PixelType = ... # 0x1402
        UInt16                   : QOpenGLTexture.PixelType = ... # 0x1403
        Int32                    : QOpenGLTexture.PixelType = ... # 0x1404
        UInt32                   : QOpenGLTexture.PixelType = ... # 0x1405
        Float32                  : QOpenGLTexture.PixelType = ... # 0x1406
        Float16                  : QOpenGLTexture.PixelType = ... # 0x140b
        UInt8_RG3B2              : QOpenGLTexture.PixelType = ... # 0x8032
        UInt16_RGBA4             : QOpenGLTexture.PixelType = ... # 0x8033
        UInt16_RGB5A1            : QOpenGLTexture.PixelType = ... # 0x8034
        UInt32_RGBA8             : QOpenGLTexture.PixelType = ... # 0x8035
        UInt32_RGB10A2           : QOpenGLTexture.PixelType = ... # 0x8036
        UInt8_RG3B2_Rev          : QOpenGLTexture.PixelType = ... # 0x8362
        UInt16_R5G6B5            : QOpenGLTexture.PixelType = ... # 0x8363
        UInt16_R5G6B5_Rev        : QOpenGLTexture.PixelType = ... # 0x8364
        UInt16_RGBA4_Rev         : QOpenGLTexture.PixelType = ... # 0x8365
        UInt16_RGB5A1_Rev        : QOpenGLTexture.PixelType = ... # 0x8366
        UInt32_RGBA8_Rev         : QOpenGLTexture.PixelType = ... # 0x8367
        UInt32_RGB10A2_Rev       : QOpenGLTexture.PixelType = ... # 0x8368
        UInt32_D24S8             : QOpenGLTexture.PixelType = ... # 0x84fa
        UInt32_RG11B10F          : QOpenGLTexture.PixelType = ... # 0x8c3b
        UInt32_RGB9_E5           : QOpenGLTexture.PixelType = ... # 0x8c3e
        Float16OES               : QOpenGLTexture.PixelType = ... # 0x8d61
        Float32_D32_UInt32_S8_X24: QOpenGLTexture.PixelType = ... # 0x8dad

    class SwizzleComponent(Shiboken.Enum):
        SwizzleRed               : QOpenGLTexture.SwizzleComponent = ... # 0x8e42
        SwizzleGreen             : QOpenGLTexture.SwizzleComponent = ... # 0x8e43
        SwizzleBlue              : QOpenGLTexture.SwizzleComponent = ... # 0x8e44
        SwizzleAlpha             : QOpenGLTexture.SwizzleComponent = ... # 0x8e45

    class SwizzleValue(Shiboken.Enum):
        ZeroValue                : QOpenGLTexture.SwizzleValue = ... # 0x0
        OneValue                 : QOpenGLTexture.SwizzleValue = ... # 0x1
        RedValue                 : QOpenGLTexture.SwizzleValue = ... # 0x1903
        GreenValue               : QOpenGLTexture.SwizzleValue = ... # 0x1904
        BlueValue                : QOpenGLTexture.SwizzleValue = ... # 0x1905
        AlphaValue               : QOpenGLTexture.SwizzleValue = ... # 0x1906

    class Target(Shiboken.Enum):
        Target1D                 : QOpenGLTexture.Target = ... # 0xde0
        Target2D                 : QOpenGLTexture.Target = ... # 0xde1
        Target3D                 : QOpenGLTexture.Target = ... # 0x806f
        TargetRectangle          : QOpenGLTexture.Target = ... # 0x84f5
        TargetCubeMap            : QOpenGLTexture.Target = ... # 0x8513
        Target1DArray            : QOpenGLTexture.Target = ... # 0x8c18
        Target2DArray            : QOpenGLTexture.Target = ... # 0x8c1a
        TargetBuffer             : QOpenGLTexture.Target = ... # 0x8c2a
        TargetCubeMapArray       : QOpenGLTexture.Target = ... # 0x9009
        Target2DMultisample      : QOpenGLTexture.Target = ... # 0x9100
        Target2DMultisampleArray : QOpenGLTexture.Target = ... # 0x9102

    class TextureFormat(Shiboken.Enum):
        NoFormat                 : QOpenGLTexture.TextureFormat = ... # 0x0
        DepthFormat              : QOpenGLTexture.TextureFormat = ... # 0x1902
        AlphaFormat              : QOpenGLTexture.TextureFormat = ... # 0x1906
        RGBFormat                : QOpenGLTexture.TextureFormat = ... # 0x1907
        RGBAFormat               : QOpenGLTexture.TextureFormat = ... # 0x1908
        LuminanceFormat          : QOpenGLTexture.TextureFormat = ... # 0x1909
        LuminanceAlphaFormat     : QOpenGLTexture.TextureFormat = ... # 0x190a
        RG3B2                    : QOpenGLTexture.TextureFormat = ... # 0x2a10
        RGB8_UNorm               : QOpenGLTexture.TextureFormat = ... # 0x8051
        RGB16_UNorm              : QOpenGLTexture.TextureFormat = ... # 0x8054
        RGBA4                    : QOpenGLTexture.TextureFormat = ... # 0x8056
        RGB5A1                   : QOpenGLTexture.TextureFormat = ... # 0x8057
        RGBA8_UNorm              : QOpenGLTexture.TextureFormat = ... # 0x8058
        RGBA16_UNorm             : QOpenGLTexture.TextureFormat = ... # 0x805b
        D16                      : QOpenGLTexture.TextureFormat = ... # 0x81a5
        D24                      : QOpenGLTexture.TextureFormat = ... # 0x81a6
        D32                      : QOpenGLTexture.TextureFormat = ... # 0x81a7
        R8_UNorm                 : QOpenGLTexture.TextureFormat = ... # 0x8229
        R16_UNorm                : QOpenGLTexture.TextureFormat = ... # 0x822a
        RG8_UNorm                : QOpenGLTexture.TextureFormat = ... # 0x822b
        RG16_UNorm               : QOpenGLTexture.TextureFormat = ... # 0x822c
        R16F                     : QOpenGLTexture.TextureFormat = ... # 0x822d
        R32F                     : QOpenGLTexture.TextureFormat = ... # 0x822e
        RG16F                    : QOpenGLTexture.TextureFormat = ... # 0x822f
        RG32F                    : QOpenGLTexture.TextureFormat = ... # 0x8230
        R8I                      : QOpenGLTexture.TextureFormat = ... # 0x8231
        R8U                      : QOpenGLTexture.TextureFormat = ... # 0x8232
        R16I                     : QOpenGLTexture.TextureFormat = ... # 0x8233
        R16U                     : QOpenGLTexture.TextureFormat = ... # 0x8234
        R32I                     : QOpenGLTexture.TextureFormat = ... # 0x8235
        R32U                     : QOpenGLTexture.TextureFormat = ... # 0x8236
        RG8I                     : QOpenGLTexture.TextureFormat = ... # 0x8237
        RG8U                     : QOpenGLTexture.TextureFormat = ... # 0x8238
        RG16I                    : QOpenGLTexture.TextureFormat = ... # 0x8239
        RG16U                    : QOpenGLTexture.TextureFormat = ... # 0x823a
        RG32I                    : QOpenGLTexture.TextureFormat = ... # 0x823b
        RG32U                    : QOpenGLTexture.TextureFormat = ... # 0x823c
        RGB_DXT1                 : QOpenGLTexture.TextureFormat = ... # 0x83f0
        RGBA_DXT1                : QOpenGLTexture.TextureFormat = ... # 0x83f1
        RGBA_DXT3                : QOpenGLTexture.TextureFormat = ... # 0x83f2
        RGBA_DXT5                : QOpenGLTexture.TextureFormat = ... # 0x83f3
        RGBA32F                  : QOpenGLTexture.TextureFormat = ... # 0x8814
        RGB32F                   : QOpenGLTexture.TextureFormat = ... # 0x8815
        RGBA16F                  : QOpenGLTexture.TextureFormat = ... # 0x881a
        RGB16F                   : QOpenGLTexture.TextureFormat = ... # 0x881b
        D24S8                    : QOpenGLTexture.TextureFormat = ... # 0x88f0
        RG11B10F                 : QOpenGLTexture.TextureFormat = ... # 0x8c3a
        RGB9E5                   : QOpenGLTexture.TextureFormat = ... # 0x8c3d
        SRGB8                    : QOpenGLTexture.TextureFormat = ... # 0x8c41
        SRGB8_Alpha8             : QOpenGLTexture.TextureFormat = ... # 0x8c43
        SRGB_DXT1                : QOpenGLTexture.TextureFormat = ... # 0x8c4c
        SRGB_Alpha_DXT1          : QOpenGLTexture.TextureFormat = ... # 0x8c4d
        SRGB_Alpha_DXT3          : QOpenGLTexture.TextureFormat = ... # 0x8c4e
        SRGB_Alpha_DXT5          : QOpenGLTexture.TextureFormat = ... # 0x8c4f
        D32F                     : QOpenGLTexture.TextureFormat = ... # 0x8cac
        D32FS8X24                : QOpenGLTexture.TextureFormat = ... # 0x8cad
        S8                       : QOpenGLTexture.TextureFormat = ... # 0x8d48
        R5G6B5                   : QOpenGLTexture.TextureFormat = ... # 0x8d62
        RGB8_ETC1                : QOpenGLTexture.TextureFormat = ... # 0x8d64
        RGBA32U                  : QOpenGLTexture.TextureFormat = ... # 0x8d70
        RGB32U                   : QOpenGLTexture.TextureFormat = ... # 0x8d71
        RGBA16U                  : QOpenGLTexture.TextureFormat = ... # 0x8d76
        RGB16U                   : QOpenGLTexture.TextureFormat = ... # 0x8d77
        RGBA8U                   : QOpenGLTexture.TextureFormat = ... # 0x8d7c
        RGB8U                    : QOpenGLTexture.TextureFormat = ... # 0x8d7d
        RGBA32I                  : QOpenGLTexture.TextureFormat = ... # 0x8d82
        RGB32I                   : QOpenGLTexture.TextureFormat = ... # 0x8d83
        RGBA16I                  : QOpenGLTexture.TextureFormat = ... # 0x8d88
        RGB16I                   : QOpenGLTexture.TextureFormat = ... # 0x8d89
        RGBA8I                   : QOpenGLTexture.TextureFormat = ... # 0x8d8e
        RGB8I                    : QOpenGLTexture.TextureFormat = ... # 0x8d8f
        R_ATI1N_UNorm            : QOpenGLTexture.TextureFormat = ... # 0x8dbb
        R_ATI1N_SNorm            : QOpenGLTexture.TextureFormat = ... # 0x8dbc
        RG_ATI2N_UNorm           : QOpenGLTexture.TextureFormat = ... # 0x8dbd
        RG_ATI2N_SNorm           : QOpenGLTexture.TextureFormat = ... # 0x8dbe
        RGB_BP_UNorm             : QOpenGLTexture.TextureFormat = ... # 0x8e8c
        SRGB_BP_UNorm            : QOpenGLTexture.TextureFormat = ... # 0x8e8d
        RGB_BP_SIGNED_FLOAT      : QOpenGLTexture.TextureFormat = ... # 0x8e8e
        RGB_BP_UNSIGNED_FLOAT    : QOpenGLTexture.TextureFormat = ... # 0x8e8f
        R8_SNorm                 : QOpenGLTexture.TextureFormat = ... # 0x8f94
        RG8_SNorm                : QOpenGLTexture.TextureFormat = ... # 0x8f95
        RGB8_SNorm               : QOpenGLTexture.TextureFormat = ... # 0x8f96
        RGBA8_SNorm              : QOpenGLTexture.TextureFormat = ... # 0x8f97
        R16_SNorm                : QOpenGLTexture.TextureFormat = ... # 0x8f98
        RG16_SNorm               : QOpenGLTexture.TextureFormat = ... # 0x8f99
        RGB16_SNorm              : QOpenGLTexture.TextureFormat = ... # 0x8f9a
        RGBA16_SNorm             : QOpenGLTexture.TextureFormat = ... # 0x8f9b
        RGB10A2                  : QOpenGLTexture.TextureFormat = ... # 0x906f
        R11_EAC_UNorm            : QOpenGLTexture.TextureFormat = ... # 0x9270
        R11_EAC_SNorm            : QOpenGLTexture.TextureFormat = ... # 0x9271
        RG11_EAC_UNorm           : QOpenGLTexture.TextureFormat = ... # 0x9272
        RG11_EAC_SNorm           : QOpenGLTexture.TextureFormat = ... # 0x9273
        RGB8_ETC2                : QOpenGLTexture.TextureFormat = ... # 0x9274
        SRGB8_ETC2               : QOpenGLTexture.TextureFormat = ... # 0x9275
        RGB8_PunchThrough_Alpha1_ETC2: QOpenGLTexture.TextureFormat = ... # 0x9276
        SRGB8_PunchThrough_Alpha1_ETC2: QOpenGLTexture.TextureFormat = ... # 0x9277
        RGBA8_ETC2_EAC           : QOpenGLTexture.TextureFormat = ... # 0x9278
        SRGB8_Alpha8_ETC2_EAC    : QOpenGLTexture.TextureFormat = ... # 0x9279
        RGBA_ASTC_4x4            : QOpenGLTexture.TextureFormat = ... # 0x93b0
        RGBA_ASTC_5x4            : QOpenGLTexture.TextureFormat = ... # 0x93b1
        RGBA_ASTC_5x5            : QOpenGLTexture.TextureFormat = ... # 0x93b2
        RGBA_ASTC_6x5            : QOpenGLTexture.TextureFormat = ... # 0x93b3
        RGBA_ASTC_6x6            : QOpenGLTexture.TextureFormat = ... # 0x93b4
        RGBA_ASTC_8x5            : QOpenGLTexture.TextureFormat = ... # 0x93b5
        RGBA_ASTC_8x6            : QOpenGLTexture.TextureFormat = ... # 0x93b6
        RGBA_ASTC_8x8            : QOpenGLTexture.TextureFormat = ... # 0x93b7
        RGBA_ASTC_10x5           : QOpenGLTexture.TextureFormat = ... # 0x93b8
        RGBA_ASTC_10x6           : QOpenGLTexture.TextureFormat = ... # 0x93b9
        RGBA_ASTC_10x8           : QOpenGLTexture.TextureFormat = ... # 0x93ba
        RGBA_ASTC_10x10          : QOpenGLTexture.TextureFormat = ... # 0x93bb
        RGBA_ASTC_12x10          : QOpenGLTexture.TextureFormat = ... # 0x93bc
        RGBA_ASTC_12x12          : QOpenGLTexture.TextureFormat = ... # 0x93bd
        SRGB8_Alpha8_ASTC_4x4    : QOpenGLTexture.TextureFormat = ... # 0x93d0
        SRGB8_Alpha8_ASTC_5x4    : QOpenGLTexture.TextureFormat = ... # 0x93d1
        SRGB8_Alpha8_ASTC_5x5    : QOpenGLTexture.TextureFormat = ... # 0x93d2
        SRGB8_Alpha8_ASTC_6x5    : QOpenGLTexture.TextureFormat = ... # 0x93d3
        SRGB8_Alpha8_ASTC_6x6    : QOpenGLTexture.TextureFormat = ... # 0x93d4
        SRGB8_Alpha8_ASTC_8x5    : QOpenGLTexture.TextureFormat = ... # 0x93d5
        SRGB8_Alpha8_ASTC_8x6    : QOpenGLTexture.TextureFormat = ... # 0x93d6
        SRGB8_Alpha8_ASTC_8x8    : QOpenGLTexture.TextureFormat = ... # 0x93d7
        SRGB8_Alpha8_ASTC_10x5   : QOpenGLTexture.TextureFormat = ... # 0x93d8
        SRGB8_Alpha8_ASTC_10x6   : QOpenGLTexture.TextureFormat = ... # 0x93d9
        SRGB8_Alpha8_ASTC_10x8   : QOpenGLTexture.TextureFormat = ... # 0x93da
        SRGB8_Alpha8_ASTC_10x10  : QOpenGLTexture.TextureFormat = ... # 0x93db
        SRGB8_Alpha8_ASTC_12x10  : QOpenGLTexture.TextureFormat = ... # 0x93dc
        SRGB8_Alpha8_ASTC_12x12  : QOpenGLTexture.TextureFormat = ... # 0x93dd

    class TextureFormatClass(Shiboken.Enum):
        NoFormatClass            : QOpenGLTexture.TextureFormatClass = ... # 0x0
        FormatClass_128Bit       : QOpenGLTexture.TextureFormatClass = ... # 0x1
        FormatClass_96Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x2
        FormatClass_64Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x3
        FormatClass_48Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x4
        FormatClass_32Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x5
        FormatClass_24Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x6
        FormatClass_16Bit        : QOpenGLTexture.TextureFormatClass = ... # 0x7
        FormatClass_8Bit         : QOpenGLTexture.TextureFormatClass = ... # 0x8
        FormatClass_RGTC1_R      : QOpenGLTexture.TextureFormatClass = ... # 0x9
        FormatClass_RGTC2_RG     : QOpenGLTexture.TextureFormatClass = ... # 0xa
        FormatClass_BPTC_Unorm   : QOpenGLTexture.TextureFormatClass = ... # 0xb
        FormatClass_BPTC_Float   : QOpenGLTexture.TextureFormatClass = ... # 0xc
        FormatClass_S3TC_DXT1_RGB: QOpenGLTexture.TextureFormatClass = ... # 0xd
        FormatClass_S3TC_DXT1_RGBA: QOpenGLTexture.TextureFormatClass = ... # 0xe
        FormatClass_S3TC_DXT3_RGBA: QOpenGLTexture.TextureFormatClass = ... # 0xf
        FormatClass_S3TC_DXT5_RGBA: QOpenGLTexture.TextureFormatClass = ... # 0x10
        FormatClass_Unique       : QOpenGLTexture.TextureFormatClass = ... # 0x11

    class TextureUnitReset(Shiboken.Enum):
        ResetTextureUnit         : QOpenGLTexture.TextureUnitReset = ... # 0x0
        DontResetTextureUnit     : QOpenGLTexture.TextureUnitReset = ... # 0x1

    class WrapMode(Shiboken.Enum):
        Repeat                   : QOpenGLTexture.WrapMode = ... # 0x2901
        ClampToBorder            : QOpenGLTexture.WrapMode = ... # 0x812d
        ClampToEdge              : QOpenGLTexture.WrapMode = ... # 0x812f
        MirroredRepeat           : QOpenGLTexture.WrapMode = ... # 0x8370

    @typing.overload
    def __init__(self, image:PySide6.QtGui.QImage, genMipMaps:PySide6.QtOpenGL.QOpenGLTexture.MipMapGeneration=...) -> None: ...
    @typing.overload
    def __init__(self, target:PySide6.QtOpenGL.QOpenGLTexture.Target) -> None: ...

    @typing.overload
    def allocateStorage(self) -> None: ...
    @typing.overload
    def allocateStorage(self, pixelFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, pixelType:PySide6.QtOpenGL.QOpenGLTexture.PixelType) -> None: ...
    @typing.overload
    def bind(self) -> None: ...
    @typing.overload
    def bind(self, unit:int, reset:PySide6.QtOpenGL.QOpenGLTexture.TextureUnitReset=...) -> None: ...
    def borderColor(self) -> PySide6.QtGui.QColor: ...
    @typing.overload
    @staticmethod
    def boundTextureId(target:PySide6.QtOpenGL.QOpenGLTexture.BindingTarget) -> int: ...
    @typing.overload
    @staticmethod
    def boundTextureId(unit:int, target:PySide6.QtOpenGL.QOpenGLTexture.BindingTarget) -> int: ...
    def comparisonFunction(self) -> PySide6.QtOpenGL.QOpenGLTexture.ComparisonFunction: ...
    def comparisonMode(self) -> PySide6.QtOpenGL.QOpenGLTexture.ComparisonMode: ...
    def create(self) -> bool: ...
    def createTextureView(self, target:PySide6.QtOpenGL.QOpenGLTexture.Target, viewFormat:PySide6.QtOpenGL.QOpenGLTexture.TextureFormat, minimumMipmapLevel:int, maximumMipmapLevel:int, minimumLayer:int, maximumLayer:int) -> PySide6.QtOpenGL.QOpenGLTexture: ...
    def depth(self) -> int: ...
    def depthStencilMode(self) -> PySide6.QtOpenGL.QOpenGLTexture.DepthStencilMode: ...
    def destroy(self) -> None: ...
    def faces(self) -> int: ...
    def format(self) -> PySide6.QtOpenGL.QOpenGLTexture.TextureFormat: ...
    @typing.overload
    def generateMipMaps(self) -> None: ...
    @typing.overload
    def generateMipMaps(self, baseLevel:int, resetBaseLevel:bool=...) -> None: ...
    @staticmethod
    def hasFeature(feature:PySide6.QtOpenGL.QOpenGLTexture.Feature) -> bool: ...
    def height(self) -> int: ...
    def isAutoMipMapGenerationEnabled(self) -> bool: ...
    @typing.overload
    def isBound(self) -> bool: ...
    @typing.overload
    def isBound(self, unit:int) -> bool: ...
    def isCreated(self) -> bool: ...
    def isFixedSamplePositions(self) -> bool: ...
    def isStorageAllocated(self) -> bool: ...
    def isTextureView(self) -> bool: ...
    def layers(self) -> int: ...
    def levelOfDetailRange(self) -> typing.Tuple: ...
    def levelofDetailBias(self) -> float: ...
    def magnificationFilter(self) -> PySide6.QtOpenGL.QOpenGLTexture.Filter: ...
    def maximumAnisotropy(self) -> float: ...
    def maximumLevelOfDetail(self) -> float: ...
    def maximumMipLevels(self) -> int: ...
    def minMagFilters(self) -> typing.Tuple: ...
    def minificationFilter(self) -> PySide6.QtOpenGL.QOpenGLTexture.Filter: ...
    def minimumLevelOfDetail(self) -> float: ...
    def mipBaseLevel(self) -> int: ...
    def mipLevelRange(self) -> typing.Tuple: ...
    def mipLevels(self) -> int: ...
    def mipMaxLevel(self) -> int: ...
    @typing.overload
    def release(self) -> None: ...
    @typing.overload
    def release(self, unit:int, reset:PySide6.QtOpenGL.QOpenGLTexture.TextureUnitReset=...) -> None: ...
    def samples(self) -> int: ...
    def setAutoMipMapGenerationEnabled(self, enabled:bool) -> None: ...
    @typing.overload
    def setBorderColor(self, color:PySide6.QtGui.QColor) -> None: ...
    @typing.overload
    def setBorderColor(self, r:float, g:float, b:float, a:float) -> None: ...
    @typing.overload
    def setBorderColor(self, r:int, g:int, b:int, a:int) -> None: ...
    @typing.overload
    def setBorderColor(self, r:int, g:int, b:int, a:int) -> None: ...
    def setComparisonFunction(self, function:PySide6.QtOpenGL.QOpenGLTexture.ComparisonFunction) -> None: ...
    def setComparisonMode(self, mode:PySide6.QtOpenGL.QOpenGLTexture.ComparisonMode) -> None: ...
    @typing.overload
    def setCompressedData(self, dataSize:int, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setCompressedData(self, mipLevel:int, dataSize:int, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setCompressedData(self, mipLevel:int, layer:int, cubeFace:PySide6.QtOpenGL.QOpenGLTexture.CubeMapFace, dataSize:int, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setCompressedData(self, mipLevel:int, layer:int, dataSize:int, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setCompressedData(self, mipLevel:int, layer:int, layerCount:int, cubeFace:PySide6.QtOpenGL.QOpenGLTexture.CubeMapFace, dataSize:int, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, image:PySide6.QtGui.QImage, genMipMaps:PySide6.QtOpenGL.QOpenGLTexture.MipMapGeneration=...) -> None: ...
    @typing.overload
    def setData(self, mipLevel:int, layer:int, cubeFace:PySide6.QtOpenGL.QOpenGLTexture.CubeMapFace, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, mipLevel:int, layer:int, layerCount:int, cubeFace:PySide6.QtOpenGL.QOpenGLTexture.CubeMapFace, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, mipLevel:int, layer:int, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, mipLevel:int, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, layer:int, cubeFace:PySide6.QtOpenGL.QOpenGLTexture.CubeMapFace, layerCount:int, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, layer:int, cubeFace:PySide6.QtOpenGL.QOpenGLTexture.CubeMapFace, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, layer:int, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, mipLevel:int, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    @typing.overload
    def setData(self, xOffset:int, yOffset:int, zOffset:int, width:int, height:int, depth:int, sourceFormat:PySide6.QtOpenGL.QOpenGLTexture.PixelFormat, sourceType:PySide6.QtOpenGL.QOpenGLTexture.PixelType, data:int, options:typing.Optional[PySide6.QtOpenGL.QOpenGLPixelTransferOptions]=...) -> None: ...
    def setDepthStencilMode(self, mode:PySide6.QtOpenGL.QOpenGLTexture.DepthStencilMode) -> None: ...
    def setFixedSamplePositions(self, fixed:bool) -> None: ...
    def setFormat(self, format:PySide6.QtOpenGL.QOpenGLTexture.TextureFormat) -> None: ...
    def setLayers(self, layers:int) -> None: ...
    def setLevelOfDetailRange(self, min:float, max:float) -> None: ...
    def setLevelofDetailBias(self, bias:float) -> None: ...
    def setMagnificationFilter(self, filter:PySide6.QtOpenGL.QOpenGLTexture.Filter) -> None: ...
    def setMaximumAnisotropy(self, anisotropy:float) -> None: ...
    def setMaximumLevelOfDetail(self, value:float) -> None: ...
    def setMinMagFilters(self, minificationFilter:PySide6.QtOpenGL.QOpenGLTexture.Filter, magnificationFilter:PySide6.QtOpenGL.QOpenGLTexture.Filter) -> None: ...
    def setMinificationFilter(self, filter:PySide6.QtOpenGL.QOpenGLTexture.Filter) -> None: ...
    def setMinimumLevelOfDetail(self, value:float) -> None: ...
    def setMipBaseLevel(self, baseLevel:int) -> None: ...
    def setMipLevelRange(self, baseLevel:int, maxLevel:int) -> None: ...
    def setMipLevels(self, levels:int) -> None: ...
    def setMipMaxLevel(self, maxLevel:int) -> None: ...
    def setSamples(self, samples:int) -> None: ...
    def setSize(self, width:int, height:int=..., depth:int=...) -> None: ...
    @typing.overload
    def setSwizzleMask(self, component:PySide6.QtOpenGL.QOpenGLTexture.SwizzleComponent, value:PySide6.QtOpenGL.QOpenGLTexture.SwizzleValue) -> None: ...
    @typing.overload
    def setSwizzleMask(self, r:PySide6.QtOpenGL.QOpenGLTexture.SwizzleValue, g:PySide6.QtOpenGL.QOpenGLTexture.SwizzleValue, b:PySide6.QtOpenGL.QOpenGLTexture.SwizzleValue, a:PySide6.QtOpenGL.QOpenGLTexture.SwizzleValue) -> None: ...
    @typing.overload
    def setWrapMode(self, direction:PySide6.QtOpenGL.QOpenGLTexture.CoordinateDirection, mode:PySide6.QtOpenGL.QOpenGLTexture.WrapMode) -> None: ...
    @typing.overload
    def setWrapMode(self, mode:PySide6.QtOpenGL.QOpenGLTexture.WrapMode) -> None: ...
    def swizzleMask(self, component:PySide6.QtOpenGL.QOpenGLTexture.SwizzleComponent) -> PySide6.QtOpenGL.QOpenGLTexture.SwizzleValue: ...
    def target(self) -> PySide6.QtOpenGL.QOpenGLTexture.Target: ...
    def textureId(self) -> int: ...
    def width(self) -> int: ...
    def wrapMode(self, direction:PySide6.QtOpenGL.QOpenGLTexture.CoordinateDirection) -> PySide6.QtOpenGL.QOpenGLTexture.WrapMode: ...


class QOpenGLTextureBlitter(Shiboken.Object):
    OriginBottomLeft         : QOpenGLTextureBlitter.Origin = ... # 0x0
    OriginTopLeft            : QOpenGLTextureBlitter.Origin = ... # 0x1

    class Origin(Shiboken.Enum):
        OriginBottomLeft         : QOpenGLTextureBlitter.Origin = ... # 0x0
        OriginTopLeft            : QOpenGLTextureBlitter.Origin = ... # 0x1

    def __init__(self) -> None: ...

    def bind(self, target:int=...) -> None: ...
    @typing.overload
    def blit(self, texture:int, targetTransform:PySide6.QtGui.QMatrix4x4, sourceOrigin:PySide6.QtOpenGL.QOpenGLTextureBlitter.Origin) -> None: ...
    @typing.overload
    def blit(self, texture:int, targetTransform:PySide6.QtGui.QMatrix4x4, sourceTransform:PySide6.QtGui.QMatrix3x3) -> None: ...
    def create(self) -> bool: ...
    def destroy(self) -> None: ...
    def isCreated(self) -> bool: ...
    def release(self) -> None: ...
    def setOpacity(self, opacity:float) -> None: ...
    def setRedBlueSwizzle(self, swizzle:bool) -> None: ...
    @staticmethod
    def sourceTransform(subTexture:PySide6.QtCore.QRectF, textureSize:PySide6.QtCore.QSize, origin:PySide6.QtOpenGL.QOpenGLTextureBlitter.Origin) -> PySide6.QtGui.QMatrix3x3: ...
    def supportsExternalOESTarget(self) -> bool: ...
    @staticmethod
    def targetTransform(target:PySide6.QtCore.QRectF, viewport:PySide6.QtCore.QRect) -> PySide6.QtGui.QMatrix4x4: ...


class QOpenGLTimeMonitor(PySide6.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def create(self) -> bool: ...
    def destroy(self) -> None: ...
    def isCreated(self) -> bool: ...
    def isResultAvailable(self) -> bool: ...
    def objectIds(self) -> typing.List: ...
    def recordSample(self) -> int: ...
    def reset(self) -> None: ...
    def sampleCount(self) -> int: ...
    def setSampleCount(self, sampleCount:int) -> None: ...
    def waitForIntervals(self) -> typing.List: ...
    def waitForSamples(self) -> typing.List: ...


class QOpenGLTimerQuery(PySide6.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def begin(self) -> None: ...
    def create(self) -> bool: ...
    def destroy(self) -> None: ...
    def end(self) -> None: ...
    def isCreated(self) -> bool: ...
    def isResultAvailable(self) -> bool: ...
    def objectId(self) -> int: ...
    def recordTimestamp(self) -> None: ...
    def waitForResult(self) -> int: ...
    def waitForTimestamp(self) -> int: ...


class QOpenGLVersionProfile(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, format:PySide6.QtGui.QSurfaceFormat) -> None: ...
    @typing.overload
    def __init__(self, other:PySide6.QtOpenGL.QOpenGLVersionProfile) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def hasProfiles(self) -> bool: ...
    def isLegacyVersion(self) -> bool: ...
    def isValid(self) -> bool: ...
    def profile(self) -> PySide6.QtGui.QSurfaceFormat.OpenGLContextProfile: ...
    def setProfile(self, profile:PySide6.QtGui.QSurfaceFormat.OpenGLContextProfile) -> None: ...
    def setVersion(self, majorVersion:int, minorVersion:int) -> None: ...
    def version(self) -> typing.Tuple: ...


class QOpenGLVertexArrayObject(PySide6.QtCore.QObject):

    class Binder(Shiboken.Object):

        def __init__(self, v:PySide6.QtOpenGL.QOpenGLVertexArrayObject) -> None: ...

        def rebind(self) -> None: ...
        def release(self) -> None: ...

    def __init__(self, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def bind(self) -> None: ...
    def create(self) -> bool: ...
    def destroy(self) -> None: ...
    def isCreated(self) -> bool: ...
    def objectId(self) -> int: ...
    def release(self) -> None: ...


class QOpenGLWindow(PySide6.QtGui.QPaintDeviceWindow):
    NoPartialUpdate          : QOpenGLWindow.UpdateBehavior = ... # 0x0
    PartialUpdateBlit        : QOpenGLWindow.UpdateBehavior = ... # 0x1
    PartialUpdateBlend       : QOpenGLWindow.UpdateBehavior = ... # 0x2

    class UpdateBehavior(Shiboken.Enum):
        NoPartialUpdate          : QOpenGLWindow.UpdateBehavior = ... # 0x0
        PartialUpdateBlit        : QOpenGLWindow.UpdateBehavior = ... # 0x1
        PartialUpdateBlend       : QOpenGLWindow.UpdateBehavior = ... # 0x2

    @typing.overload
    def __init__(self, shareContext:PySide6.QtGui.QOpenGLContext, updateBehavior:PySide6.QtOpenGL.QOpenGLWindow.UpdateBehavior=..., parent:typing.Optional[PySide6.QtGui.QWindow]=...) -> None: ...
    @typing.overload
    def __init__(self, updateBehavior:PySide6.QtOpenGL.QOpenGLWindow.UpdateBehavior=..., parent:typing.Optional[PySide6.QtGui.QWindow]=...) -> None: ...

    def context(self) -> PySide6.QtGui.QOpenGLContext: ...
    def defaultFramebufferObject(self) -> int: ...
    def doneCurrent(self) -> None: ...
    def grabFramebuffer(self) -> PySide6.QtGui.QImage: ...
    def initializeGL(self) -> None: ...
    def isValid(self) -> bool: ...
    def makeCurrent(self) -> None: ...
    def metric(self, metric:PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def paintEvent(self, event:PySide6.QtGui.QPaintEvent) -> None: ...
    def paintGL(self) -> None: ...
    def paintOverGL(self) -> None: ...
    def paintUnderGL(self) -> None: ...
    def redirected(self, arg__1:PySide6.QtCore.QPoint) -> PySide6.QtGui.QPaintDevice: ...
    def resizeEvent(self, event:PySide6.QtGui.QResizeEvent) -> None: ...
    def resizeGL(self, w:int, h:int) -> None: ...
    def shareContext(self) -> PySide6.QtGui.QOpenGLContext: ...
    def updateBehavior(self) -> PySide6.QtOpenGL.QOpenGLWindow.UpdateBehavior: ...

# eof
