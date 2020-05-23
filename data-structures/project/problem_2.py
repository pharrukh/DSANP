import os

def find_files_recursive(suffix, path, coll):
    if os.path.isfile(path) and path.endswith(suffix):
        coll.append(path)
    elif os.path.isdir(path):
        for cur_path in os.listdir(path):
            new_path = os.path.join(path, cur_path)
            find_files_recursive(suffix, new_path, coll)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    coll = list()
    find_files_recursive(suffix, path, coll)
    return coll


## Test 1
file_path = 'testdir'
absolute_file_path = os.path.abspath(file_path)
print(find_files('.c', absolute_file_path))
"""
    [
        'testdir/subdir3/subsubdir1/b.c', 
        'testdir/t1.c', 
        'testdir/subdir5/a.c', 
        'testdir/subdir1/a.c'
    ]
"""
## Test 2
file_path = 'testdir/subdir1'
absolute_file_path = os.path.abspath(file_path)
print(find_files('.c', absolute_file_path))
"""
    [
        'testdir/subdir1/a.c'
    ]
"""
## Test 3
file_path = 'testdir/subdir4'
absolute_file_path = os.path.abspath(file_path)
print(find_files('.c', absolute_file_path))
"""
    []
"""
## Test 3
file_path = 'testdir'
absolute_file_path = os.path.abspath(file_path)
print(find_files('.gitkeep', absolute_file_path))
"""
    [
        'testdir/subdir4/.gitkeep', 
        'testdir/subdir2/.gitkeep'
    ]
"""