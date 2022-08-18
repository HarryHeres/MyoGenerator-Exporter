### General libraries ###
import subprocess
import os
from sys import platform
from .strings import strings
from .addon_export_button import ExportButton
from .addon_popups import SimplePopup

### Blender libraries ###
import bpy
from bpy.types import Operator

class DecomposeButton(Operator):
    bl_idname = strings["DecomposeButton_bl_idname"]
    bl_label = ""
    bl_description = strings["DecomposeButton_bl_description"]
    bl_property = "type"
    mdt_format = ".obj"
    import_format = ".obj"

    type: bpy.props.StringProperty(
        name = "Decompose button type (all/specified)",
        default = strings["DecomposeButton_type_specified"]
    )

    @classmethod
    def poll(cls, context):
        return True

    def decompose(self, dir, muscle_name):
        volume = os.path.join(dir, muscle_name + ExportButton.type_delimiter + "volume" + ExportButton.export_format_volume)
        insertion = os.path.join(dir, muscle_name + ExportButton.type_delimiter + "insertion" + ExportButton.export_format_origin_insertion)
        origin = os.path.join(dir, muscle_name + ExportButton.type_delimiter + "origin" + ExportButton.export_format_origin_insertion)

        not_exist = None
        if(not os.path.exists(volume)):
            not_exist = volume
        elif(not os.path.exists(insertion)):
            not_exist = insertion
        elif(not os.path.exists(origin)):
            not_exist = origin
        
        if(not_exist != None):
            message = strings["Message_file_not_found"] + "(File: " + not_exist + ")"
            # SimplePopup.showPopup(self, message, "ERROR", "ERROR")
            return [False, message]

        output = os.path.join(dir, muscle_name + ExportButton.type_delimiter + "decomposed" + self.mdt_format)

        mdt = "./assets/MuscleDecompositionTest" # Muscle decomposition executable
        if(platform == "win32"):
            mdt += ".exe"
            
        cmd = [
            os.path.join(os.path.realpath(os.path.dirname(__file__)), mdt), # Executable
            volume,
            "-i",
            insertion,
            "-o",
            origin,
            "-n",
            str(bpy.context.scene.export_fibres),
            "-r",
            str(bpy.context.scene.export_resolution),
            "-v",
            str(bpy.context.scene.export_visualize),
            "-f",
            output
        ]
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            msg = result.stderr.decode("utf-8")
            print("MDT: " + msg)
            return [True, msg]
        except FileNotFoundError:
            return [False, strings["Message_mdt_not_found"]]
    
    def execute(self, context): 
        to_decompose = [] # Muscle names to decompose
        dir = bpy.path.abspath(bpy.context.scene.output_path)

        if(self.type == strings["DecomposeButton_type_all"]):
            for entry in os.listdir(dir):
                if(entry.endswith(ExportButton.export_format_origin_insertion) or entry.endswith(ExportButton.export_format_volume)):
                    name = entry.split(ExportButton.type_delimiter)[0]

                    if(("decomposed" not in name) and (name not in to_decompose)):
                        to_decompose.append(name)
        else:
            to_decompose.append(bpy.context.scene.muscle_name)

        if(len(to_decompose) == 0):
            SimplePopup.showPopup(self, strings["Message_nothing_to_decompose"], "WARNING", "TRIA_UP")
            return {"FINISHED"}

        for muscle_name in to_decompose:
            res = self.decompose(dir, muscle_name)
            msg = strings["Message_decomposition_unsuccessful"]
            if(res[0] == False): # If there has been a problem with the decomposition, abort the process
                msg += res[1]
                SimplePopup.showPopup(self, msg, "ERROR", "ERROR")
                return {"CANCELLED"}
            else:
                msg = strings["Message_decomposition_done"]
                if(res[1] == ''): # No issues
                    msg += "Successful"
                    SimplePopup.showPopup(self, msg, "INFO", "INFO")
                else:
                    msg += "ERROR! Please, check the MuscleDecompositionOutput for further information"
                    SimplePopup.showPopup(self, msg, "INFO", "INFO")
                    return {"CANCELLED"}
                

            decomposed = os.path.join(dir, muscle_name + ExportButton.type_delimiter + "decomposed" + self.mdt_format) # Decomposed muscle
            # converted = os.path.join(dir, muscle_name + ExportButton.type_delimiter + "converted" + self.import_format) - DEPRECATED

            # Import back to Blender
            try:
                bpy.ops.import_scene.obj(filepath=decomposed, axis_forward="Y", axis_up="Z") # The axis parameters are crucial! 
            except FileNotFoundError:
                message = strings["Message_file_not_found"] + "(File: " + decomposed + ")"
                SimplePopup.showPopup(self, message, "ERROR", "ERROR")
                return {"CANCELLED"}
                
        return {"FINISHED"}
   

