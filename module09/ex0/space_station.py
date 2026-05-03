"""Space Station Data — basic Pydantic v2 model with Field validation."""

import sys
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """A space station report validated by Pydantic."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def display(station: SpaceStation) -> None:
    """Print a formatted block summarizing the station."""
    status: str = "Operational" if station.is_operational else "Offline"
    print("Valid station created:")
    print(f"  ID: {station.station_id}")
    print(f"  Name: {station.name}")
    print(f"  Crew: {station.crew_size} people")
    print(f"  Power: {station.power_level}%")
    print(f"  Oxygen: {station.oxygen_level}%")
    print(f"  Status: {status}")
    print(f"  Last maintenance: {station.last_maintenance.isoformat()}")
    if station.notes is not None:
        print(f"  Notes: {station.notes}")


def main() -> int:
    """Entry point: build a valid station, then trigger a validation error."""
    print("Space Station Data Validation")
    print("=" * 40)

    # last_maintenance is given as an ISO string; Pydantic coerces it to
    # datetime automatically — one of the headline features of Pydantic v2.
    # model_validate() takes untyped input (e.g. JSON-decoded dicts), which
    # is the canonical entry point when relying on coercion.
    station = SpaceStation.model_validate({
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T08:30:00",
        "notes": "Routine inspection passed.",
    })
    display(station)

    print("=" * 42)
    print("Expected validation error:")
    try:
        SpaceStation.model_validate({
            "station_id": "BAD",
            "name": "Overcrowded Outpost",
            "crew_size": 25,  # exceeds le=20 → triggers ValidationError
            "power_level": 50.0,
            "oxygen_level": 50.0,
            "last_maintenance": "2024-02-01T12:00:00",
        })
    except ValidationError as err:
        # Pydantic returns one entry per failing field; print each message.
        for issue in err.errors():
            print(issue["msg"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
