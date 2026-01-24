import bpy
import mathutils

def copy_bone_distance_to_clipboard():
    obj = bpy.context.active_object

    # Vérification armature
    if not obj or obj.type != 'ARMATURE':
        show_message("Sélectionne une armature.", "Erreur", 'ERROR')
        return

    mode = obj.mode
    matrix_world = obj.matrix_world

    # ======================
    # EDIT MODE
    # ======================
    if mode == 'EDIT':
        bones = bpy.context.selected_editable_bones

        if len(bones) != 2:
            show_message("Sélectionne exactement 2 os.", "Erreur", 'ERROR')
            return

        p1 = matrix_world @ bones[0].head
        p2 = matrix_world @ bones[1].head

    # ======================
    # POSE MODE
    # ======================
    elif mode == 'POSE':
        bones = bpy.context.selected_pose_bones

        if len(bones) != 2:
            show_message("Sélectionne exactement 2 os.", "Erreur", 'ERROR')
            return

        # Head en espace monde
        p1 = matrix_world @ bones[0].matrix.translation
        p2 = matrix_world @ bones[1].matrix.translation

    else:
        show_message("Passe en Edit ou Pose Mode.", "Erreur", 'ERROR')
        return

    # ======================
    # Distance
    # ======================
    distance = (p1 - p2).length
    distance_str = str(round(distance, 3))

    bpy.context.window_manager.clipboard = distance_str
    show_message(f"{distance_str} m", "Distance copiée", 'COPYDOWN')
    print(f"Distance copiée : {distance_str}")

def show_message(message="", title="Message", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

if __name__ == "__main__":
    copy_bone_distance_to_clipboard()
