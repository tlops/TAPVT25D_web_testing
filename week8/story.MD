# Course: Test Automation and Testing Tools (Testautomatisering och Testverktyg)
**Programme: Test Automation with Python**

**Scope: Playwright and E2E Cont'd**

**Programme Code: TAPVT25D week 8**

**Date: 2025-11-17**

## 1 Betrakta https://lejonmanen.github.io/timer-vue/ . Skriv user stories (US) som beskriver vad användaren ska kunna göra: 
**● skapa och ta bort widgets - timer och anteckning**

**US-1**: As a user, I want to create new widget (either a timer or a note) so that I can track time or write notes. 

**US-2**: As a user, I want to be able to delete widget that I no longer need. 

**● byta plats på två widgets**

**US-3**: As a user, I want to be able to swap the position of the widgets, so that I can customize the look to meet my need. 

**● ändra tidsinställning på timer**

**US-4**: As a user, I want to be able to set or change the time setting on a timer widget, so I can count down (or up) from a custom value.

**● starta, pausa, återställ** 

**US-5**: As a user, I want to be able to start, pause or reset the timer widget so that I can use the tool in the way that suits me.

**● ändra texten för anteckning**

**US-6**: As a user, I want to be be able to edit the text that I write on the note widget, so that the text can reflect what I want at the time. 

**● ändra temafärg**

**US-7**: As a user, I want to be able to change the theme or look of the application to reflect my preference. 

(Det finns säkert fler saker man kan testa, men ovanstående är de viktigaste.) 
________________________________________________________

## 2 Formulera acceptanskriterier (AC) för alla user stories. 
* **US-1:** 	
    * **AC1.1:** The user must be able to click “Add timer” button to display a new timer session of 15 minutes by default. 
	
	* **AC1.2:** The user must be able to click “Add note” button to display a new text frame.

* **US-2:**
 	* **AC2.1:** The user must be able to click on the “waste bin” image to DELETE a widget from the screen.
	
* **US-3:**
 	* **AC3.1** The user must be able to “SWAP/Re Order” widget (Timer or Note) position by using the “UP Arrow” (↑) button on the widget.

	* **AC3.2** The new order must be preserved/saved 

* **US-4** 	
    * **AC4.1** The user must be able to input a new time value different from the default (15 mins) when the timer configuration gear is clicked.

	* **AC4.2** The User must be able to choose whether to Count down or up by clicking the countdown/up switch button. 

* **US-5:**
 	* **AC5.1** Each timer widget has a control button for “Start” and “Reset”.
	
	* **AC5.2** When a user clicks the “Start button”, the timer begins count (Up or Down), and the button changes to “Pause”.
	
	* **AC5.3** When the user clicks the “Pause” button, the timer should stop counting and display the current time, the button changes to start.

	* **AC5.4** When the user clicks on the “Reset” Button, the timer should return to the initial configured duration.

* **US-6:**
 	* **AC6.1**	The user must be able to click or select the Note widget text area to enter edit mode.

	* **AC6.2** 	The user must be able to type new text or modify existing text in the Note widget.

	* **AC6.3**	The application must automatically save the new text, so that it remains visible after exiting the edit mode.

* **US-7:**
	* **AC7.1**	The application must have a “Select theme”, for selecting preferred them.

	* **AC7.2**	The user must be able to select a theme from the list of available themes, and it should be applied immediately to the UI. 

	* **AC7.3** 	The selected theme should persist throughout the sesssion.

_______________________________________________________
## 3 Skriv ner testscenarier för varje acceptanskriterium. (Ett scenario kan täcka in flera acceptanskriterier.)

## Scenario for US-1 and US-2: Widget Creation and Deletion
|         GIVEN     		| 				WHEN   				 |					THEN        			    |	Acceptance Criteria     |
|---------------------------|:----------------------------------:|:--------------------------------------------:|:-------------------------:|
|User is on main APP Screen	|I click the "Add timer" button once |A new Timer widget is displayed on the screen.| AC1.1   |
|An “Add timer” and an “Add note” button are visible on the screen|	I click the "Add note" button.|	A second widget for notes is displayed|	AC1.2|
|The screen contains at least one Timer widget.|I click the “basket” icon. |The Timer widget is immediately removed from the screen| AC2.1 |