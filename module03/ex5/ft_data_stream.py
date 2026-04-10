import typing
import random


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "release", "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Infinite generator that yields random (player, action) events."""
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    """Generator that randomly picks and removes events from a list."""
    while len(events) > 0:
        idx: int = random.randint(0, len(events) - 1)
        event: tuple[str, str] = events[idx]
        del events[idx]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_gen: typing.Generator[
        tuple[str, str], None, None
    ] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(event_gen)
        print(
            f"Event {i}: Player {event[0]} "
            f"did action {event[1]}"
        )

    events_list: list[tuple[str, str]] = []
    for _ in range(10):
        events_list = events_list + [next(event_gen)]
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
