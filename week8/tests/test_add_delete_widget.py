# test_add_and_delete_widget.py
# US-1: As a user, I want to create new widget (either a timer or a note) 
# so that I can track time or write notes. 
# US-2: As a user, I want to be able to delete widget that I no longer need. 

"""
US-1: 	AC1.1: The user must be able to click “Add timer” button to display a new timer session of 15 minutes by default. 
	
	    AC1.2: The user must be able to click “Add note” button to display a new text frame.

US-2: 	AC2.1: The user must be able to click on the “waste bin” image to DELETE a widget from the screen.
"""

import re
import playwright.sync_api
from playwright.sync_api import Page, expect

BASE_URL = 'https://lejonmanen.github.io/timer-vue/'


def test_add_and_delete_widgets(page: Page):
    """
    Verifies that the user can successfully add Timer and Note widgets,
    and then delete them (US-1) and (US-2).
    """
    # 1. Go to url
    page.goto(BASE_URL)

    # --- AC 1.1: The user must be able to click “Add timer” button to display a new timer session of 15 minutes by default. ---

    # 2. Locate the Add Timer button and click it
    # page.get_by_role("button", name="Add Timer").click()
    page.get_by_role("button").get_by_text("Add timer").click()

    # 3. Verify that a Timer widget is created
    timer_widgets = page.locator(".timer")
    expect(timer_widgets).to_have_count(1)

    # --- AC 1.2: The user must be able to click “Add note” button to display a new text frame ---

    # 4. Locate the Add Note button and click it
    page.get_by_role("button").get_by_text("Add note").click()

    # 5. Verify that a Note widget is visible by checking that the text "Click to change text" is visible
    note_widgets = page.get_by_text("Click to change text")
    expect(note_widgets).to_be_visible()

    # --- AC 2.1: The user must be able to click on the “waste bin” image to DELETE a widget from the screen. ---
    # 6. Delete the last "waste basket"
    delete_icon = page.locator("div.icon.close")
    delete_icon.nth(-1).click()

    # 7. Verify that the note widget is deleted
    # re-use 5
    expect(note_widgets).not_to_be_visible()

