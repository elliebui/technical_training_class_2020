import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_file = os.listdir(path)
    output = []

    for item in list_file:
        full_path = os.path.join(path, item)
        if os.path.isfile(os.path.join(path, item)):
            if full_path.endswith(suffix):
                output.append(full_path)
        else:
            output += find_files(suffix, full_path)

    return output


print(find_files(".c", "./testdir"))
"""
Answer:
['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
"""