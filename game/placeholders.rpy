# placeholders.rpy — temporary art & audio stubs
#
# Every image the prologue needs is defined here with Ren'Py's built-in
# Placeholder displayable. When real art arrives, DROP THE FILE into
# game/images/ with the same name (e.g. "bg bedroom.png") and DELETE the
# corresponding line here — the story script itself never changes.

# --- Prologue backgrounds -------------------------------------------------

image bg bedroom        = Placeholder("bg", text="BG — Bedroom, silk & canopy, 10:47 AM")
image bg bathroom       = Placeholder("bg", text="BG — Bathroom, the gilded mirror")
image bg breakfast_hall = Placeholder("bg", text="BG — Breakfast hall, table for forty")
image bg estate_night   = Placeholder("bg", text="BG — The estate, Sunday night, a suit laid out")
image bg driveway       = Placeholder("bg", text="BG — Driveway, the convertible, two spaces")
image bg lobby          = Placeholder("bg", text="BG — McQuinsey lobby, the glass lift")
image bg floor67        = Placeholder("bg", text="BG — Floor 67, corner office")
image bg coffee_point   = Placeholder("bg", text="BG — The coffee point")
image bg lift           = Placeholder("bg", text="BG — Lift, floor numbers ticking down")
image bg floor3         = Placeholder("bg", text="BG — Floor 3, smallest desk, beside the printer")
image black             = Solid("#000000")

# --- Prologue CG panels -----------------------------------------------------

image cg newspaper   = Placeholder("bg", text="CG — Front page: a yacht, a harbour, a crane")
image cg velvet_box  = Placeholder("bg", text="CG — The velvet box: the card, locked")
image cg excel       = Placeholder("bg", text="CG — Excel. The cells are winning")
image cg badge_old   = Placeholder("bg", text="CG — Badge close-up: P. VAULMONT")
image cg badge_new   = Placeholder("bg", text="CG — New badge: first name, Junior Analyst")

# --- Character sprites ------------------------------------------------------

image nestor   = Placeholder("boy",  text="Nestor — butler, white gloves")
image father   = Placeholder("boy",  text="Father — double-breasted, reading glasses")
image vergeau  = Placeholder("girl", text="Mme Vergeau — silver bob, angular glasses")
image prov     = Placeholder("boy",  text="Prov — rumpled cardigan, pencil behind ear")
image piedad   = Placeholder("girl", text="Ms Piedad — cardigan, glasses on a chain")
image maxi     = Placeholder("boy",  text="Maxi Geldmann — velvet jacket, signet ring")
image tanaka   = Placeholder("boy",  text="Tanaka san — immaculate, unreadable")
image chairman = Placeholder("boy",  text="The Chairman — white tie, eyebrows")
image waiter   = Placeholder("boy",  text="The Waiter — ancient, silver tray")

# --- Audio ------------------------------------------------------------------
# No audio yet. Scenes carry commented `# play music/sound` lines as markers;
# when tracks exist, put files in game/audio/ and uncomment.
