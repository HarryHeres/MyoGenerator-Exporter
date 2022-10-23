### General modules ###
from .flip_button import MirrorButton
from ..strings.ids import ids
from ..strings.labels import labels

### Blender modules ###
import bpy


class MirrorMenu(bpy.types.Panel):
    bl_idname = ids["MirrorMenu_bl_idname"]
    bl_label = labels["MirrorMenu_bl_label"]
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        row = box.row()
        row.prop(context.scene, "mirror_x", text="Mirror X-axis")

        row = box.row()
        row.prop(context.scene, "mirror_y", text="Mirror Y-axis")

        row = box.row()
        row.prop(context.scene, "mirror_z", text="Mirror Z-axis")

        layout.separator()

        row = box.row()
        row.operator(MirrorButton.bl_idname, text=MirrorButton.bl_label)
