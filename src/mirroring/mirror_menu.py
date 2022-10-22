### General modules ###
from .flip_button import FlipButton
from ..strings.ids import ids
from ..strings.labels import labels

### Blender modules ###
import bpy


class MirrorMenu(bpy.types.Menu):
    bl_idname = ids["MirrorMenu_bl_idname"]
    bl_label = labels["MirrorMenu_bl_label"]

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        row = box.row()
        row.operator(FlipButton.bl_idname, text=FlipButton.bl_label)
