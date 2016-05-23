import gzip
import os
import shutil

supported_filetypes = [".js", ".css", ".html"]

for path, subdirs, files in os.walk("."):
    for name in files:
        resolved = os.path.join(path, name)
        type_flag = False
        for filetype in supported_filetypes:
            if resolved.endswith(filetype) and "static" in resolved:
                type_flag = True
        if type_flag:
            print("Zipping " + resolved)
            with open(resolved, 'rb') as f_in:
                with gzip.open(resolved + ".gz", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
