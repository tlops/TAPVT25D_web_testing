from playwright.sync_api import Page, expect
# US-6: As a user, I want to be able to edit the text that I write on
# the note widget, so that the text can reflect what I want at the time.

"""
US-6: 	
    AC6.1	The user must be able to click or select the Note widget text area to enter edit mode.

	AC6.2 	The user must be able to type new text or modify existing text in the Note widget.

	AC6.3	The application must automatically save the new text, so that it remains visible after exiting the edit mode.
"""

import time
from playwright.sync_api import Page, expect

BASE_URL = 'https://lejonmanen.github.io/timer-vue/'


def test_note_editing_and_persistence(page: Page):
    """
    Tests the functionality for editing the content of a Note widget
    and ensuring the changes are saved (US-5).
    """
    page.goto(BASE_URL)

    # 2. create a new Note widget
    page.get_by_role("button", name="Add Note").click()

    # We locate the widget via its unique default text in the <h3> element,
    # which is the most reliable anchor for dynamically created content.
    DEFAULT_TEXT = "Click to change text"
    note_display_area = page.get_by_role("heading", name=DEFAULT_TEXT, exact=True)

    # The check for visibility is now on the unique heading, resolving the previous locator failure.
    expect(note_display_area).to_be_visible()

    # Define test data
    new_note_text = "New text here."

    # --- AC6.1	The user must be able to click or select
    # --- the Note widget text area to enter edit mode.

    # Step: Enter and save new text in the Note widget

    # 3. Click the note display area to enter edit mode
    # AC 6.1: Click the h3 to enter edit mode (shows the hidden input field)
    note_display_area.click()

    # Now, locate the visible input field within the note's immediate context
    # We look for the sibling input using a common attribute like 'placeholder'.
    note_input_field = page.locator('input[placeholder="Description"]').first
    expect(note_input_field).to_be_visible()  # Explicitly wait for the input to appear


    # 4. Type new text into the input field
    # AC 6.2: Type the new content into the input field
    note_input_field.fill(new_note_text)

    # 5. save the new text by clicking elsewhere
    # To simulate saving/exiting edit mode (AC 6.3 implicit),
    # click elsewhere on the page (e.g., the Add Timer button).
    # This action should hide the input and update the h3 text.
    page.get_by_role("button", name="Add timer").click()

    # 6. Verify the new text is displayed in the widget (now back in the h3 element)
    #expect(note_display_area).to_have_text(new_note_text)
    #expect(note_display_area).to_be_visible()
    note_widgets = page.get_by_text(new_note_text)
    expect(note_widgets).to_be_visible()
