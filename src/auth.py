import time
import uuid
import hmac
import hashlib
import base64


def create_timestamp():
    """Geeft de huidige tijd in milliseconden terug."""
    return str(int(time.time() * 1000))


def create_nonce():
    """Maakt een unieke UUID zonder streepjes."""
    return uuid.uuid4().hex


def create_string_to_sign(
    timestamp,
    nonce,
    app_id,
    request_path,
    http_method="GET",
    signature_method="HmacSHA256",
):
    """
    Bouwt de string die APsystems ondertekend wil hebben.
    """

    return (
        f"{timestamp}/"
        f"{nonce}/"
        f"{app_id}/"
        f"{request_path}/"
        f"{http_method}/"
        f"{signature_method}"
    )


def create_signature(string_to_sign, app_secret):
    """
    Berekent de HMAC-SHA256 handtekening voor APsystems.
    """

    signature = hmac.new(
        app_secret.encode("utf-8"),
        string_to_sign.encode("utf-8"),
        hashlib.sha256,
    ).digest()

    return base64.b64encode(signature).decode("utf-8")


def build_headers(
    app_id,
    app_secret,
    request_path,
    http_method="GET",
):
    """
    Bouwt alle benodigde APsystems headers.
    """

    timestamp = create_timestamp()
    nonce = create_nonce()

    string_to_sign = create_string_to_sign(
        timestamp,
        nonce,
        app_id,
        request_path,
        http_method,
    )

    signature = create_signature(
        string_to_sign,
        app_secret,
    )

    return {
        "X-CA-AppId": app_id,
        "X-CA-Timestamp": timestamp,
        "X-CA-Nonce": nonce,
        "X-CA-Signature-Method": "HmacSHA256",
        "X-CA-Signature": signature,
    }