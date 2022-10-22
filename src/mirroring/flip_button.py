### General modules ###
from ..strings.ids import ids
from ..strings.descriptions import descriptions
from ..strings.labels import labels

### Blender modules ###
import bpy
from bpy.types import Operator

class FlipButton(Operator):
    bl_idname =  ids["FlipButton_bl_idname"]
    bl_description = descriptions["FlipButton_bl_description"]
    bl_label = labels["FlipButton_bl_label"]

    @classmethod
    def poll(cls, context):
        return True
    
    def flip(self):
        selected = bpy.context.selected_objects[0]
        flipped = selected.copy()
        flipped.name = selected.name + "_flipped"
        bpy.ops.object.add_named(name = flipped.name)
        bpy.context.active_object.scale = (-1.0, 1.0, 1.0) # Mirroring  
        #TODO: Rename to right-side muscles

    def execute(self, context):
        self.flip()
        return {"FINISHED"}
        
