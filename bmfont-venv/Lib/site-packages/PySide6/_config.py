built_modules = list(name for name in
    "Core;Gui;Widgets;PrintSupport;Sql;Network;Test;Concurrent;Xml;Help;OpenGL;OpenGLFunctions;OpenGLWidgets;Qml;Quick;QuickControls2;QuickWidgets;Svg;SvgWidgets;UiTools;3DCore;3DRender;3DInput;3DLogic;3DAnimation;3DExtras"
    .split(";"))

shiboken_library_soversion = str(6.0)
pyside_library_soversion = str(6.0)

version = "6.0.2"
version_info = (6, 0, 2, "", "")

__build_date__ = '2021-03-04T19:00:11+00:00'




__setup_py_package_version__ = '6.0.2'
