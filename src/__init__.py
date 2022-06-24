### General libraries ###
# import pip # NOT NEEDED FOR THIS VERSION

### Blender libraries ###
import bpy
from bpy.utils import register_class, unregister_class

_props = []
'''
Add-on properties
'''

_classes = []

# _modules = ["debugpy"]
# '''
# Add-on essential modules
# '''


bl_info = {
 "name": "MyoGenerator Exporter",
 "description": "Addon used for exporting muscle models created by the Myogenerator, decomposing them into muscle fibers using 3rd party software and then importing them back to Blender",
 "author": "Jan Heres",
 "blender": (2, 91, 0),
 "version": (0, 0, 1),
 "warning": "Only officially supported for versions 2.93.X of Blender!",
 "category": "Export",
}
'''
Add-on info in Edit -> Preferences -> Add-ons
'''

def register():
    global _classes

    # install_modules() # Making sure the essential modules are installed - NOT NEEDED IN THIS VERSION

    # NOTE: Have to import the add-on's classes AFTER the essential modules are installed
    from .addon_panel import MainPanel
    from .addon_decompose_button import DecomposeButton
    from .addon_export_button import ExportButton
    
    _classes = [MainPanel, DecomposeButton, ExportButton]

    for cls in _classes:
        register_class(cls)

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

    bpy.types.Scene.export_visualize = bpy.props.IntProperty(
        name = "Visualization mode",
        default = 0,
        description = "Visualization mode: 0 = none, 1 = vizualize, 2 = debug",
        subtype = "UNSIGNED",
        min = 0,
        max = 2,
        step = 1,
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


# NOT NEEDED FOR THIS VERSION
# '''
# Installing all dependent modules
# '''
# def install_modules():
#     # try:
#     #     # Version 2.92 and older
#     #     python_path = bpy.app.binary_path_python
#     # except AttributeError:
#     #     # Version 2.93 and later
#     #     python_path = sys.executable
    
#     for module in _modules:
#     #     cmd = [
#     #         os.path.abspath(python_path),
#     #         "-m" 
#     #         "pip",
#     #         "install",
#     #         module,
#     #     ]
#     #     result = subprocess.run(cmd, stdout=subprocess.PIPE)
#     #     print(result.stdout.decode("utf-8"))
#         result = pip.main(["install", module])
#         if(result == 1):
#             print("ERROR! Module \"" + module + "\" have not been found for this version of Python!")
            


if __name__ == "__main__":
    register()
