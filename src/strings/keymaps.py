from ..mirroring.mirror_menu import MirrorMenu

keymaps = {"Mirroring": [{
                "label": "Mirror object(s)",
                "region_type": "WINDOW",
                "space_type": "EMPTY",
                "map_type": "KEYBOARD",
                "menu_name": "Window",
                "action" : "wm.call_panel",
                "idname": MirrorMenu.bl_idname,
                "type": "F5",
                "ctrl": False,
                "alt": False,
                "shift": False,
                "oskey": False,
                "value": "PRESS"
            }]}
'''
Add-on specific keymaps
'''