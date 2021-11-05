import bpy

# 1.既存要素削除
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

# 2.材質の定義(赤色)
mat1 = bpy.data.materials.new('Red')
mat1.diffuse_color = (1.0, 0.0, 0.0, 1.0)

# 3.材質の定義(青色)
mat2 = bpy.data.materials.new('blue')
mat2.diffuse_color = (0.0, 0.0, 1.0, 1.0)

# 4.球体作成
bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 1), radius = 0.5, subdivisions=5 )
bpy.context.object.data.materials.append(mat1) # 材質(赤)指定

# 5.平板作成
bpy.ops.mesh.primitive_cube_add(location=(0, -0.5, 0), size=2.5)
bpy.ops.transform.resize(value=(2.0,2.0,0.05)) # 図形を変形(X方向2倍、Y方向2倍、厚さ方向0.05倍)
bpy.context.object.data.materials.append(mat2) # 材質(青)指定
