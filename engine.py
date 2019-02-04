import tcod as libt

from entity import Entity
from input_handlers import handle_keys
from render_functions import clear_all, render_all

def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libt.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libt.yellow)
    entities = [npc, player]

    libt.console_set_custom_font('consolas10x10_gs_tc.png', libt.FONT_TYPE_GREYSCALE | libt.FONT_LAYOUT_TCOD)

    libt.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

    con = libt.console_new(screen_width, screen_height)

    key = libt.Key()
    mouse = libt.Mouse()

    while not libt.console_is_window_closed():
        libt.sys_check_for_event(libt.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, screen_width, screen_height)
        libt.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libt.console_set_fullscreen(not libt.console_is_fullscreen())

if __name__ == '__main__':
    main()
