import tcod as libt

def render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libt.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        libt.console_set_char_background(con, x, y, colors.get('light_wall'), libt.BKGND_SET)
                    else:
                        libt.console_set_char_background(con, x, y, colors.get('light_ground'), libt.BKGND_SET)
                else:
                    if wall:
                        libt.console_set_char_background(con, x, y, colors.get('dark_wall'), libt.BKGND_SET)
                    else:
                        libt.console_set_char_background(con, x, y, colors.get('dark_ground'), libt.BKGND_SET)
    
    # draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)

    libt.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity):
    libt.console_set_default_foreground(con, entity.color)
    libt.console_put_char(con, entity.x, entity.y, entity.char, libt.BKGND_NONE)

def clear_entity(con, entity):
    # erase the character that represents this object
    libt.console_put_char(con, entity.x, entity.y, ' ', libt.BKGND_NONE)
