### General libraries ### 
from .addon_export_button import ExportButton
from .strings import strings
from.addon_decompose_button import DecomposeButton

# NOTE: Developing in VS CODE: Have to import the whole bpy library,
# since the Blender addon development extension is a bit older and 
# does not link the some submodules very well
### Blender libraries ###
import bpy

class MainPanel(bpy.types.Panel):

    ### Class atributes ### 
    bl_idname = "ExportAddon_Panel"
    bl_label = "MyoGenerator Exporter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Exporter"
    bl_context = "objectmode"

    # Draw the add-on's panel
    def draw(self, context):
        layout = self.layout
        box = layout.box()

        # Select output path
        row = box.row()
        row.label(text=strings["Label_output_path_text"])

        # Output directory 
        row = box.row()
        row.prop(context.scene, "output_path", text="") 

        # Output filename
        row = box.row()
        row.label(text=strings["Label_output_filename_text"])

        row = box.row()
        row.prop(context.scene, "muscle_name", text = "")

        layout.separator()

        # Muscle decomposition parameters
        box = layout.box()
        row = box.row()
        row.label(text=strings["Label_parameters_text"])

        # Number of fibres
        row = box.row()
        row.prop(context.scene, "export_fibres", text="Fibres")

        # Resolution of the fibres
        box = layout.box()
        row = box.row()
        row.prop(context.scene, "export_resolution", text="Resolution")

        # Visualization mode
        box = layout.box()
        row = box.row()
        row.prop(context.scene, "export_visualize", text="Visualization mode")

        layout.separator()

        # Export button
        box = layout.box()
        row = box.row()
        col = row.column()
        col.operator(ExportButton.bl_idname, text=strings["ExportButton_text"])
        col.enabled = (context.scene.output_path != "") # Path HAS to be set

        layout.separator()

        # Decompose buttons
        box = layout.box()
        row = box.row()
        row.operator(DecomposeButton.bl_idname, text = strings["DecomposeButton_type_specified_text"])
        row.enabled = (context.scene.output_path != "" and context.scene.muscle_name != "") # Path AND filename have to be set

        row = box.row()
        row.operator(DecomposeButton.bl_idname, text = strings["DecomposeButton_type_all_text"]).type = "all"
        row.enabled = (context.scene.output_path != "") # Only path has to be specified
        