"""Keeps section markers from being read as attribute docstrings.

Members are grouped with string section markers (such as
`\"\"\" Class Methods \"\"\"`). When a marker follows an attribute, `griffe`
reads it as that attribute's docstring, so the attribute appears in the
documentation with the marker as its description. This extension removes
those docstrings.

Contents:
    SectionMarkers: `griffe` extension that removes section marker
        docstrings from attributes.

"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

import griffe

if TYPE_CHECKING:
    import ast

# Matches a one-line string with spaces inside its quotes (such as
# `""" Public Methods """`), which ordinary docstrings do not have.
_MARKER = re.compile(r'\s*("""|\'\'\') \S.*\S \1\s*')


class SectionMarkers(griffe.Extension):
    """Removes section marker docstrings from attributes."""

    """ Public Methods """

    def on_attribute_instance(
            self,
            *,
            node: ast.AST | griffe.ObjectNode,
            attr: griffe.Attribute,
            agent: griffe.Visitor | griffe.Inspector,
            **kwargs: Any) -> None:
        """Removes the docstring of `attr` if it is a section marker.

        Args:
            node: node that `attr` was created from.
            attr: attribute to check.
            agent: `griffe` visitor or inspector that found `attr`.
            **kwargs: other arguments from `griffe`, which are not used.

        """
        if attr.docstring and _MARKER.fullmatch(attr.docstring.source):
            attr.docstring = None
