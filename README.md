# Minecraft Enchantment Table Grind

A quick hack that automates the clicking of the enchantment table until you get
a desired level.

Run e.g. `./update-pattern num-{2,5}.png` to get level-25 enchantments in the
future. (Requires [GraphicsMagick](http://www.graphicsmagick.org/).)

Put an item on the enchantment table and run ench.sikuli in
[Sikuli](http://sikuli.org/). When it asks you to select a region on the
screen, select an area that contains the “Enchant” title text, the three
enchantment choices and a few pixels of margin around all of that.

Make sure your Minecraft UI uses a matching zoom level with
ench.sikuli/Enchant-title.png and ench.sikuli/num.png.
