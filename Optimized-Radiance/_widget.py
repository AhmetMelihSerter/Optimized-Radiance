"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""
# Standard library
import os
# Packages
# Project Modules
from . import _utils as utils
from ._tkinter import tk
from ._utils import get_file_directory


class ThemedWidget(object):
    """
    Provides functions to manipulate themes in order to reduce code
    duplication in the ThemedTk and ThemedStyle classes.
    """

    pixmap_themes = [
        "radiance"
    ]

    def __init__(self, tk_interpreter, gif_override=False):
        """
        Initialize attributes and call _load_themes
        :param tk_interpreter: tk interpreter for tk.Widget that is
            being initialized as ThemedWidget. Even if this Widget is
            just a single widget, the changes affect all widgets with
            the same parent Tk instance.
        """
        self.tk = tk_interpreter

        # Change working directory temporarily to allow Tcl to work
        self.png_support = True and not gif_override
        if tk.TkVersion <= 8.5 and not gif_override:
            self.png_support = False
            try:
                from tkimg import load_tkimg_into_interpreter
                load_tkimg_into_interpreter(self.tk)
                self.png_support = True
            except (ImportError, tk.TclError):
                pass
        self._load_themes()

    def _load_themes(self):
        """Load the themes into the Tkinter interpreter"""
        with utils.temporary_chdir(utils.get_file_directory()):
            self.tk.eval("source themes/pkgIndex.tcl")


    def set_theme(self, theme_name):
        """
        Set new theme to use. Uses a direct tk call to allow usage
        of the themes supplied with this package.
        :param theme_name: name of theme to activate
        """
        self.tk.call("package", "require", "ttkthemes")
        self.tk.call("ttk::setTheme", theme_name)