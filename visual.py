import open3d as o3d
import numpy as np
# visualization of point clouds.
pcd = o3d.io.read_point_cloud('/home/heihei/Downloads/uni_ply/author/mvsnet048_l3.ply')
# o3d.visualization.draw_geometries([pcd])


vis = o3d.visualization.Visualizer()
vis.create_window()
render_option: o3d.visualization.RenderOption = vis.get_render_option()
render_option.background_color = np.array([0, 0, 0])
# render_option.point_size = 2.0
vis.add_geometry(pcd)
vis.run()
