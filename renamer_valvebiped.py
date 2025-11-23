
bl_info = {
    "name": "Renamer ValvBiped",
    "author": "CeiLciuZ",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool",
    "description": "Easy way to rename bones",
    "warning": "",
}

import bpy


class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

class My_Button1(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button1"
    bl_label = "ValveBiped.Bip01_Pelvis"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button1.bl_label)
        return {'FINISHED'}
class My_Button2(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button2"
    bl_label = "ValveBiped.Bip01_Spine"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button2.bl_label)
        return {'FINISHED'}
class My_Button3(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button3"
    bl_label = "ValveBiped.Bip01_Spine1"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button3.bl_label)
        return {'FINISHED'}
class My_Button4(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button4"
    bl_label = "ValveBiped.Bip01_Spine2"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button4.bl_label)
        return {'FINISHED'}
class My_Button5(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button5"
    bl_label = "ValveBiped.Bip01_Spine4"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button5.bl_label)
        return {'FINISHED'}
class My_Button6(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button6"
    bl_label = "ValveBiped.Bip01_Neck1"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button6.bl_label)
        return {'FINISHED'}
class My_Button7(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button7"
    bl_label = "ValveBiped.Bip01_Head1"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button7.bl_label)
        return {'FINISHED'}
class My_Button8(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button8"
    bl_label = "ValveBiped.Bip01_R_Clavicle"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button8.bl_label)
        return {'FINISHED'}
class My_Button9(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button9"
    bl_label = "ValveBiped.Bip01_R_UpperArm"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button9.bl_label)
        return {'FINISHED'}
class My_Button10(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button10"
    bl_label = "ValveBiped.Bip01_R_Forearm"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button10.bl_label)
        return {'FINISHED'}
class My_Button11(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button11"
    bl_label = "ValveBiped.Bip01_R_Hand"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button11.bl_label)
        return {'FINISHED'}
class My_Button12(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button12"
    bl_label = "ValveBiped.Bip01_R_Finger0"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button12.bl_label)
        return {'FINISHED'}
class My_Button13(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button13"
    bl_label = "ValveBiped.Bip01_R_Finger01"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button13.bl_label)
        return {'FINISHED'}
class My_Button14(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button14"
    bl_label = "ValveBiped.Bip01_R_Finger02"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button14.bl_label)
        return {'FINISHED'}
class My_Button15(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button15"
    bl_label = "ValveBiped.Bip01_R_Finger1"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button15.bl_label)
        return {'FINISHED'}
class My_Button16(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button16"
    bl_label = "ValveBiped.Bip01_R_Finger11"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button16.bl_label)
        return {'FINISHED'}
class My_Button17(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button17"
    bl_label = "ValveBiped.Bip01_R_Finger12"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button17.bl_label)
        return {'FINISHED'}
class My_Button18(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button18"
    bl_label = "ValveBiped.Bip01_R_Finger2"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button18.bl_label)
        return {'FINISHED'}
class My_Button19(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button19"
    bl_label = "ValveBiped.Bip01_R_Finger21"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button19.bl_label)
        return {'FINISHED'}
class My_Button20(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button20"
    bl_label = "ValveBiped.Bip01_R_Finger22"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button20.bl_label)
        return {'FINISHED'}
class My_Button21(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button21"
    bl_label = "ValveBiped.Bip01_R_Finger3"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button21.bl_label)
        return {'FINISHED'}
class My_Button22(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button22"
    bl_label = "ValveBiped.Bip01_R_Finger31"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button22.bl_label)
        return {'FINISHED'}
class My_Button23(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button23"
    bl_label = "ValveBiped.Bip01_R_Finger32"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button23.bl_label)
        return {'FINISHED'}
class My_Button24(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button24"
    bl_label = "ValveBiped.Bip01_R_Finger4"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button24.bl_label)
        return {'FINISHED'}
class My_Button25(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button25"
    bl_label = "ValveBiped.Bip01_R_Finger41"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button25.bl_label)
        return {'FINISHED'}
class My_Button26(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button26"
    bl_label = "ValveBiped.Bip01_R_Finger42"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button26.bl_label)
        return {'FINISHED'}
class My_Button27(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button27"
    bl_label = "ValveBiped.Bip01_L_Clavicle"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button27.bl_label)
        return {'FINISHED'}
class My_Button28(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button28"
    bl_label = "ValveBiped.Bip01_L_UpperArm"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button28.bl_label)
        return {'FINISHED'}
