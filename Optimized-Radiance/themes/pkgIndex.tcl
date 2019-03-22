# Author: RedFantom
# License: GNU GPLv3
# Copyright (c) 2017-2018 RedFantom

set themesdir [file join [pwd] [file dirname [info script]]]
lappend auto_path $themesdir
package provide ttkthemes 1.0
source [file join $themesdir radiance radiance.tcl]

