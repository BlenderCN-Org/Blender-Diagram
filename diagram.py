# BEGIN GPL LICENSE BLOCK #####
#
# Copyright (C) 2016  Philip Eriksson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Diagram",
    "description": "Generates animated diagram from data in file.",
    "author": "Philip Eriksson",
    "blender": (2, 76, 0),
    "category": "Import-Export",
}

import bpy


        
def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()