class My_Button29(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button29"
    bl_label = "ValveBiped.Bip01_L_Forearm"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button29.bl_label)
        return {'FINISHED'}
class My_Button30(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button30"
    bl_label = "ValveBiped.Bip01_L_Hand"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button30.bl_label)
        return {'FINISHED'}
class My_Button31(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button31"
    bl_label = "ValveBiped.Bip01_L_Finger0"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button31.bl_label)
        return {'FINISHED'}
class My_Button32(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button32"
    bl_label = "ValveBiped.Bip01_L_Finger01"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button32.bl_label)
        return {'FINISHED'}
class My_Button33(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button33"
    bl_label = "ValveBiped.Bip01_L_Finger02"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button33.bl_label)
        return {'FINISHED'}
class My_Button34(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button34"
    bl_label = "ValveBiped.Bip01_L_Finger1"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button34.bl_label)
        return {'FINISHED'}
class My_Button35(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button35"
    bl_label = "ValveBiped.Bip01_L_Finger11"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button35.bl_label)
        return {'FINISHED'}
class My_Button36(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button36"
    bl_label = "ValveBiped.Bip01_L_Finger12"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button36.bl_label)
        return {'FINISHED'}
class My_Button37(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button37"
    bl_label = "ValveBiped.Bip01_L_Finger2"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button37.bl_label)
        return {'FINISHED'}
class My_Button38(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button38"
    bl_label = "ValveBiped.Bip01_L_Finger21"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button38.bl_label)
        return {'FINISHED'}
class My_Button39(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button39"
    bl_label = "ValveBiped.Bip01_L_Finger22"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button39.bl_label)
        return {'FINISHED'}
class My_Button40(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button40"
    bl_label = "ValveBiped.Bip01_L_Finger3"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button40.bl_label)
        return {'FINISHED'}
class My_Button41(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button41"
    bl_label = "ValveBiped.Bip01_L_Finger31"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button41.bl_label)
        return {'FINISHED'}
class My_Button42(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button42"
    bl_label = "ValveBiped.Bip01_L_Finger32"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button42.bl_label)
        return {'FINISHED'}
class My_Button43(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button43"
    bl_label = "ValveBiped.Bip01_L_Finger4"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button43.bl_label)
        return {'FINISHED'}
class My_Button44(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button44"
    bl_label = "ValveBiped.Bip01_L_Finger41"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button44.bl_label)
        return {'FINISHED'}
class My_Button45(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button45"
    bl_label = "ValveBiped.Bip01_L_Finger42"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button45.bl_label)
        return {'FINISHED'}
class My_Button46(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button46"
    bl_label = "ValveBiped.Bip01_R_Thigh"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button46.bl_label)
        return {'FINISHED'}
class My_Button47(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button47"
    bl_label = "ValveBiped.Bip01_R_Calf"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button47.bl_label)
        return {'FINISHED'}
class My_Button48(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button48"
    bl_label = "ValveBiped.Bip01_R_Foot"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button48.bl_label)
        return {'FINISHED'}
class My_Button49(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button49"
    bl_label = "ValveBiped.Bip01_R_Toe0"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button49.bl_label)
        return {'FINISHED'}
class My_Button50(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button50"
    bl_label = "ValveBiped.Bip01_L_Thigh"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button50.bl_label)
        return {'FINISHED'}
class My_Button51(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button51"
    bl_label = "ValveBiped.Bip01_L_Calf"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button51.bl_label)
        return {'FINISHED'}
class My_Button52(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button52"
    bl_label = "ValveBiped.Bip01_L_Foot"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button52.bl_label)
        return {'FINISHED'}
class My_Button53(bpy.types.Operator):
    """Remove Doubles on Objects in Selection"""
    bl_idname = "object.button53"
    bl_label = "ValveBiped.Bip01_L_Toe0"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True

    def execute(self, context):
        context.active_bone.name = format(My_Button53.bl_label)
        return {'FINISHED'}




