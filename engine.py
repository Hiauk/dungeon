import tcod as libt

from entity import Entity
from fov_functions import initialize_fov, recompute_fov
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import clear_all, render_all

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    colors = {
        'dark_wall': libt.Color(0, 0, 100),
        'dark_ground': libt.Color(50, 50, 150),
        'light_wall': libt.Color(130, 110, 50),
        'light_ground': libt.Color(200, 180, 50) 
    }

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libt.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libt.yellow)
    entities = [npc, player]

    libt.console_set_custom_font('consolas10x10_gs_tc.png', libt.FONT_TYPE_GREYSCALE | libt.FONT_LAYOUT_TCOD)

    libt.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

    con = libt.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

    fov_recompute = True

    fov_map = initialize_fov(game_map)

    key = libt.Key()
    mouse = libt.Mouse()

    while not libt.console_is_window_closed():
        libt.sys_check_for_event(libt.EVENT_KEY_PRESS, key, mouse)

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)
        libt.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
                fov_recompute = True

        if exit:
            return True

        if fullscreen:
            libt.console_set_fullscreen(not libt.console_is_fullscreen())

if __name__ == '__main__':
    main()
