import distro as d
def dis():
 ose = d.os_release_info()

 for key1,value1 in ose.items():
    print(f"{key1}: {value1}")
