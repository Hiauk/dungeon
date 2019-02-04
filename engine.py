import tcod as libt
from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    libt.console_set_custom_font('consolas10x10_gs_tc.png', libt.FONT_TYPE_GREYSCALE | libt.FONT_LAYOUT_TCOD)

    libt.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

    con = libt.console_new(screen_width, screen_height)

    key = libt.Key()
    mouse = libt.Mouse()

    while not libt.console_is_window_closed():
        libt.sys_check_for_event(libt.EVENT_KEY_PRESS, key, mouse)
        libt.console_set_default_foreground(con, libt.white)
        libt.console_put_char(con, player_x, player_y, '@', libt.BKGND_NONE)
        libt.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libt.console_flush()

        libt.console_put_char(con, player_x, player_y, ' ', libt.BKGND_NONE)

        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit:
            return True

        if fullscreen:
            libt.console_set_fullscreen(not libt.console_is_fullscreen())

if __name__ == '__main__':
    main()
