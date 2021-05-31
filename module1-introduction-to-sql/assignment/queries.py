TOTAL_CHARACTERS = 'SELECT COUNT(*) ' \
                   'from charactercreator_character'

TOTAL_SUBCLASS = 'SELECT COUNT(*) ' \
                 'from charactercreator_necromancer'

TOTAL_ITEMS = 'SELECT COUNT(*) ' \
              'from armory_item'

WEAPONS = 'SELECT COUNT(*) ' \
          'FROM armory_item, armory_weapon ' \
          'WHERE armory_item.item_id = armory_weapon.item_ptr_id'

NON_WEAPONS = 'SELECT COUNT(*) FROM armory_item, armory_weapon' \
              'WHERE armory_item.item_id != armory_weapon.item_ptr_id'

CHARACTER_ITEMS = 'SELECT COUNT(item_id) ' \
                  'FROM charactercreator_character_inventory ' \
                  'GROUP BY character_id LIMIT 20'

CHARACTER_WEAPONS = 'SELECT COUNT(item_id) ' \
                    'FROM charactercreator_character_inventory, armory_weapon ' \
                    'WHERE item_id = armory_weapon.item_ptr_id ' \
                    'GROUP BY character_id LIMIT 20'

AVG_CHARACTER_ITEMS = 'SELECT AVG(count) ' \
                      'FROM (SELECT COUNT(item_id) AS count ' \
                      'FROM charactercreator_character_inventory ' \
                      'GROUP BY character_id)'

AVG_CHARACTER_WEAPONS = 'SELECT AVG(count) ' \
                        'FROM (SELECT COUNT(item_id) as count ' \
                        'FROM charactercreator_character_inventory, armory_weapon ' \
                        'WHERE item_id = armory_weapon.item_ptr_id GROUP BY character_id)'

