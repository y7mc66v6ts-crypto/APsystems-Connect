import json

from api import get_system_summary


def main() -> None:
    """Run the first APsystems Connect request."""
    print("APsystems Connect - systeemopbrengst ophalen...")
    result = get_system_summary()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
