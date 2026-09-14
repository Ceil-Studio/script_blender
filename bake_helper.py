import bpy

class NODE_OT_create_bake_textures(bpy.types.Operator):
    bl_idname = "node.create_bake_textures"
    bl_label = "Créer Textures de Bake"
    bl_options = {'REGISTER', 'UNDO'}
    
    res_x: bpy.props.IntProperty(name="Résolution X", default=2048, min=1)
    res_y: bpy.props.IntProperty(name="Résolution Y", default=2048, min=1)
    img_name: bpy.props.StringProperty(name="Nom", default="Bake_Texture")
    
    def execute(self, context):
        obj = context.active_object
        if not obj:
            self.report({'WARNING'}, "Aucun objet actif.")
            return {'CANCELLED'}
            
        mat = obj.active_material
        if not mat or not mat.use_nodes:
            self.report({'WARNING'}, "L'objet actif n'a pas de matériau nodal.")
            return {'CANCELLED'}

        name_bc = f"{self.img_name}_basecolor"
        name_rgh = f"{self.img_name}_roughness"
        name_nrm = f"{self.img_name}_normal"

        img_bc = bpy.data.images.new(name=name_bc, width=self.res_x, height=self.res_y, alpha=True, float_buffer=False)
        img_rgh = bpy.data.images.new(name=name_rgh, width=self.res_x, height=self.res_y, alpha=False, float_buffer=False)
        img_nrm = bpy.data.images.new(name=name_nrm, width=self.res_x, height=self.res_y, alpha=False, float_buffer=False)
        
        img_rgh.colorspace_settings.name = 'Non-Color'
        img_nrm.colorspace_settings.name = 'Non-Color'
        
        tree = mat.node_tree
        links = tree.links

        start_x, start_y = 0, 0
        if tree.nodes.active:
            start_x, start_y = tree.nodes.active.location.x, tree.nodes.active.location.y
            
        tex_coord = tree.nodes.new(type='ShaderNodeTexCoord')
        mapping = tree.nodes.new(type='ShaderNodeMapping')
        
        node_bc = tree.nodes.new(type='ShaderNodeTexImage')
        node_bc.image = img_bc
        
        node_rgh = tree.nodes.new(type='ShaderNodeTexImage')
        node_rgh.image = img_rgh
        
        node_nrm = tree.nodes.new(type='ShaderNodeTexImage')
        node_nrm.image = img_nrm
        
        normal_map = tree.nodes.new(type='ShaderNodeNormalMap')
        principled = tree.nodes.new(type='ShaderNodeBsdfPrincipled')

        offset_x = start_x + 1000
        
        tex_coord.location = (offset_x - 1000, start_y)
        mapping.location = (offset_x - 800, start_y)
        
        node_bc.location = (offset_x - 500, start_y)
        node_rgh.location = (offset_x - 500, start_y - 300)
        node_nrm.location = (offset_x - 500, start_y - 600)
        
        normal_map.location = (offset_x - 200, start_y - 600)
        principled.location = (offset_x, start_y)

        links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], node_bc.inputs['Vector'])
        links.new(mapping.outputs['Vector'], node_rgh.inputs['Vector'])
        links.new(mapping.outputs['Vector'], node_nrm.inputs['Vector'])
        
        links.new(node_bc.outputs['Color'], principled.inputs['Base Color'])
        links.new(node_rgh.outputs['Color'], principled.inputs['Roughness'])
        
        links.new(node_nrm.outputs['Color'], normal_map.inputs['Color'])
        links.new(normal_map.outputs['Normal'], principled.inputs['Normal'])
            
        for node in tree.nodes:
            node.select = False
            
        tex_coord.select = True
        mapping.select = True
        node_bc.select = True
        node_rgh.select = True
        node_nrm.select = True
        normal_map.select = True
        principled.select = True
        
        tree.nodes.active = node_bc

        return {'FINISHED'}

