import os
path = r"C:\ComfyUI_windows_portable_nvidia\ComfyUI_windows_portable\ComfyUI\models\checkpoints\flux1-dev-fp8.safetensors"
print(f"Path exists: {os.path.exists(path)}")
print(f"Path is file: {os.path.isfile(path)}")
print(f"Path is directory: {os.path.isdir(path)}")
print(f"Parent directory exists: {os.path.exists(os.path.dirname(path))}")


