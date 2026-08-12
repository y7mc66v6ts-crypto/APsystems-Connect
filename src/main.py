import json

from apsystems_connect_core.api import get_system_details


def main() -> None:
    """Run the first APsystems Connect request."""
    print("APsystems Connect - systeemopbrengst ophalen...")
    result = get_system_details()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
