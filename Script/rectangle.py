
import bpy

# 既存要素削除
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
#立方体の描画
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), size=1.5, rotation=(0, 0, 0))
#図形を変形(X方向2倍、Y方向1倍、厚さ方向0.5倍)
bpy.ops.transform.resize(value=(2.0,1.0,0.1))
#図形を回転(Y軸周りに 30°)
bpy.ops.transform.rotate(value=3.1415/6 ,orient_axis='Y')
#図形を移動(Z軸方向に 5移動)
bpy.ops.transform.translate(value=(0,0,5))
