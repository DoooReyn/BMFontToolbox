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
PySide6.QtTest, except for defaults which are replaced by "...".
"""

# Module PySide6.QtTest
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
import PySide6.QtWidgets
import PySide6.QtTest


class QAbstractItemModelTester(PySide6.QtCore.QObject):

    class FailureReportingMode(Shiboken.Enum):
        QtTest                   : QAbstractItemModelTester.FailureReportingMode = ... # 0x0
        Warning                  : QAbstractItemModelTester.FailureReportingMode = ... # 0x1
        Fatal                    : QAbstractItemModelTester.FailureReportingMode = ... # 0x2

    @typing.overload
    def __init__(self, model:PySide6.QtCore.QAbstractItemModel, mode:PySide6.QtTest.QAbstractItemModelTester.FailureReportingMode, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @typing.overload
    def __init__(self, model:PySide6.QtCore.QAbstractItemModel, parent:typing.Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def failureReportingMode(self) -> PySide6.QtTest.QAbstractItemModelTester.FailureReportingMode: ...
    def model(self) -> PySide6.QtCore.QAbstractItemModel: ...


class QTest(Shiboken.Object):
    Press                    : QTest.KeyAction = ... # 0x0
    Release                  : QTest.KeyAction = ... # 0x1
    Click                    : QTest.KeyAction = ... # 0x2
    Shortcut                 : QTest.KeyAction = ... # 0x3
    MousePress               : QTest.MouseAction = ... # 0x0
    MouseRelease             : QTest.MouseAction = ... # 0x1
    MouseClick               : QTest.MouseAction = ... # 0x2
    MouseDClick              : QTest.MouseAction = ... # 0x3
    MouseMove                : QTest.MouseAction = ... # 0x4
    FramesPerSecond          : QTest.QBenchmarkMetric = ... # 0x0
    BitsPerSecond            : QTest.QBenchmarkMetric = ... # 0x1
    BytesPerSecond           : QTest.QBenchmarkMetric = ... # 0x2
    WalltimeMilliseconds     : QTest.QBenchmarkMetric = ... # 0x3
    CPUTicks                 : QTest.QBenchmarkMetric = ... # 0x4
    InstructionReads         : QTest.QBenchmarkMetric = ... # 0x5
    Events                   : QTest.QBenchmarkMetric = ... # 0x6
    WalltimeNanoseconds      : QTest.QBenchmarkMetric = ... # 0x7
    BytesAllocated           : QTest.QBenchmarkMetric = ... # 0x8
    CPUMigrations            : QTest.QBenchmarkMetric = ... # 0x9
    CPUCycles                : QTest.QBenchmarkMetric = ... # 0xa
    BusCycles                : QTest.QBenchmarkMetric = ... # 0xb
    StalledCycles            : QTest.QBenchmarkMetric = ... # 0xc
    Instructions             : QTest.QBenchmarkMetric = ... # 0xd
    BranchInstructions       : QTest.QBenchmarkMetric = ... # 0xe
    BranchMisses             : QTest.QBenchmarkMetric = ... # 0xf
    CacheReferences          : QTest.QBenchmarkMetric = ... # 0x10
    CacheReads               : QTest.QBenchmarkMetric = ... # 0x11
    CacheWrites              : QTest.QBenchmarkMetric = ... # 0x12
    CachePrefetches          : QTest.QBenchmarkMetric = ... # 0x13
    CacheMisses              : QTest.QBenchmarkMetric = ... # 0x14
    CacheReadMisses          : QTest.QBenchmarkMetric = ... # 0x15
    CacheWriteMisses         : QTest.QBenchmarkMetric = ... # 0x16
    CachePrefetchMisses      : QTest.QBenchmarkMetric = ... # 0x17
    ContextSwitches          : QTest.QBenchmarkMetric = ... # 0x18
    PageFaults               : QTest.QBenchmarkMetric = ... # 0x19
    MinorPageFaults          : QTest.QBenchmarkMetric = ... # 0x1a
    MajorPageFaults          : QTest.QBenchmarkMetric = ... # 0x1b
    AlignmentFaults          : QTest.QBenchmarkMetric = ... # 0x1c
    EmulationFaults          : QTest.QBenchmarkMetric = ... # 0x1d
    RefCPUCycles             : QTest.QBenchmarkMetric = ... # 0x1e
    Abort                    : QTest.TestFailMode = ... # 0x1
    Continue                 : QTest.TestFailMode = ... # 0x2

    class KeyAction(Shiboken.Enum):
        Press                    : QTest.KeyAction = ... # 0x0
        Release                  : QTest.KeyAction = ... # 0x1
        Click                    : QTest.KeyAction = ... # 0x2
        Shortcut                 : QTest.KeyAction = ... # 0x3

    class MouseAction(Shiboken.Enum):
        MousePress               : QTest.MouseAction = ... # 0x0
        MouseRelease             : QTest.MouseAction = ... # 0x1
        MouseClick               : QTest.MouseAction = ... # 0x2
        MouseDClick              : QTest.MouseAction = ... # 0x3
        MouseMove                : QTest.MouseAction = ... # 0x4

    class QBenchmarkMetric(Shiboken.Enum):
        FramesPerSecond          : QTest.QBenchmarkMetric = ... # 0x0
        BitsPerSecond            : QTest.QBenchmarkMetric = ... # 0x1
        BytesPerSecond           : QTest.QBenchmarkMetric = ... # 0x2
        WalltimeMilliseconds     : QTest.QBenchmarkMetric = ... # 0x3
        CPUTicks                 : QTest.QBenchmarkMetric = ... # 0x4
        InstructionReads         : QTest.QBenchmarkMetric = ... # 0x5
        Events                   : QTest.QBenchmarkMetric = ... # 0x6
        WalltimeNanoseconds      : QTest.QBenchmarkMetric = ... # 0x7
        BytesAllocated           : QTest.QBenchmarkMetric = ... # 0x8
        CPUMigrations            : QTest.QBenchmarkMetric = ... # 0x9
        CPUCycles                : QTest.QBenchmarkMetric = ... # 0xa
        BusCycles                : QTest.QBenchmarkMetric = ... # 0xb
        StalledCycles            : QTest.QBenchmarkMetric = ... # 0xc
        Instructions             : QTest.QBenchmarkMetric = ... # 0xd
        BranchInstructions       : QTest.QBenchmarkMetric = ... # 0xe
        BranchMisses             : QTest.QBenchmarkMetric = ... # 0xf
        CacheReferences          : QTest.QBenchmarkMetric = ... # 0x10
        CacheReads               : QTest.QBenchmarkMetric = ... # 0x11
        CacheWrites              : QTest.QBenchmarkMetric = ... # 0x12
        CachePrefetches          : QTest.QBenchmarkMetric = ... # 0x13
        CacheMisses              : QTest.QBenchmarkMetric = ... # 0x14
        CacheReadMisses          : QTest.QBenchmarkMetric = ... # 0x15
        CacheWriteMisses         : QTest.QBenchmarkMetric = ... # 0x16
        CachePrefetchMisses      : QTest.QBenchmarkMetric = ... # 0x17
        ContextSwitches          : QTest.QBenchmarkMetric = ... # 0x18
        PageFaults               : QTest.QBenchmarkMetric = ... # 0x19
        MinorPageFaults          : QTest.QBenchmarkMetric = ... # 0x1a
        MajorPageFaults          : QTest.QBenchmarkMetric = ... # 0x1b
        AlignmentFaults          : QTest.QBenchmarkMetric = ... # 0x1c
        EmulationFaults          : QTest.QBenchmarkMetric = ... # 0x1d
        RefCPUCycles             : QTest.QBenchmarkMetric = ... # 0x1e

    class QTouchEventSequence(Shiboken.Object):
        def commit(self, processEvents:bool=...) -> None: ...
        @typing.overload
        def move(self, touchId:int, pt:PySide6.QtCore.QPoint, widget:typing.Optional[PySide6.QtWidgets.QWidget]=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @typing.overload
        def move(self, touchId:int, pt:PySide6.QtCore.QPoint, window:typing.Optional[PySide6.QtGui.QWindow]=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @typing.overload
        def press(self, touchId:int, pt:PySide6.QtCore.QPoint, widget:typing.Optional[PySide6.QtWidgets.QWidget]=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @typing.overload
        def press(self, touchId:int, pt:PySide6.QtCore.QPoint, window:typing.Optional[PySide6.QtGui.QWindow]=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @typing.overload
        def release(self, touchId:int, pt:PySide6.QtCore.QPoint, widget:typing.Optional[PySide6.QtWidgets.QWidget]=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        @typing.overload
        def release(self, touchId:int, pt:PySide6.QtCore.QPoint, window:typing.Optional[PySide6.QtGui.QWindow]=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
        def stationary(self, touchId:int) -> PySide6.QtTest.QTest.QTouchEventSequence: ...

    class TestFailMode(Shiboken.Enum):
        Abort                    : QTest.TestFailMode = ... # 0x1
        Continue                 : QTest.TestFailMode = ... # 0x2
    @staticmethod
    def addColumnInternal(id:int, name:bytes) -> None: ...
    @staticmethod
    def asciiToKey(ascii:int) -> PySide6.QtCore.Qt.Key: ...
    @staticmethod
    def compare_ptr_helper(t1:int, t2:int, actual:bytes, expected:bytes, file:bytes, line:int) -> bool: ...
    @staticmethod
    def compare_string_helper(t1:bytes, t2:bytes, actual:bytes, expected:bytes, file:bytes, line:int) -> bool: ...
    @staticmethod
    def createTouchDevice(devType:PySide6.QtGui.QInputDevice.DeviceType=..., caps:PySide6.QtGui.QInputDevice.Capabilities=...) -> PySide6.QtGui.QPointingDevice: ...
    @staticmethod
    def currentAppName() -> bytes: ...
    @staticmethod
    def currentDataTag() -> bytes: ...
    @staticmethod
    def currentTestFailed() -> bool: ...
    @staticmethod
    def currentTestFunction() -> bytes: ...
    @staticmethod
    def formatString(prefix:bytes, suffix:bytes, numArguments:int) -> bytes: ...
    @typing.overload
    @staticmethod
    def ignoreMessage(type:PySide6.QtCore.QtMsgType, message:bytes) -> None: ...
    @typing.overload
    @staticmethod
    def ignoreMessage(type:PySide6.QtCore.QtMsgType, messagePattern:PySide6.QtCore.QRegularExpression) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(widget:PySide6.QtWidgets.QWidget, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(widget:PySide6.QtWidgets.QWidget, key:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(window:PySide6.QtGui.QWindow, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyClick(window:PySide6.QtGui.QWindow, key:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @staticmethod
    def keyClicks(widget:PySide6.QtWidgets.QWidget, sequence:str, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action:PySide6.QtTest.QTest.KeyAction, widget:PySide6.QtWidgets.QWidget, ascii:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action:PySide6.QtTest.QTest.KeyAction, widget:PySide6.QtWidgets.QWidget, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action:PySide6.QtTest.QTest.KeyAction, window:PySide6.QtGui.QWindow, ascii:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyEvent(action:PySide6.QtTest.QTest.KeyAction, window:PySide6.QtGui.QWindow, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyPress(widget:PySide6.QtWidgets.QWidget, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyPress(widget:PySide6.QtWidgets.QWidget, key:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyPress(window:PySide6.QtGui.QWindow, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyPress(window:PySide6.QtGui.QWindow, key:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(widget:PySide6.QtWidgets.QWidget, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(widget:PySide6.QtWidgets.QWidget, key:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(window:PySide6.QtGui.QWindow, key:PySide6.QtCore.Qt.Key, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keyRelease(window:PySide6.QtGui.QWindow, key:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def keySequence(widget:PySide6.QtWidgets.QWidget, keySequence:PySide6.QtGui.QKeySequence) -> None: ...
    @typing.overload
    @staticmethod
    def keySequence(window:PySide6.QtGui.QWindow, keySequence:PySide6.QtGui.QKeySequence) -> None: ...
    @staticmethod
    def keyToAscii(key:PySide6.QtCore.Qt.Key) -> int: ...
    @typing.overload
    @staticmethod
    def mouseClick(widget:PySide6.QtWidgets.QWidget, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseClick(window:PySide6.QtGui.QWindow, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseDClick(widget:PySide6.QtWidgets.QWidget, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseDClick(window:PySide6.QtGui.QWindow, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseEvent(action:PySide6.QtTest.QTest.MouseAction, widget:PySide6.QtWidgets.QWidget, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers, pos:PySide6.QtCore.QPoint, delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseEvent(action:PySide6.QtTest.QTest.MouseAction, window:PySide6.QtGui.QWindow, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers, pos:PySide6.QtCore.QPoint, delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseMove(widget:PySide6.QtWidgets.QWidget, pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseMove(window:PySide6.QtGui.QWindow, pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mousePress(widget:PySide6.QtWidgets.QWidget, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mousePress(window:PySide6.QtGui.QWindow, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseRelease(widget:PySide6.QtWidgets.QWidget, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def mouseRelease(window:PySide6.QtGui.QWindow, button:PySide6.QtCore.Qt.MouseButton, stateKey:PySide6.QtCore.Qt.KeyboardModifiers=..., pos:PySide6.QtCore.QPoint=..., delay:int=...) -> None: ...
    @staticmethod
    def qCleanup() -> None: ...
    @staticmethod
    def qElementData(elementName:bytes, metaTypeId:int) -> int: ...
    @staticmethod
    def qExpectFail(dataIndex:bytes, comment:bytes, mode:PySide6.QtTest.QTest.TestFailMode, file:bytes, line:int) -> bool: ...
    @typing.overload
    @staticmethod
    def qFindTestData(basepath:str, file:typing.Optional[bytes]=..., line:int=..., builddir:typing.Optional[bytes]=..., sourcedir:typing.Optional[bytes]=...) -> str: ...
    @typing.overload
    @staticmethod
    def qFindTestData(basepath:bytes, file:typing.Optional[bytes]=..., line:int=..., builddir:typing.Optional[bytes]=..., sourcedir:typing.Optional[bytes]=...) -> str: ...
    @staticmethod
    def qGlobalData(tagName:bytes, typeId:int) -> int: ...
    @staticmethod
    def qRun() -> int: ...
    @staticmethod
    def qSkip(message:bytes, file:bytes, line:int) -> None: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowActive(widget:PySide6.QtWidgets.QWidget, timeout:int=...) -> bool: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowActive(window:PySide6.QtGui.QWindow, timeout:int=...) -> bool: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowExposed(widget:PySide6.QtWidgets.QWidget, timeout:int=...) -> bool: ...
    @typing.overload
    @staticmethod
    def qWaitForWindowExposed(window:PySide6.QtGui.QWindow, timeout:int=...) -> bool: ...
    @typing.overload
    @staticmethod
    def sendKeyEvent(action:PySide6.QtTest.QTest.KeyAction, widget:PySide6.QtWidgets.QWidget, code:PySide6.QtCore.Qt.Key, ascii:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers, delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def sendKeyEvent(action:PySide6.QtTest.QTest.KeyAction, widget:PySide6.QtWidgets.QWidget, code:PySide6.QtCore.Qt.Key, text:str, modifier:PySide6.QtCore.Qt.KeyboardModifiers, delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def sendKeyEvent(action:PySide6.QtTest.QTest.KeyAction, window:PySide6.QtGui.QWindow, code:PySide6.QtCore.Qt.Key, ascii:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers, delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def sendKeyEvent(action:PySide6.QtTest.QTest.KeyAction, window:PySide6.QtGui.QWindow, code:PySide6.QtCore.Qt.Key, text:str, modifier:PySide6.QtCore.Qt.KeyboardModifiers, delay:int=...) -> None: ...
    @staticmethod
    def setBenchmarkResult(result:float, metric:PySide6.QtTest.QTest.QBenchmarkMetric) -> None: ...
    @staticmethod
    def setMainSourcePath(file:bytes, builddir:typing.Optional[bytes]=...) -> None: ...
    @typing.overload
    @staticmethod
    def simulateEvent(widget:PySide6.QtWidgets.QWidget, press:bool, code:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers, text:str, repeat:bool, delay:int=...) -> None: ...
    @typing.overload
    @staticmethod
    def simulateEvent(window:PySide6.QtGui.QWindow, press:bool, code:int, modifier:PySide6.QtCore.Qt.KeyboardModifiers, text:str, repeat:bool, delay:int=...) -> None: ...
    @staticmethod
    def testObject() -> PySide6.QtCore.QObject: ...
    @staticmethod
    def toPrettyCString(unicode:bytes, length:int) -> bytes: ...
    @typing.overload
    @staticmethod
    def touchEvent(widget:PySide6.QtWidgets.QWidget, device:PySide6.QtGui.QPointingDevice, autoCommit:bool=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...
    @typing.overload
    @staticmethod
    def touchEvent(window:PySide6.QtGui.QWindow, device:PySide6.QtGui.QPointingDevice, autoCommit:bool=...) -> PySide6.QtTest.QTest.QTouchEventSequence: ...

# eof
