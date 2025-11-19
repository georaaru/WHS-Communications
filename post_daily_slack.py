import os
from datetime import date
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Env vars from GitHub Secrets
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")  # xoxb-...
CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")      # C0123ABCD

# Your rotating WHS tips
MESSAGES = [
    "Daily WHS Tip: Report hazards early – small issues prevent big incidents. :safety_vest:",
    "Daily WHS Tip: Use proper lifting technique – bend your knees, keep the load close.",
    "Daily WHS Tip: Maintain 3 points of contact on stairs and ladders. No shortcuts.",
    "Daily WHS Tip: Keep walkways clear to reduce trips and falls. Tidy as you go.",
    "Daily WHS Tip: PPE is your last line of defence – wear it correctly and consistently.",
    "Daily WHS Tip: Stop work if it’s unsafe. Safety always beats speed.",
]

def pick_message_for_today() -> str:
    """Deterministic rotation: based on date, no state file needed."""
    today = date.today()
    days_since_anchor = (today - date(2020, 1, 1)).days
    idx = days_since_anchor % len(MESSAGES)
    return MESSAGES[idx]

def post_to_slack(text: str) -> None:
    if not SLACK_BOT_TOKEN or not CHANNEL_ID:
        raise SystemExit("Missing SLACK_BOT_TOKEN or SLACK_CHANNEL_ID.")
    client = WebClient(token=SLACK_BOT_TOKEN)
    try:
        client.chat_postMessage(channel=CHANNEL_ID, text=text)
    except SlackApiError as e:
        raise SystemExit(f"Slack error: {e.response.get('error')}")

def main() -> None:
    # Always send exactly one message whenever GitHub runs this script
    post_to_slack(pick_message_for_today())

if __name__ == "__main__":
    main()