class NODE_OT_bake_texture(bpy.types.Operator):
    bl_idname = "node.bake_texture"
    bl_label = "Bake Texture"
    bl_options = {'REGISTER', 'UNDO'}

    bake_type: bpy.props.StringProperty(default='DIFFUSE_COLOR')

    def execute(self, context):
        scene = context.scene
        
        if scene.render.engine != 'CYCLES':
            scene.render.engine = 'CYCLES'

        obj = context.active_object
        if not obj:
            self.report({'WARNING'}, "Aucun objet actif.")
            return {'CANCELLED'}
            
        mat = obj.active_material
        if not mat or not mat.use_nodes:
            self.report({'WARNING'}, "L'objet actif n'a pas de matériau nodal.")
            return {'CANCELLED'}

        active_node = mat.node_tree.nodes.active
        if not active_node or active_node.type != 'TEX_IMAGE':
            self.report({'WARNING'}, "Veuillez sélectionner et activer un nœud Image Texture dans le matériau.")
            return {'CANCELLED'}

        bpy.ops.object.select_all(action='DESELECT')
        
        target_objects = []
        for o in context.view_layer.objects:
            if o.type == 'MESH' and o.visible_get():
                if mat.name in [m.name for m in o.data.materials if m]:
                    o.select_set(True)
                    target_objects.append(o)
                    
        if not target_objects:
            self.report({'WARNING'}, "Aucun objet MESH visible dans la View Layer n'utilise ce matériau.")
            return {'CANCELLED'}

        context.view_layer.objects.active = target_objects[0]

        try:
            if self.bake_type == 'DIFFUSE_COLOR':
                bpy.ops.object.bake(type='DIFFUSE', pass_filter={'COLOR'})
                bake_name = "Diffuse (Color)"
            elif self.bake_type == 'ROUGHNESS':
                bpy.ops.object.bake(type='ROUGHNESS')
                bake_name = "Roughness"
            elif self.bake_type == 'NORMAL':
                bpy.ops.object.bake(type='NORMAL')
                bake_name = "Normal"
                
            self.report({'INFO'}, f"Bake {bake_name} terminé sur {len(target_objects)} objet(s).")
        except Exception as e:
            self.report({'ERROR'}, f"Échec du bake : {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}

class NODE_PT_bake_texture_panel(bpy.types.Panel):
    bl_label = "Bake Helper"
    bl_idname = "NODE_PT_bake_texture_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Bake"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "bake_res_x", text="X")
        layout.prop(scene, "bake_res_y", text="Y")
        layout.prop(scene, "bake_img_name", text="Nom")

        layout.separator()
        
        props = layout.operator(NODE_OT_create_bake_textures.bl_idname, text="Générer Setup", icon='NODETREE')
        props.res_x = scene.bake_res_x
        props.res_y = scene.bake_res_y
        props.img_name = scene.bake_img_name

        layout.separator()
        
        col = layout.column(align=True)
        
        op_diff = col.operator(NODE_OT_bake_texture.bl_idname, text="Bake Diffuse", icon='SHADING_TEXTURE')
        op_diff.bake_type = 'DIFFUSE_COLOR'
        
        op_rough = col.operator(NODE_OT_bake_texture.bl_idname, text="Bake Roughness", icon='SHADING_RENDERED')
        op_rough.bake_type = 'ROUGHNESS'
        
        op_norm = col.operator(NODE_OT_bake_texture.bl_idname, text="Bake Normal", icon='MATCUBE')
        op_norm.bake_type = 'NORMAL'

classes = (NODE_OT_create_bake_textures, NODE_OT_bake_texture, NODE_PT_bake_texture_panel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.bake_res_x = bpy.props.IntProperty(name="Res X", default=2048, min=1)
    bpy.types.Scene.bake_res_y = bpy.props.IntProperty(name="Res Y", default=2048, min=1)
    bpy.types.Scene.bake_img_name = bpy.props.StringProperty(name="Nom", default="Texture")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.bake_res_x
    del bpy.types.Scene.bake_res_y
    del bpy.types.Scene.bake_img_name

if __name__ == "__main__":
    register()