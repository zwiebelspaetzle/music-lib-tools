import os
import subprocess
import sys

def run_fast_scandir(dir: str):
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            print(f.path)
            result = subprocess.run(["md5", f.path], capture_output=True, text=True)
            print(result.stdout.split(" = ").pop())

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files

def get_md5(path):
  md5_hash = md5()
  with open(path, "rb") as f:
      # Read and update hash in chunks of 4K
      for byte_block in iter(lambda: f.read(4096),b""):
          md5_hash.update(byte_block)
      return md5_hash.hexdigest()

directory = os.path.abspath(sys.argv[1])
print(f'scanning {directory}')
subfolders, files = run_fast_scandir(directory)
