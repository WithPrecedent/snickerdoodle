"""Script to generate the project's credits.

This code is adapted from pawamoy's packages. See, e.g.,
https://github.com/pawamoy/duty/blob/main/scripts/gen_credits.py.
"""

from __future__ import annotations

import re
from importlib.metadata import PackageNotFoundError, metadata
from itertools import chain
from pathlib import Path
from textwrap import dedent
from typing import Mapping, cast

import toml
from jinja2 import StrictUndefined
from jinja2.sandbox import SandboxedEnvironment


project_dir = Path(".")
pyproject = toml.load(project_dir / "pyproject.toml")
project = pyproject["project"]
uv = pyproject["tool"]["uv"]
lock_data = toml.load(project_dir / "uv.lock")
lock_pkgs = {pkg["name"].lower(): pkg for pkg in lock_data["package"]}
project_name = project["name"]
regex = re.compile(r"(?P<dist>[\w.-]+)(?P<spec>.*)$")


def _get_license(pkg_name: str) -> str:
    try:
        data = metadata(pkg_name)
    except PackageNotFoundError:
        return "?"
    license_name = cast(dict, data).get("License", "").strip()
    multiple_lines = bool(license_name.count("\n"))
    if multiple_lines or not license_name or license_name == "UNKNOWN":
        for header, value in cast(dict, data).items():
            if header == "Classifier" and value.startswith("License ::"):
                license_name = value.rsplit("::", 1)[1].strip()
    return license_name or "?"


def _get_deps(
    base_deps: Mapping[str, Mapping[str, str]]) -> dict[str, dict[str, str]]:
    deps = {}
    for dep in base_deps:
        parsed = regex.match(dep).groupdict()  # type: ignore[union-attr]
        dep_name = parsed["dist"].lower()
        if dep_name not in lock_pkgs:
            continue
        deps[dep_name] = {
            "license": _get_license(dep_name),
            **parsed,
            **lock_pkgs[dep_name]}
    again = True
    while again:
        again = False
        for pkg_name in lock_pkgs:
            if pkg_name in deps:
                for pkg_dependency in lock_pkgs[pkg_name].get(
                    "dependencies", []):
                    parsed = regex.match(pkg_dependency).groupdict()  # type: ignore[union-attr]
                    dep_name = parsed["dist"].lower()
                    if (dep_name in lock_pkgs
                        and dep_name not in deps
                        and dep_name != project["name"]):
                        deps[dep_name] = {
                            "license": _get_license(dep_name),
                            **parsed,
                            **lock_pkgs[dep_name]}
                        again = True
    return deps


def _render_credits() -> str:
    dev_dependencies = _get_deps(
        chain(*uv.get("dev-dependencies", {}).values()))  # type: ignore[arg-type]
    prod_dependencies = _get_deps(
        chain(  # type: ignore[arg-type]
            project.get("dependencies", []),
            chain(*project.get("dependency-groups", {}).values()),),)

    template_data = {
        "project_name": project_name,
        "prod_dependencies": sorted(
            prod_dependencies.values(), key=lambda dep: dep["name"]),
        "dev_dependencies": sorted(
            dev_dependencies.values(), key=lambda dep: dep["name"]),
        "more_credits": "",}
    template_text = dedent(
        """
        These projects were used to build *{{ project_name }}*. **Thank you!**

        [`python`](https://www.python.org/) |
        [`uv`](https://docs.astral.sh/uv/)

        {% macro dep_line(dep) -%}
        [`{{ dep.name }}`](https://pypi.org/project/{{ dep.name }}/) | {{ dep.summary }} | {{ ("`" ~ dep.spec ~ "`") if dep.spec else "" }} | `{{ dep.version }}` | {{ dep.license }}
        {%- endmacro %}

        ### Runtime dependencies

        Project | Summary | Version (accepted) | Version (last resolved) | License
        ------- | ------- | ------------------ | ----------------------- | -------
        {% for dep in prod_dependencies -%}
        {{ dep_line(dep) }}
        {% endfor %}

        ### Development dependencies

        Project | Summary | Version (accepted) | Version (last resolved) | License
        ------- | ------- | ------------------ | ----------------------- | -------
        {% for dep in dev_dependencies -%}
        {{ dep_line(dep) }}
        {% endfor %}

        {% if more_credits %}**[More credits from the author]({{ more_credits }})**{% endif %}
        """,)
    jinja_env = SandboxedEnvironment(undefined=StrictUndefined)
    return jinja_env.from_string(template_text).render(**template_data)


print(_render_credits())
