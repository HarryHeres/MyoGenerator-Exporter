import bpy

class ProgressPopup(bpy.types.Operator):
    bl_idname = "exporter.ok_popup"
    bl_label = "Exporting successful!"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        return {"FINISHED"}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class SimplePopup():
    '''
    Create a simple popup to notify the user
    '''
    def showPopup(self, message = "Message", title = "Info", icon = 'INFO'):
        def draw(self, context):
            self.layout.label(text = message)

        bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)