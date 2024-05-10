import os


def generate_tree(root_dir, prefix=""):
    """
    Recursively generate a directory tree string.
    :param root_dir: The root directory to generate the tree for.
    :param prefix: A prefix used for the current level, used for recursive calls.
    :return: A string representing the directory tree.
    """
    tree_str = ""
    files = sorted(os.listdir(root_dir))
    for index, name in enumerate(files):
        # Skip specific directories
        if name in ['.git', '.github', 'scripts']:
            continue
        path = os.path.join(root_dir, name)
        if os.path.isdir(path):
            # Print directory
            tree_str += f"{prefix}+-- {name}/\n"
            if index == len(files) - 1:
                new_prefix = prefix + "    "
            else:
                new_prefix = prefix + "|   "
            tree_str += generate_tree(path, new_prefix)
        else:
            # Print file
            tree_str += f"{prefix}+-- {name}\n"
    return tree_str


def update_readme(root_dir, readme_path='README.md'):
    """
    Update the README file with a tree-like structure of the directory.
    :param root_dir: The directory to document.
    :param readme_path: The path to the README file.
    """
    # Generate the directory tree
    directory_tree = generate_tree(root_dir)

    # Update the README file
    with open(readme_path, 'w') as readme_file:
        readme_file.write("# Project Directory Structure\n\n")
        readme_file.write("```\n")
        readme_file.write(directory_tree)
        readme_file.write("```\n")


if __name__ == "__main__":
    # Update the README.md with the tree of the current directory
    update_readme('.')
    print("README has been updated with the directory structure.")
