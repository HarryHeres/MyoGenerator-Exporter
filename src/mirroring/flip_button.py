### General modules ###
from ..strings.ids import ids
from ..strings.descriptions import descriptions
from ..strings.labels import labels

### Blender modules ###
import bpy
from bpy.types import Operator

class MirrorButton(Operator):
    bl_idname =  ids["FlipButton_bl_idname"]
    bl_description = descriptions["FlipButton_bl_description"]
    bl_label = labels["FlipButton_bl_label"]
    

    @classmethod
    def poll(cls, context):
        return True
    
    def mirror(self):
        mirror_x = -1.0 if bpy.context.scene.mirror_x == True else 1.0
        mirror_y = -1.0 if bpy.context.scene.mirror_y == True else 1.0
        mirror_z = -1.0 if bpy.context.scene.mirror_z == True else 1.0

        if(len(bpy.context.selected_objects) == 0):
            return
        
        for obj in bpy.context.selected_objects:
            flipped = obj.copy()

            if("right" in flipped.name):
                flipped.name =  obj.name[0:len(obj.name) - len("right")] + " left"
            else:
                flipped.name =  obj.name[0:len(obj.name) - len("left")] + " right"
            bpy.ops.object.add_named(name=flipped.name)
            bpy.context.active_object.scale = (mirror_x, mirror_y, mirror_z)

    def execute(self, context):
        self.mirror()
        return {"FINISHED"}
        
