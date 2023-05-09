import unittest

bedroll = {
    "name": "Bedroll",
    "weight": 7,
    "condition": "Good",
    "value": 1,
    "properties": "A bedroll is a simple but essential item for adventurers who need to sleep outdoors. It provides a soft and comfortable surface to sleep on, as well as some insulation against the cold or damp ground. When rolled up, it is compact and easy to carry, making it a convenient addition to any adventurer's gear."
}
spellbook = {
    "name": "Spellbook",
    "weight": 3,
    "condition": "Good",
    "value": 50,
    "properties": "A spellbook is a wizard's most important possession, containing all of the spells they have learned and the formulae to prepare them. Alice's spellbook contains a variety of spells, including some that she has prepared for the day and others that she has yet to learn. The spellbook is carefully maintained and protected, as its loss would be a serious setback for Alice's magical studies."
}

wand_of_magic_missiles = {
    "name": "Wand of Magic Missiles",
    "weight": 1,
    "condition": "Good",
    "value": 375,
    "properties": "A wand of magic missiles is a powerful arcane device that can unleash bolts of magical force at its target. Alice's wand can cast the magic missile spell, which automatically hits its target and deals force damage. The wand has a limited number of charges, and can be recharged by spending gold and time at a wizard's workshop."
}

ring_of_protection = {
    "name": "Ring of Protection",
    "weight": 0,
    "condition": "Good",
    "value": 2000,
    "properties": "A ring of protection is a magical item that enhances the wearer's defenses. Alice's ring provides a +1 bonus to her Armor Class and all saving throws, making her harder to hit and more resilient to spells and other attacks. The ring is a valuable and sought-after item, and would be a valuable asset to any adventurer."
}

rations = {
    "name": "Rations",
    "weight": 2,
    "condition": "Good",
    "value": 5,
    "properties": "Rations are a basic food supply that adventurers carry with them on their journeys. Alice's rations consist of dried meat, bread, and fruit, and are enough to sustain her for several days. They are carefully stored and packed to prevent spoilage, and are an essential part of Alice's survival kit."
}

waterskin = {
    "name": "Waterskin",
    "weight": 5,
    "condition": "Good",
    "value": 1,
    "properties": "A waterskin is a container used to carry drinking water on long journeys. Alice's waterskin is made of sturdy leather and can hold up to a gallon of water. It is carefully filled and stored to prevent spills and leaks, and is an essential part of Alice's survival kit."
}

alice_items = [spellbook, wand_of_magic_missiles, ring_of_protection, rations, waterskin]

chain_mail = {
    "name": "Chain Mail",
    "armor_class": 16,
    "strength_requirement": 13,
    "stealth_disadvantage": True,
    "weight": 55
}

mace = {
    "name": "Mace",
    "damage": "1d6 bludgeoning",
    "properties": ["Versatile (1d8)", "Light"],
    "weight": 4
}

shield = {
    "name": "Shield",
    "armor_class": 2,
    "weight": 6
}

holy_symbol = {
    "name": "Holy Symbol",
    "description": "A silver amulet depicting a sunburst",
    "weight": 1
}

eve_items = [chain_mail, mace, shield, holy_symbol]

chain_mail = {
    'name': 'Chain Mail',
    'weight': 40.0,
    'value': 150.0,
    'armor_class': 16,
    'max_dex_bonus': 2,
    'armor_check_penalty': -5,
    'spell_failure_chance': 30,
    'speed': 10
}

mace = {
    "name": "Mace",
    "type": "Weapon",
    "subtype": "Bludgeoning",
    "damage": "1d8",
    "critical": "x2",
    "weight": 8.0,
    "value": 308.0,
    "condition": "Good"
}

quarterstaff = {
    "name": "Quarterstaff",
    "type": "Weapon",
    "subtype": "Bludgeoning",
    "damage": "1d6",
    "critical": "x2",
    "weight": 4.0,
    "value": 0.0,
    "condition": "Excellent"
}



chain_mail = ArmorItem(
    name='Chain mail',
    weight=40,
    value=150,
    armor_class=5,
    max_dex_bonus=2,
    check_penalty=-5,
    spell_failure=30,
    speed_reduction=10
)
print(chain_mail.to_dict())

