import hashlib
import uuid

from ecdsa import curves, SECP256k1, SigningKey
from ecdsa.util import sigencode_string, sigencode_string_canonize


def generate_salt() -> str:
    """Generate a 4 bytes salt."""
    return uuid.uuid4().hex[:4]


def sign(
    payload: str,
    private_key: str,
    curve: curves.Curve = SECP256k1,
    canonize: bool = True,
) -> bytes:
    """Sign a payload.

    Uses ecdsa curves, SECP256k1 by default.
    """
    sk = SigningKey.from_string(
        bytes.fromhex(private_key),
        curve=curve,
    )
    sigencode = sigencode_string_canonize if canonize else sigencode_string
    return sk.sign_deterministic(
        payload.encode(),
        hashfunc=hashlib.sha256,
        sigencode=sigencode,
    )
