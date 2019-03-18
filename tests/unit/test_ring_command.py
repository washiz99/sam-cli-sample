from app.ring_command import RingCommand


def test_turn_next(config_json):
    ring = RingCommand(config_json)

    status = ring.turn_next()
    assert status == 2

    status = ring.turn_next()
    assert status == 3

    status = ring.turn_next()
    assert status == 1


def test_turn_prev(config_json):
    ring = RingCommand(config_json)

    status = ring.turn_prev()
    assert status == 3

    status = ring.turn_prev()
    assert status == 2

    status = ring.turn_prev()
    assert status == 1


def test_get_command(config_json):
    ring = RingCommand(config_json)

    cmd = ring.get_command()
    assert cmd == 'first-lambda'
