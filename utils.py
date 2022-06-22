from platform import platform


import os
import platform
def check_for_packwiz(root):
    """
    Check if Packwiz is installed.
    """
    path_var = os.environ.get("PATH")
    os_var = platform.system()
    match os_var:
        case "Windows":
            packwiz_name = "packwiz.exe"
        case "Linux":
            packwiz_name = "packwiz"
        case "Darwin":
            packwiz_name = "packwiz"
    if path_var is None:
        return False
    path_list = path_var.split(os.pathsep)
    for path in path_list:
        if os.path.isfile(os.path.join(path, f"{packwiz_name}")):
            return True
    if os.path.isfile(f"{root}/bin/{packwiz_name}"):
        return True