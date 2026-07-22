import bpy

def reset_all_shapekeys():
    """
    Réinitialise la valeur de toutes les shape keys du fichier courant à 0.0.
    """
    # Itération directe sur les datablocks de shape keys
    for shape_key in bpy.data.shape_keys:
        for kb in shape_key.key_blocks:
            kb.value = 0.0
            
if __name__ == "__main__":
    reset_all_shapekeys()
    print("Toutes les valeurs des shape keys ont été réinitialisées à 0.0.")