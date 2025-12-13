import bpy
import os

export_path = "/home/ceilciuz/export_obj/"

os.makedirs(export_path, exist_ok=True)

bpy.ops.object.select_all(action='DESELECT')

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        filepath = os.path.join(export_path, f"{obj.name}.obj")

        bpy.ops.wm.obj_export(
            filepath=filepath,
            export_selected_objects=True,
            export_materials=False
        )

        obj.select_set(False)

print("Export terminé")
