# Introduction
Diagram (Blender-Diagram on GitHub) is a [Blender](https://www.blender.org/) add-on that generates animated diagrams, or graphs, from data tables.

# Usage
This add-on lets you import Comma Separated Values (.csv) into Blender. First, go to the File -> Import menu and click Table data. Browse to and choose the file containing the data. Now, select the options for how you want the data to appear.

## Appropriate data
| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| --- | --- | --- | --- | --- |
| Name of bar 1 | Value key frame 1 | Value key frame 2 | ... | Value key frame *n* |
| Name of bar 2 | Value key frame 1 | Value key frame 2 | ... | Value key frame *n* |
| ... | ... | ... | ... | ... |
| Name of bar *n* | Value key frame 1 | Value key frame 2 | ... | Value key frame *n* |
Value should be numeric with a dot (".") as decimal delimiter.

# Installation
Blender offers [instructions for installing 3rd party add-ons](https://www.blender.org/manual/advanced/scripting/python/add_ons.html#installation-of-a-3rd-party-add-on).

# License
Diagram is released under the GNU General Public License. See LICENSE for details.
