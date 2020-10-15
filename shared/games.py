# (c) Copyright 2020 by Vicarious Drama.
#
# games.py
#
# Every function here is called directly by a menu item. They should all be async.
#
import ckcc, pyb, version
from ux import ux_show_story, the_ux, ux_confirm, ux_dramatic_pause, ux_poll_once, ux_aborted
from ux import ux_enter_number, ux_wait_keyup, PressRelease
from utils import imported, pretty_short_delay
from main import settings
from uasyncio import sleep_ms
from files import CardSlot, CardMissingError
from utils import xfp2str
from main import pa, settings, dis, loop, numpad
from actions import *
from callgate import get_dfu_button, get_is_bricked, get_genuine, clear_genuine


async def game_blackjack(*a):
    await show_nickname('BLACK JACK')

async def game_chess(*a):
    await show_nickname('CHESS')

async def game_memory(*a):
    await show_nickname('MEMORY MATCH')

async def game_numberguess(*a):
    await show_nickname('NUMBER GUESS')

async def game_passthepigs(*a):
    await show_nickname('PASS THE PIGS')

async def game_snake(*a):
    await show_nickname('SNAKE')

async def game_spacerace(*a):
    await show_nickname('SPACE RACE')

async def game_tacopleb(*a):
    from main import dis
    from display import FontTiny, FontLarge

    show_nickname('TACO PLEB')
    await sleep_ms(500)
    show_nickname('woot woot')
    await sleep_ms(2500)
    pr = PressRelease()
    # fixed parts of screen
    dis.clear()
    y = 38
    dis.text(0, y, "Press 7 or 9"); y += 13
    dis.text(0, y, "to change lane.")
    dis.save()
    dis.show()
    x = 4
    y = 20
    # arrow_down, arrow_up, box, scroll, selected, sm_box, space, spin, wedge, xbox
    while 1:
        dis.clear()
        ch = await pr.wait()
        if ch == '1':
            dis.icon(x-2, y-10, 'spin')
        elif ch == '2':
            dis.icon(x-2, y-10, 'wedge')
        elif ch == '3':
            dis.icon(x-2, y-10, 'box')
        elif ch == '4':
            dis.icon(x-2, y-10, 'sm_box')
        elif ch == '5':
            dis.icon(x-2, y-10, 'arrow_up')
        elif ch == '7':
            show_nickname('<')
            dis.icon(x-2, y-10, 'spin')
            await sleep_ms(500)
        elif ch == '8':
            dis.icon(x-2, y-10, 'arrow_down')
        elif ch == '9':
            show_nickname('>')
            await sleep_ms(500)
        elif ch == 'x':
            break
        elif ch == 'y':
            break

        dis.show()
