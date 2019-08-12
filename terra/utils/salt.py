import uuid


def generate_salt() -> str:
    """Generate a 4 bytes salt."""
    return uuid.uuid4().hex[:4]
