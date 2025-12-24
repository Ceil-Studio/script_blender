bl_info = {
    "name": "Renamer ValveBiped",
    "author": "CeiLciuZ",
    "version": (1, 2, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Tool",
    "description": "Clean ValveBiped bone renamer",
}

import bpy


# =====================================================
# SIMPLE RENAME OPERATOR
# =====================================================

class OBJECT_OT_rename_bone(bpy.types.Operator):
    bl_idname = "object.rename_bone"
    bl_label = "Rename Bone"

    bone_name: bpy.props.StringProperty()

    def execute(self, context):

        obj = context.object
        if not obj or obj.type != 'ARMATURE' or context.mode != 'POSE':
            return {'CANCELLED'}

        pbone = context.active_pose_bone
        if not pbone:
            return {'CANCELLED'}

        pbone.name = self.bone_name
        return {'FINISHED'}


# =====================================================
# FINGER CHAIN OPERATOR
# =====================================================

class OBJECT_OT_rename_finger_chain(bpy.types.Operator):
    bl_idname = "object.rename_finger_chain"
    bl_label = "Rename Finger Chain"

    base_name: bpy.props.StringProperty()

    def execute(self, context):

        obj = context.object
        if not obj or obj.type != 'ARMATURE' or context.mode != 'POSE':
            return {'CANCELLED'}

        pbone = context.active_pose_bone
        if not pbone:
            return {'CANCELLED'}

        pbone.name = self.base_name

        if pbone.children:
            c1 = pbone.children[0]
            c1.name = f"{self.base_name}1"

            if c1.children:
                c2 = c1.children[0]
                c2.name = f"{self.base_name}2"

        return {'FINISHED'}


# =====================================================
# PANEL
# =====================================================

class VIEW3D_PT_valvebiped_renamer(bpy.types.Panel):
    bl_label = "ValveBiped Renamer"
    bl_idname = "VIEW3D_PT_valvebiped_renamer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        # ---------------- BODY ----------------
        layout.label(text="Body")

        body_bones = [
            "ValveBiped.Bip01_Pelvis",
            "ValveBiped.Bip01_Spine",
            "ValveBiped.Bip01_Spine1",
            "ValveBiped.Bip01_Spine2",
            "ValveBiped.Bip01_Spine4",
            "ValveBiped.Bip01_Neck1",
            "ValveBiped.Bip01_Head1",
        ]

        for name in body_bones:
            op = layout.operator("object.rename_bone", text=name)
            op.bone_name = name

        layout.separator()

        # ---------------- RIGHT ARM ----------------
        layout.label(text="Right Arm")

        right_arm = [
            "ValveBiped.Bip01_R_Clavicle",
            "ValveBiped.Bip01_R_UpperArm",
            "ValveBiped.Bip01_R_Forearm",
            "ValveBiped.Bip01_R_Hand",
        ]

        for name in right_arm:
            op = layout.operator("object.rename_bone", text=name)
            op.bone_name = name

        for i in range(5):
            op = layout.operator(
                "object.rename_finger_chain",
                text=f"R Finger {i}"
            )
            op.base_name = f"ValveBiped.Bip01_R_Finger{i}"

        layout.separator()

        # ---------------- LEFT ARM ----------------
        layout.label(text="Left Arm")

        left_arm = [
            "ValveBiped.Bip01_L_Clavicle",
            "ValveBiped.Bip01_L_UpperArm",
            "ValveBiped.Bip01_L_Forearm",
            "ValveBiped.Bip01_L_Hand",
        ]

        for name in left_arm:
            op = layout.operator("object.rename_bone", text=name)
            op.bone_name = name

        for i in range(5):
            op = layout.operator(
                "object.rename_finger_chain",
                text=f"L Finger {i}"
            )
            op.base_name = f"ValveBiped.Bip01_L_Finger{i}"

        layout.separator()

        # ---------------- LEGS ----------------
        layout.label(text="Legs")

        legs = [
            "ValveBiped.Bip01_R_Thigh",
            "ValveBiped.Bip01_R_Calf",
            "ValveBiped.Bip01_R_Foot",
            "ValveBiped.Bip01_R_Toe0",
            "ValveBiped.Bip01_L_Thigh",
            "ValveBiped.Bip01_L_Calf",
            "ValveBiped.Bip01_L_Foot",
            "ValveBiped.Bip01_L_Toe0",
        ]

        for name in legs:
            op = layout.operator("object.rename_bone", text=name)
            op.bone_name = name


# =====================================================
# REGISTER
# =====================================================

classes = (
    OBJECT_OT_rename_bone,
    OBJECT_OT_rename_finger_chain,
    VIEW3D_PT_valvebiped_renamer,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
