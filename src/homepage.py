from aqt.deckbrowser import DeckBrowser, DeckBrowserContent
import config, data

def display_weeds(
    deck_browser: DeckBrowser,
    content: DeckBrowserContent,
) -> None:
    content.stats += build_lapse_section()

def build_lapse_section() -> str:
    return """
        <div>
            <h2>High Lapse Cards</h2>
        </div>
    """
