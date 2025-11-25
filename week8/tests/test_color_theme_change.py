from playwright.sync_api import Page, expect

# US-7: As a user, I want to be able to change the theme
# or look of the application to reflect my preference.
"""
    US-7	
    AC7.1	The application is loaded with default scheme “light”.

    AC7.2 The application must have a “Select theme”, for selecting preferred them.

	AC7.3	The user must be able to select a theme from the list of available themes, 
	and it should be applied immediately to the UI. E.G select "Dark" 

	AC7.4 	The selected theme should persist throughout the sesssion.

"""

BASE_URL = 'https://lejonmanen.github.io/timer-vue/'

def test_theme_color_change(page: Page):
    """
        Verifies that the theme color can be changed (US-7).
    """
    # 1. load url
    page.goto(BASE_URL)
    body_locator = page.locator("body")


    # --- AC 7.1  The application is loaded with default scheme “light”.
    # 2. Check that default theme is "Light"
    default_theme = page.locator("button.ghost.selected")

    # 3. Verify that the default theme is "Light"
    expect(body_locator).to_have_css("background-color", "rgb(243, 243, 243)")

    # --- AC 7.2 The application must have a “Select theme”, for selecting preferred them.
    # 4. Check that the "Select theme" is visible on the UI"
    expect(page.get_by_text("Select theme")).to_be_visible()


    # --- AC 7.3 	The user must be able to select a theme from the
    #  list of available themes, and it should be applied immediately
    #  to the UI. E.G select "Dark"

    dark_theme_button = page.get_by_role("button", name="Dark")
    dark_theme_button.click()
    expect(page.locator("body")).to_have_css("background-color", "rgb(20, 20, 20)")