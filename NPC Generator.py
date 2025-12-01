names = {"Arindor", "Lyssara", "Thornak", "Veloria", "Dravenor",
        "Seraphel", "Mornak", "Ylendra", "Kaelor", "Sylvran",
        "Eldamir", "Ravessia", "Torvak", "Nymera", "Falkorin",
        "Isyriel", "Bramdor", "Zaleth", "Aerwyn", "Korvash"}

Races = {"Human", "Elf", "Dwarf", "Halfling", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"}

appearances = {"Scarred", "Tattooed", "Bearded", "Bald", "Long-haired",
        "Braided-hair", "Pointed-ears", "Glowing-eyes", "Pierced",
        "Freckled", "Tall", "Short", "Muscular", "Slender",
        "Weathered", "Elegant", "Shaggy", "Wild-eyed", "Stoic", "Graceful"}

Traits = {"Old: Your character is old for their race.", 
          "Young: Your character is young for their race.", "Wrathful: Your character is emotional, and does not like insults. AT ALL.",
          "Calm: Your character remains calm even when everything is going to s***. Others might view them as robotic."
          "Scarred: Your character carries visible scars that hint at past battles.",
        "Sharp-Eyed: Your character notices small details others often miss.",
        "Soft-Spoken: Your character speaks quietly, choosing words carefully.",
        "Hot-Blooded: Your character reacts quickly and passionately to events.",
        "Stoic: Your character rarely shows emotion, maintaining a calm demeanor.",
        "Superstitious: Your character strongly believes in omens and signs.",
        "Broad-Shouldered: Your character has a powerful, imposing build.",
        "Silver-Tongued: Your character is charming and persuasive in conversation.",
        "Night-Owl: Your character feels most alive during late hours.",
        "Absent-Minded: Your character often drifts into thoughts and forgets small details."}

def Generating():
    print("Name: ", names.pop())
    print("Race: ", Races.pop())
    print("Appearance: ", appearances.pop())
    print("Character Trait: ", Traits.pop())

Generating()