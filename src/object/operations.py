'''
Common object operations (methods) to import
'''
### General libraries ### 

### Blender libraries ###
import bpy
import bmesh
import bpy.types


def triangulate_volume(obj) -> None:
    '''
    Triangulate volume model mesh from quadrilateral
    '''
    bpy.context.view_layer.objects.active = bpy.data.objects[obj.name] # Make object active
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
    print("[" + obj.name + "]: Model triangulated")


def reorder_coords(obj) -> 'bpy.types.BMesh':
    '''
    Reorder boundary vertices into a sequentially numbered order
    '''
    reordered = bmesh.from_edit_mesh(obj.data)
    if hasattr(reordered.verts, "ensure_lookup_table"):
        reordered.verts.ensure_lookup_table()
    initial = reordered.verts[0]
    vert = initial
    prev = None
    for i in range(len(reordered.verts)):
        vert.index = i
        next = None
        for v in [e.other_vert(vert) for e in vert.link_edges]:
            if (v != prev and v != initial):
                next = v
        if next is None:
            break
        prev, vert = vert, next
    reordered.verts.sort()
    bmesh.update_edit_mesh(obj.data)
    print("[" + obj.name + "]: Reordered vertices")
    return reordered