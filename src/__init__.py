### General libraries ###
from .main_gui.panel import MainPanel
from .main_gui.decompose_button import DecomposeButton
from .main_gui.export_button import ExportButton

### Blender libraries ###
import bpy
from bpy.utils import register_class, unregister_class

_props = []
'''
Add-on properties
'''

_classes = [MainPanel, DecomposeButton, ExportButton]
'''
Add-on classes
'''

bl_info = {
 "name": "MyoGenerator Exporter",
 "description": "Addon used for exporting muscle models created by the Myogenerator, decomposing them into muscle fibers using 3rd party software and then importing them back to Blender",
 "author": "Jan Hereš (www.janheres.eu)",
 "blender": (2, 93, 0),
 "version": (1, 0, 1),
 "warning": "Only officially supported for versions 2.91.X - 2.93.X of Blender!",
 "category": "Export",
}
'''
Add-on info in Edit -> Preferences -> Add-ons
'''

def register():
    register_classes()
    register_props()

def register_classes():
    global _classes

    for cls in _classes:
        register_class(cls)


def register_props():
    bpy.types.Scene.output_path = bpy.props.StringProperty(
        name = "Output path (folder)",
        default = "",
        description = "Select where to save your file...",
        subtype = "DIR_PATH"
    )

    bpy.types.Scene.muscle_name = bpy.props.StringProperty(
        name = "Muscle name",
        default = "",
        description = "Filename of the muscle to decompose (without the file format)",
        subtype = "FILE_NAME"
    )

    bpy.types.Scene.export_fibres = bpy.props.IntProperty(
        name = "Number of fibres",
        default = 10,
        description = "Desired number of muscle fibres to decompose into",
        subtype = "UNSIGNED",
        min = 1,
        step = 1,
        soft_max = 100 # Only for the slider
    )

    bpy.types.Scene.export_resolution = bpy.props.IntProperty(
        name = "Fiber resolution",
        default = 15,
        description = "Desired resolution of the produced fibres",
        subtype = "UNSIGNED",
        min = 1,
        step = 1,
        soft_max = 100, 
    )

    bpy.types.Scene.export_visualize = bpy.props.EnumProperty(
        name = "Visualization mode",
        items = [("0", "None", "No visualization", 0), 
                 ("1", "Visualize", "Standard visualization in a separate window", 1), 
                 ("2", "Debug", "Visualization mainly for debugging purposes", 2)
                ],
        default = 0,
    )

    _props.append(bpy.types.Scene.output_path)
    _props.append(bpy.types.Scene.muscle_name)
    _props.append(bpy.types.Scene.export_fibres)
    _props.append(bpy.types.Scene.export_resolution)
    _props.append(bpy.types.Scene.export_visualize)


def unregister():
    for cls in _classes:
        unregister_class(cls)
    
    for prop in _props:
        del prop


if __name__ == "__main__":
    register()
