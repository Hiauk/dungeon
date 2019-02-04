import tcod as libt

def handle_keys(key):
    # movement keys
    if key.vk == libt.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libt.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libt.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libt.KEY_RIGHT:
        return {'move': (1, 0)}

    if key.vk == libt.KEY_ENTER and key.lalt:
        # alt+enter: toggle fullscreen
        return {'fullscreen': True}
    elif key.vk == libt.KEY_ESCAPE:
        # exit the game
        return {'exit': True}

    # if no key is pressed
    return {}
