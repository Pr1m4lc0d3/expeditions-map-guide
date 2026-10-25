FOB MODULE ART TEMPLATE
=======================

Four images, four sizes, four different crops. Replace MODNAME with your
module's name and paint inside the blanks.

FILES YOU EDIT

  MODNAME_bg.png   380 x 92
      Appears: Store list row, and the sell dialog
      Fit:     Fills the row height and CLIPS OFF THE LEFT EDGE. Keep anything that must be readable in the right two thirds.

  MODNAME_popup.png   380 x 92
      Appears: Purchase card
      Fit:     The WHOLE image is shown. Nothing is cropped.

  MODNAME_right.png   760 x 90
      Appears: Banner above the module card when the module is in use
      Fit:     Artwork sits at the RIGHT. The icon and module name are drawn over the left end, so keep that end clear.

  MODNAME_small.png   124 x 52
      Appears: HUD strip of deployed modules
      Fit:     A tight CENTRED crop that fills the chip. Cropped on every side.

THE .ora FILES  <-- START HERE
  A layered file for each slot, with three layers:

      GUIDE - hide before export     the red unusable area
      YOUR ART - paint here          empty, paint in this one
      SAMPLE - delete this           a real vanilla module for scale

  Open it, delete the sample, paint on YOUR ART, hide the guide, export as
  PNG at the same size. Opens in:

      GIMP        free       gimp.org
      Krita       free       krita.org
      Photopea    free       photopea.com   (runs in a browser, no install,
                                             and can export PSD if you want one)

THE _guide_ FILES
  Same sizes, with the unusable area shaded red. Design against these, then
  export at the same size without the guide.

  Red means "keep important detail out of here", for one of two reasons:
    bg      the game CROPS this off the left edge
    right   the icon and module name are DRAWN OVER this end
    small   the chip crops a margin on every side
    popup   nothing is shaded: the whole image is shown

WHERE THEY GO IN YOUR MOD
  ui/textures/MODNAME_bg.png
  ui/textures/MODNAME_popup.png
  ui/textures/MODNAME_right.png
  ui/textures/MODNAME_small.png

HOW YOU REFERENCE THEM
  In the module descriptor, name them WITHOUT the folder and WITHOUT .png:

      "bg":            "MODNAME_bg",
      "popupModuleBg": "MODNAME_popup",
      "bgRight":       "MODNAME_right",
      "bgSmall":       "MODNAME_small",

  Only these four may be your own files. The icon fields (iconMap40,
  iconTrade, icon20, icon40, iconModuleBg, tradeArrowsSpecialIcon,
  uiDescTradeHeaderIcon) take a symbol from the game's own UI bundle. A PNG
  you ship in an icon field will NOT render.

IF YOU SEE A YELLOW SQUARE WITH A RED MOUNTAIN
  The name did not resolve. Check for a typo, a stray .png in the descriptor,
  or a file that is not actually inside the pak.
