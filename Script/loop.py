import bpy
import math

# 既存要素削除
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

N = 12
RR1 = 10.0
RR2 = 2.0
for i in range(0, N):
    rad = 2 * math.pi * i /N  # 角度計算2π i /n
    xx = RR1 * math.cos(rad) # x座標計算 半径*cosθ
    yy = RR1 * math.sin(rad) # y座標計算 半径*sinθ
    # 球体作成
    bpy.ops.mesh.primitive_ico_sphere_add(location=(xx, yy, 0),radius= RR2, subdivisions = 5 )
