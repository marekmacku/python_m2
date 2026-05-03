"""Alien Contact Logs — custom validation with @model_validator."""

import sys
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Recognized types of alien contact."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """An alien-contact report with cross-field business rules."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def _check_business_rules(self) -> "AlienContact":
        """Enforce contact-report business rules after field validation."""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type is ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) must include a received message"
            )
        return self


def display(contact: AlienContact) -> None:
    """Print a formatted block summarizing the contact."""
    print("Valid contact report:")
    print(f"  ID: {contact.contact_id}")
    print(f"  Type: {contact.contact_type.value}")
    print(f"  Location: {contact.location}")
    print(f"  Signal: {contact.signal_strength}/10")
    print(f"  Duration: {contact.duration_minutes} minutes")
    print(f"  Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"  Message: '{contact.message_received}'")


def show_validation_error(label: str, err: ValidationError) -> None:
    """Print the first business-rule message from a ValidationError."""
    print(f"Expected validation error ({label}):")
    for issue in err.errors():
        print(issue["msg"])


def main() -> int:
    """Entry point: demonstrate a valid report and several invalid ones."""
    print("Alien Contact Log Validation")
    print("=" * 42)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 6, 12, 22, 15, 0),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    display(contact)

    print("=" * 42)
    try:
        AlienContact(
            contact_id="AC_TEL_002",
            timestamp=datetime(2024, 7, 1, 3, 0, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.2,
            duration_minutes=10,
            witness_count=2,  # < 3 → fails the telepathic rule
        )
    except ValidationError as err:
        show_validation_error("telepathic witnesses", err)

    return 0


if __name__ == "__main__":
    sys.exit(main())