# Output:
# {
#     'name': 'Chain mail',
#     'weight': 40,
#     'value': 150,
#     'condition': 'new',
#     'armor_class': 5,
#     'max_dex_bonus': 2,
#     'check_penalty': -5,
#     'spell_failure': 30,
#     'speed_reduction': 10
# }

crossbow = {
    "name": "Heavy Crossbow",
    "type": "ranged",
    "subtype": "crossbow",
    "damage": "1d10",
    "critical": "19-20/x2",
    "range": "120 ft.",
    "weight": 8,
    "value": 50,
    "condition": "new"
}

ring_of_protection_dict = {
    "name": "Ring of Protection",
    "weight": 0.1,
    "value": 200,
    "condition": "Good",
    "magic_bonus": 1,
    "effect": "This ring grants a +1 deflection bonus to AC."
}

import unittest


class TestInventoryItem(unittest.TestCase):
    def test_init(self):
        item = InventoryItem(name="Spellbook", weight=3, description="A book of spells.")
        self.assertEqual(item.name, "Spellbook")
        self.assertEqual(item.weight, 3)
        self.assertEqual(item.description, "A book of spells.")
        self.assertEqual(item.condition, "new")
        self.assertEqual(item.value, 0)

        item = InventoryItem(name="Wand of Magic Missiles", weight=1, description="A wand that shoots magic missiles.")
        self.assertEqual(item.name, "Wand of Magic Missiles")
        self.assertEqual(item.weight, 1)
        self.assertEqual(item.description, "A wand that shoots magic missiles.")
        self.assertEqual(item.condition, "new")
        self.assertEqual(item.value, 0)

    def test_to_dict(self):
        item = InventoryItem(name="Spellbook", weight=3, description="A book of spells.")
        expected_dict = {
            "name": "Spellbook",
            "weight": 3,
            "description": "A book of spells.",
            "condition": "new",
            "value": 0
        }
        self.assertDictEqual(item.to_dict(), expected_dict)

        item = InventoryItem(name="Wand of Magic Missiles", weight=1, description="A wand that shoots magic missiles.",
                             value=100)
        expected_dict = {
            "name": "Wand of Magic Missiles",
            "weight": 1,
            "description": "A wand that shoots magic missiles.",
            "condition": "new",
            "value": 100
        }
        self.assertDictEqual(item.to_dict(), expected_dict)

    def test_from_dict(self):
        dict_data = {
            "name": "Spellbook",
            "weight": 3,
            "description": "A book of spells.",
            "condition": "used",
            "value": 50
        }
        item = InventoryItem.from_dict(dict_data)
        self.assertEqual(item.name, "Spellbook")
        self.assertEqual(item.weight, 3)
        self.assertEqual(item.description, "A book of spells.")
        self.assertEqual(item.condition, "used")
        self.assertEqual(item.value, 50)

        dict_data = {
            "name": "Wand of Magic Missiles",
            "weight": 1,
            "description": "A wand that shoots magic missiles.",
            "value": 100
        }
        item = InventoryItem.from_dict(dict_data)
        self.assertEqual(item.name, "Wand of Magic Missiles")
        self.assertEqual(item.weight, 1)
        self.assertEqual(item.description, "A wand that shoots magic missiles.")
        self.assertEqual(item.condition, "new")
        self.assertEqual(item.value, 100)

import unittest
from inventory_item import ArmorItem