class PanelOne(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_1"
    bl_label = "Renamer ValveBone"

    def draw(self, context):
        obj = context.object
        layout = self.layout
        
        
        
        row = layout.row()
        row.label(text="Active object is: {}".format(obj.name))
        
        row = layout.row()
        row.label(text="Actual bone name is: {}".format(context.active_bone.name))
        
        row = layout.row()
        row.operator(My_Button1.bl_idname)

        row = layout.row()
        row.operator(My_Button2.bl_idname)

        row = layout.row()
        row.operator(My_Button3.bl_idname)

        row = layout.row()
        row.operator(My_Button4.bl_idname)

        row = layout.row()
        row.operator(My_Button5.bl_idname)

        row = layout.row()
        row.operator(My_Button6.bl_idname)

        row = layout.row()
        row.operator(My_Button7.bl_idname)

        row = layout.row()
        row.operator(My_Button8.bl_idname)

        row = layout.row()
        row.operator(My_Button9.bl_idname)

        row = layout.row()
        row.operator(My_Button10.bl_idname)

        row = layout.row()
        row.operator(My_Button11.bl_idname)

        row = layout.row()
        row.operator(My_Button12.bl_idname)

        row = layout.row()
        row.operator(My_Button13.bl_idname)

        row = layout.row()
        row.operator(My_Button14.bl_idname)

        row = layout.row()
        row.operator(My_Button15.bl_idname)

        row = layout.row()
        row.operator(My_Button16.bl_idname)

        row = layout.row()
        row.operator(My_Button17.bl_idname)

        row = layout.row()
        row.operator(My_Button18.bl_idname)

        row = layout.row()
        row.operator(My_Button19.bl_idname)

        row = layout.row()
        row.operator(My_Button20.bl_idname)

        row = layout.row()
        row.operator(My_Button21.bl_idname)

        row = layout.row()
        row.operator(My_Button22.bl_idname)

        row = layout.row()
        row.operator(My_Button23.bl_idname)

        row = layout.row()
        row.operator(My_Button24.bl_idname)

        row = layout.row()
        row.operator(My_Button25.bl_idname)

        row = layout.row()
        row.operator(My_Button26.bl_idname)

        row = layout.row()
        row.operator(My_Button27.bl_idname)

        row = layout.row()
        row.operator(My_Button28.bl_idname)

        row = layout.row()
        row.operator(My_Button29.bl_idname)

        row = layout.row()
        row.operator(My_Button30.bl_idname)

        row = layout.row()
        row.operator(My_Button31.bl_idname)

        row = layout.row()
        row.operator(My_Button32.bl_idname)

        row = layout.row()
        row.operator(My_Button33.bl_idname)

        row = layout.row()
        row.operator(My_Button34.bl_idname)

        row = layout.row()
        row.operator(My_Button35.bl_idname)

        row = layout.row()
        row.operator(My_Button36.bl_idname)

        row = layout.row()
        row.operator(My_Button37.bl_idname)

        row = layout.row()
        row.operator(My_Button38.bl_idname)

        row = layout.row()
        row.operator(My_Button39.bl_idname)

        row = layout.row()
        row.operator(My_Button40.bl_idname)

        row = layout.row()
        row.operator(My_Button41.bl_idname)

        row = layout.row()
        row.operator(My_Button42.bl_idname)

        row = layout.row()
        row.operator(My_Button43.bl_idname)

        row = layout.row()
        row.operator(My_Button44.bl_idname)

        row = layout.row()
        row.operator(My_Button45.bl_idname)

        row = layout.row()
        row.operator(My_Button46.bl_idname)

        row = layout.row()
        row.operator(My_Button47.bl_idname)

        row = layout.row()
        row.operator(My_Button48.bl_idname)

        row = layout.row()
        row.operator(My_Button49.bl_idname)

        row = layout.row()
        row.operator(My_Button50.bl_idname)

        row = layout.row()
        row.operator(My_Button51.bl_idname)

        row = layout.row()
        row.operator(My_Button52.bl_idname)

        row = layout.row()
        row.operator(My_Button53.bl_idname)






def register():
    bpy.utils.register_class(My_Button1)
    bpy.utils.register_class(My_Button2)
    bpy.utils.register_class(My_Button3)
    bpy.utils.register_class(My_Button4)
    bpy.utils.register_class(My_Button5)
    bpy.utils.register_class(My_Button6)
    bpy.utils.register_class(My_Button7)
    bpy.utils.register_class(My_Button8)
    bpy.utils.register_class(My_Button9)
    bpy.utils.register_class(My_Button10)
    bpy.utils.register_class(My_Button11)
    bpy.utils.register_class(My_Button12)
    bpy.utils.register_class(My_Button13)
    bpy.utils.register_class(My_Button14)
    bpy.utils.register_class(My_Button15)
    bpy.utils.register_class(My_Button16)
    bpy.utils.register_class(My_Button17)
    bpy.utils.register_class(My_Button18)
    bpy.utils.register_class(My_Button19)
    bpy.utils.register_class(My_Button20)
    bpy.utils.register_class(My_Button21)
    bpy.utils.register_class(My_Button22)
    bpy.utils.register_class(My_Button23)
    bpy.utils.register_class(My_Button24)
    bpy.utils.register_class(My_Button25)
    bpy.utils.register_class(My_Button26)
    bpy.utils.register_class(My_Button27)
    bpy.utils.register_class(My_Button28)
    bpy.utils.register_class(My_Button29)
    bpy.utils.register_class(My_Button30)
    bpy.utils.register_class(My_Button31)
    bpy.utils.register_class(My_Button32)
    bpy.utils.register_class(My_Button33)
    bpy.utils.register_class(My_Button34)
    bpy.utils.register_class(My_Button35)
    bpy.utils.register_class(My_Button36)
    bpy.utils.register_class(My_Button37)
    bpy.utils.register_class(My_Button38)
    bpy.utils.register_class(My_Button39)
    bpy.utils.register_class(My_Button40)
    bpy.utils.register_class(My_Button41)
    bpy.utils.register_class(My_Button42)
    bpy.utils.register_class(My_Button43)
    bpy.utils.register_class(My_Button44)
    bpy.utils.register_class(My_Button45)
    bpy.utils.register_class(My_Button46)
    bpy.utils.register_class(My_Button47)
    bpy.utils.register_class(My_Button48)
    bpy.utils.register_class(My_Button49)
    bpy.utils.register_class(My_Button50)
    bpy.utils.register_class(My_Button51)
    bpy.utils.register_class(My_Button52)
    bpy.utils.register_class(My_Button53)
    bpy.utils.register_class(PanelOne)


def unregister():
    bpy.utils.unregister_class(My_Button1)
    bpy.utils.unregister_class(My_Button2)
    bpy.utils.unregister_class(My_Button3)
    bpy.utils.unregister_class(My_Button4)
    bpy.utils.unregister_class(My_Button5)
    bpy.utils.unregister_class(My_Button6)
    bpy.utils.unregister_class(My_Button7)
    bpy.utils.unregister_class(My_Button8)
    bpy.utils.unregister_class(My_Button9)
    bpy.utils.unregister_class(My_Button10)
    bpy.utils.unregister_class(My_Button11)
    bpy.utils.unregister_class(My_Button12)
    bpy.utils.unregister_class(My_Button13)
    bpy.utils.unregister_class(My_Button14)
    bpy.utils.unregister_class(My_Button15)
    bpy.utils.unregister_class(My_Button16)
    bpy.utils.unregister_class(My_Button17)
    bpy.utils.unregister_class(My_Button18)
    bpy.utils.unregister_class(My_Button19)
    bpy.utils.unregister_class(My_Button20)
    bpy.utils.unregister_class(My_Button21)
    bpy.utils.unregister_class(My_Button22)
    bpy.utils.unregister_class(My_Button23)
    bpy.utils.unregister_class(My_Button24)
    bpy.utils.unregister_class(My_Button25)
    bpy.utils.unregister_class(My_Button26)
    bpy.utils.unregister_class(My_Button27)
    bpy.utils.unregister_class(My_Button28)
    bpy.utils.unregister_class(My_Button29)
    bpy.utils.unregister_class(My_Button30)
    bpy.utils.unregister_class(My_Button31)
    bpy.utils.unregister_class(My_Button32)
    bpy.utils.unregister_class(My_Button33)
    bpy.utils.unregister_class(My_Button34)
    bpy.utils.unregister_class(My_Button35)
    bpy.utils.unregister_class(My_Button36)
    bpy.utils.unregister_class(My_Button37)
    bpy.utils.unregister_class(My_Button38)
    bpy.utils.unregister_class(My_Button39)
    bpy.utils.unregister_class(My_Button40)
    bpy.utils.unregister_class(My_Button41)
    bpy.utils.unregister_class(My_Button42)
    bpy.utils.unregister_class(My_Button43)
    bpy.utils.unregister_class(My_Button44)
    bpy.utils.unregister_class(My_Button45)
    bpy.utils.unregister_class(My_Button46)
    bpy.utils.unregister_class(My_Button47)
    bpy.utils.unregister_class(My_Button48)
    bpy.utils.unregister_class(My_Button49)
    bpy.utils.unregister_class(My_Button50)
    bpy.utils.unregister_class(My_Button51)
    bpy.utils.unregister_class(My_Button52)
    bpy.utils.unregister_class(My_Button53)
    bpy.utils.unregister_class(PanelOne)


if __name__ == "__main__":
    register()
