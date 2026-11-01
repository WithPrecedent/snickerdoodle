"""Generates the API reference pages and navigation.

Only public objects are documented. They are the names in the `__all__` of
each package in "src" or, if a package has no `__all__`, its names that do
not start with "_" (leaving out submodules and names imported from other
packages). Each object gets one page, under the name that users import it
by (such as `package.Name` instead of `package.module.Name`), so it
appears only once.

"""

from __future__ import annotations

import pathlib

import griffe
import mkdocs_gen_files

SOURCE = pathlib.Path('src')


def _get_public_names(package: griffe.Module) -> list[str]:
    """Returns the names of the public objects in `package`.

    Args:
        package: package loaded by `griffe`.

    Returns:
        The names in `__all__` or, if there is no `__all__`, the names that
            do not start with "_" and are not submodules or imports from
            other packages.

    """
    if package.exports is not None:
        return list(package.exports)
    names = []
    for name, member in package.members.items():
        if name.startswith('_'):
            continue
        if member.is_alias:
            if not member.target_path.startswith(f'{package.name}.'):
                continue
        elif member.is_module:
            continue
        names.append(name)
    return names


packages = sorted(path.parent.name for path in SOURCE.glob('*/__init__.py'))
nav = mkdocs_gen_files.Nav()
for package_name in packages:
    package = griffe.load(package_name, search_paths = [str(SOURCE)])
    for name in _get_public_names(package):
        # With one package, its objects are listed directly under "API".
        parts = (name,) if len(packages) == 1 else (package_name, name)
        doc_path = pathlib.Path(*parts).with_suffix('.md')
        full_doc_path = pathlib.Path('reference', doc_path)
        nav[parts] = doc_path.as_posix()
        with mkdocs_gen_files.open(full_doc_path, 'w') as page:
            page.write(f'::: {package_name}.{name}\n')
        source_path = package[name].relative_filepath
        mkdocs_gen_files.set_edit_path(
            full_doc_path, pathlib.Path('..', source_path))

with mkdocs_gen_files.open('reference/SUMMARY.md', 'w') as nav_file:
    nav_file.writelines(nav.build_literate_nav())
