import bpy

obj = bpy.context.active_object

if not obj or obj.type != 'ARMATURE' or bpy.context.mode != 'POSE':
    raise Exception("Armature active + Pose Mode requis")

bones = [
    pb.name
    for pb in obj.pose.bones
    if pb.select
]

bpy.context.window_manager.clipboard = "\n".join(bones)

"Copié dans le presse-papier"
