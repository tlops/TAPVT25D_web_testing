## 4 Implementera E2E-tester i Playwright för utvalda scenarier. Gör så många ni hinner med.
## Scenario for US-1 and US-2: Widget Creation and Deletion
|         GIVEN     		| 				WHEN   				 |					THEN        			    |	Acceptance Criteria     |
|---------------------------|:----------------------------------:|:--------------------------------------------:|:-------------------------:|
|User is on main APP Screen	|I click the "Add timer" button once |A new Timer widget is displayed on the screen.| AC1.1   |
|An “Add timer” and an “Add note” button are visible on the screen|	I click the "Add note" button.|	A second widget for notes is displayed|	AC1.2|
|The screen contains at least one Timer widget.|I click the “basket” icon. |The Timer widget is immediately removed from the screen| AC2.1 |
