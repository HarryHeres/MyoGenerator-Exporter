### General libraries ### 
import os
import re
from .addon_popups import SimplePopup

### Blender libraries ###

# NOTE: Developing in VS CODE: Had to import the whole bpy library,
# since the Blender addon development extension is a bit older and 
# does not link the some submodules very well
import bpy
import bmesh # Blender mesh 
from bpy.types import Operator
from .strings import strings

class ExportButton(Operator):

    bl_idname = strings["ExportButton_bl_idname"]
    bl_label = strings["ExportButton_bl_label"]
    bl_description = strings["ExportButton_bl_description"]

    # Export formats supported by the MuscleDecompositionTest tool
    export_format_origin_insertion = ".vtk"
    export_format_volume = ".stl"
    type_delimiter = " "

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False


    def execute(self, context):
        if len(bpy.context.selected_objects) == 0:
            SimplePopup.showPopup(self, strings["Message_nothing_selected"], "ERROR", "ERROR")
            return {"FINISHED"}

        # For each selected object in the scene
        for obj in bpy.context.selected_objects:
            if "origin boundary" in obj.name:
                self.export_origin_insertion(obj, "origin")
            elif "insertion boundary" in obj.name:
                self.export_origin_insertion(obj, "insertion")
            elif "volume" in obj.name:
                self.export_volume(obj)
            else:
                SimplePopup.showPopup(self, strings["Message_wrong_name_format"], "ERROR", "ERROR")
                return {"FINISHED"}
            
        # Let the user now about the current state of exporting
        # NOTE: Operator defined by the bl_idname property
        SimplePopup.showPopup(self, strings["Message_exporting_finished"], "Export")
            
        return {'FINISHED'}
    

    def export_volume(self, obj) -> None:
        # For debugging purposes
        print_format = "[" + obj.name + "]: " 

        # Deselect all and the select active object based on the name
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        obj.select_set(True)

        # Apply all object transforms before exporting
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # For debugging purposes
        print_format = "[" + obj.name + "]: " 

        # Prepare the output file 
        output_dir =  bpy.path.abspath(bpy.context.scene.output_path) # User chosen output dir
        output_file = os.path.join(output_dir, obj.name.split(self.type_delimiter)[0] + self.type_delimiter + "volume" + ExportButton.export_format_volume)
        print(print_format + "Output filepath: " + output_file)

        # Export the volume as an stl mesh
        bpy.ops.export_mesh.stl(filepath=output_file, 
                                check_existing=True, 
                                filter_glob='*.stl',
                                use_selection=True, 
                                global_scale=1.0, 
                                use_scene_unit=False, 
                                ascii=False, 
                                use_mesh_modifiers=True, 
                                batch_mode='OFF', 
                                axis_forward='Y', 
                                axis_up='Z')


    def export_origin_insertion(self, obj, type) -> None:
        # For debugging purposes
        print_format = "[" + obj.name + "]: " 

        # Prepare the output file
        output_dir =  bpy.path.abspath(bpy.context.scene.output_path) # User chosen output dir
        output_file = os.path.join(output_dir, obj.name.split(self.type_delimiter)[0] + self.type_delimiter + type + ExportButton.export_format_origin_insertion)
        print(print_format + "Output filepath: " + output_file)

        # Deselect all objects
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.select_all(action = 'DESELECT')

        # Find the right object by its name and select it 
        bpy.context.view_layer.objects.active = bpy.data.objects[obj.name]
        obj.select_set(True)

        # Apply all transforms before exporting
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True) # Apply object's tranforms before exporting
        
        # Switch to edit mode (-> mesh layout)
        bpy.ops.object.mode_set(mode = 'EDIT')

        # bpy.ops.object.select_all(action = 'SELECT') 

        bpy.context.tool_settings.mesh_select_mode = (True, False, False) # Vertex selection mode
        bpy.ops.mesh.select_all(action = 'SELECT') # Select all vertices

        # Get the active mesh
        bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
        bm.faces.active = None
        pointsList = []

        for v in bm.verts:
            if v.select:
                # print(v.co)
                coords = str(tuple(v.co))
                coords = re.sub('[(),]', '', coords)
                pointsList.append(coords)
            # print(pointsList)
        pointsCount = len(pointsList)

        # --- For debugging purposes --- #
        print(print_format + "Points count: " + str(pointsCount))

        # Write out the muscle origin/insertion into a "self.export_format" format
        with open(output_file, "w") as of:
            header = str('# vtk DataFile Version 3.0\nvtk output\nASCII\nDATASET POLYDATA\nPOINTS %d float\n' %pointsCount) 
            of.write(header)
            for point in pointsList:
                of.write(point +'\n')

        # Jump back to object mode
        bpy.ops.object.mode_set(mode="OBJECT")


