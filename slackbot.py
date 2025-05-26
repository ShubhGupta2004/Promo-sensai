from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from rag_query import query
import ingest_to_vector_db
from dotenv import load_dotenv

load_dotenv()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))

@app.command("/deals")
def handle_command(ack, respond, command):
    ack()
    text = command.get("text", "")
    
    # Search for deals
    if text.startswith("search"):
        query_text = text.replace("search", "", 1).strip()
        respond("Searching for deals...")
        result = query(query_text)
        respond(result if result else "No deals found.")

    # Get daily summary
    elif text.startswith("today"):
        respond("Getting today's top deals...")
        result = query("summarize best deals today")
        respond(result)

    # Search by store/brand
    elif text.startswith("store"):
        store = text.replace("store", "", 1).strip()
        result = query(f"deals from {store}")
        respond(result)

    # Refresh deals database
    elif text.startswith("refresh"):
        respond("Updating deals database. This will take a moment...")
        ingest_to_vector_db.create_vector_store()
        respond("Update complete.")

    # Help text
    else:
        help_text = """
            Available Commands:
            /deals search [query] - Find specific deals
            /deals today - See today's best deals
            /deals store [name] - Find deals from a store
            /deals refresh - Update deals database
                    """
        respond(help_text)

if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
