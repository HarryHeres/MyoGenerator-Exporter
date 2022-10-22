### General libraries ###
from .main_gui.panel import MainPanel
from .main_gui.decompose_button import DecomposeButton
from .main_gui.export_button import ExportButton
from .mirroring.flip_button import FlipButton
from .mirroring.mirror_menu import MirrorMenu
from .strings.keymaps import keymaps

### Blender libraries ###
import bpy
from bpy.utils import register_class, unregister_class

_props = []
'''
Add-on properties
'''


_classes = [MainPanel, DecomposeButton, ExportButton, FlipButton, MirrorMenu]
'''
Add-on classes
'''

_keymaps_list = []

# _modules = ["debugpy"]
# '''
# Add-on essential modules
# '''


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
    register_keymaps()

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

def register_keymaps():
    global _keymaps_list

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    for keymap_group_name in keymaps:
        keylist = keymaps[keymap_group_name]

        for list_item in keylist:
            menu_name = list_item.get("menu_name")
            space_type = list_item.get("space_type", "EMPTY")
            region_type = list_item.get("region_type", "WINDOW")

            if list_item:
                km = kc.keymaps.new(menu_name, space_type=space_type, region_type=region_type)

                if km:
                    action = list_item.get("action")
                    idname = list_item.get("idname")
                    type = list_item.get("type")
                    value = list_item.get("value")

                    shift = list_item.get("shift", False)
                    ctrl = list_item.get("ctrl", False)
                    alt = list_item.get("alt", False)
                    oskey = list_item.get("oskey", False)

                    kmi = km.keymap_items.new(action, type, value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

                    if kmi:
                        kmi.properties.name = idname
                _keymaps_list.append(km)

    # Mirroring keymap group 
    # km = wm.keyconfigs.addon.keymaps.new("Window", space_type="EMPTY", region_type="WINDOW")

    # # Particular key shortcuts
    # kmi = km.keymap_items.new("wm.call_menu", type="F5", value="PRESS")
    # kmi.properties.name = MirrorMenu.bl_idname
    # _keymaps_list.append(km)


def unregister_keymaps():
    global _keymaps_list

    wm = bpy.context.window_manager

    for km in _keymaps_list:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
    _keymaps_list.clear()


def unregister():
    for cls in _classes:
        unregister_class(cls)
    
    for prop in _props:
        del prop

    unregister_keymaps()


# DEPRECATED
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