class TestArmorItem(unittest.TestCase):

    def test_from_dict(self):
        item_dict = {
            "name": "Chain mail",
            "item_type": "armor",
            "armor_type": "medium",
            "ac_bonus": 5,
            "max_dex_bonus": 2,
            "check_penalty": -5,
            "spell_failure": 30,
            "speed_penalty": -5,
            "weight": 40,
            "value": 150,
            "condition": "new"
        }

        item = ArmorItem.from_dict(item_dict)

        self.assertEqual(item.name, "Chain mail")
        self.assertEqual(item.item_type, "armor")
        self.assertEqual(item.armor_type, "medium")
        self.assertEqual(item.ac_bonus, 5)
        self.assertEqual(item.max_dex_bonus, 2)
        self.assertEqual(item.check_penalty, -5)
        self.assertEqual(item.spell_failure, 30)
        self.assertEqual(item.speed_penalty, -5)
        self.assertEqual(item.weight, 40)
        self.assertEqual(item.value, 150)
        self.assertEqual(item.condition, "new")

    def test_to_dict(self):
        item = ArmorItem(
            "Chain mail",
            "armor",
            "medium",
            5,
            2,
            -5,
            30,
            -5,
            40,
            150,
            "new"
        )

        item_dict = item.to_dict()

        self.assertEqual(item_dict["name"], "Chain mail")
        self.assertEqual(item_dict["item_type"], "armor")
        self.assertEqual(item_dict["armor_type"], "medium")
        self.assertEqual(item_dict["ac_bonus"], 5)
        self.assertEqual(item_dict["max_dex_bonus"], 2)
        self.assertEqual(item_dict["check_penalty"], -5)
        self.assertEqual(item_dict["spell_failure"], 30)
        self.assertEqual(item_dict["speed_penalty"], -5)
        self.assertEqual(item_dict["weight"], 40)
        self.assertEqual(item_dict["value"], 150)
        self.assertEqual(item_dict["condition"], "new")

import unittest
from inventory import WeaponItem

class TestWeaponItem(unittest.TestCase):
    def setUp(self):
        self.mace = WeaponItem("Mace", "Melee", 6, "1d6", "Bludgeoning")

    def test_init(self):
        self.assertEqual(self.mace.name, "Mace")
        self.assertEqual(self.mace.category, "Melee")
        self.assertEqual(self.mace.weight, 6)
        self.assertEqual(self.mace.damage, "1d6")
        self.assertEqual(self.mace.damage_type, "Bludgeoning")

    def test_to_dict(self):
        expected = {
            "name": "Mace",
            "category": "Melee",
            "weight": 6,
            "damage": "1d6",
            "damage_type": "Bludgeoning"
        }
        self.assertEqual(self.mace.to_dict(), expected)

    def test_from_dict(self):
        data = {
            "name": "Mace",
            "category": "Melee",
            "weight": 6,
            "damage": "1d6",
            "damage_type": "Bludgeoning"
        }
        mace = WeaponItem.from_dict(data)
        self.assertEqual(mace.name, "Mace")
        self.assertEqual(mace.category, "Melee")
        self.assertEqual(mace.weight, 6)
        self.assertEqual(mace.damage, "1d6")
        self.assertEqual(mace.damage_type, "Bludgeoning")

import unittest

class TestMagicRing(unittest.TestCase):

    def test_init(self):
        # Test initialization of MagicRing object
        ring = MagicRing(name="Ring of Protection", value=100, condition=90, magic_type="protection", bonus=2)
        self.assertEqual(ring.name, "Ring of Protection")
        self.assertEqual(ring.value, 100)
        self.assertEqual(ring.condition, 90)
        self.assertEqual(ring.magic_type, "protection")
        self.assertEqual(ring.bonus, 2)

    def test_to_dict(self):
        # Test conversion of MagicRing object to dictionary
        ring = MagicRing(name="Ring of Protection", value=100, condition=90, magic_type="protection", bonus=2)
        ring_dict = ring.to_dict()
        expected_dict = {
            "name": "Ring of Protection",
            "value": 100,
            "condition": 90,
            "magic_type": "protection",
            "bonus": 2
        }
        self.assertDictEqual(ring_dict, expected_dict)

    def test_from_dict(self):
        # Test conversion of dictionary to MagicRing object
        ring_dict = {
            "name": "Ring of Protection",
            "value": 100,
            "condition": 90,
            "magic_type": "protection",
            "bonus": 2
        }
        ring = MagicRing.from_dict(ring_dict)
        self.assertEqual(ring.name, "Ring of Protection")
        self.assertEqual(ring.value, 100)
        self.assertEqual(ring.condition, 90)
        self.assertEqual(ring.magic_type, "protection")
        self.assertEqual(ring.bonus, 2)


if __name__ == '__main__':
    unittest.main()
