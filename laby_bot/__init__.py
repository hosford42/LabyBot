from laby_bot.bot import Navigator, drop_and
from laby_bot.robot import Exit, Web, Void, Rock, Unknown, say, escape, Wall


def main():
    navigator = Navigator()

    while True:
        navigator.look()

        if navigator.carrying_rock:
            preferences = (Exit, Web, Void, Rock, Unknown, None)
        else:
            preferences = (Exit, Void, Rock, Unknown, None)

        unvisited = set(navigator.iter_unvisited(preferences))
        if not unvisited:
            say("I'm trapped!")
            return

        nearest = min(unvisited,
                      key=lambda position: (
                              navigator.distance_to(position) *
                              navigator.distance_to(position, navigator.last_explored_position)
                      ))
        # say("Nearest distance: %s" % (navigator.distance_to(nearest),))
        for direction in navigator.directions_to(nearest):
            seen = navigator.look(direction)
            if seen == Exit:
                say("Aha!")
                navigator.turn(direction)
                drop_and(navigator, escape)
                return
            elif seen in (Void, Unknown):
                navigator.move(direction)
                break
            elif seen == Rock:
                if navigator.carrying_rock:
                    say("Hmm...")
                navigator.turn(direction)
                assert drop_and(navigator, lambda: navigator.take(direction))
                navigator.move(direction)
                break
            elif navigator.carrying_rock and seen == Web:
                navigator.clear(direction)
                say("Ha!")
                navigator.move(direction)
            elif seen != Wall:
                say("Nope!")
