import bpy

obj = bpy.context.active_object

names = []

if obj and obj.data.shape_keys:
    for sk in obj.data.shape_keys.key_blocks:
        names.append(sk.name)

bpy.context.window_manager.clipboard = "\n".join(names)

"Copié dans le presse-papier"

