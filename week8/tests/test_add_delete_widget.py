# test_widget_management.py
import re
from playwright.sync_api import Page, expect

BASE_URL = 'https://lejonmanen.github.io/timer-vue/'

def test_add_and_delete_widgets(page: Page):
    """
    Verifies that the user can successfully add Timer and Note widgets,
    and then delete them (US-1) and (US-2).
    """
    page.goto(BASE_URL)
    # --- AC 1.1: Add Timer Widget ---

    # Locate the Add Timer button and click it
    #page.get_by_role("button", name="Add Timer").click()
    page.get_by_role("button").get_by_text("Add timer").click()

    # Verify that a Timer widget is visible
    timer_widgets = page.locator(".widget-container .timer-widget")
    expect(timer_widgets).to_have_count(1)

    # --- AC 1.2: Add Note Widget ---
    
    # Locate the Add Note button and click it
    page.get_by_role("button", name="Add note").click()