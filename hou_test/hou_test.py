import hou

hip = "/home/rapa/temp.hipnc"
add_hip = "/home/rapa/test_hip/test_addCamMantra_1.hipnc"
# un_name ="/home/rapa/test_hip/un_name.hipnc"

# hou.hipFile.isNewFile()
# hou.hipFile.load(hip) #hip파일 가져오기

node = hou.pwd()

root = hou.node("/obj/")
if root != None:
    n = root.createNode("cam")
    n.parm("focal").set(38)


root = hou.node("/out/")
if root != None:
    n = root.createNode("ifd")
    s = "/home/rapa/test_hip/my_filename_0002.exr"
    n.parm("vm_picture").set(s)


hou.hipFile.save(file_name=add_hip)

