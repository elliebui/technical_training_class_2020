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
    list_file = os.listdir(path)  # Time complexity: O(1)
    output = []

    for item in list_file:  # Time complexity: O(N)
        full_path = os.path.join(path, item)  # Time complexity: O(1)
        if os.path.isfile(full_path):  # Time complexity: O(1)
            if full_path.endswith(suffix):  # Time complexity: O(1)
                output.append(full_path)  # Time complexity: O(1)
        else:
            output += find_files(suffix, full_path)   # Time complexity: O(N)

    return output
    # Time complexity: O(N^2)


print(find_files(".c", "./testdir"))
"""
Answer:
['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
"""