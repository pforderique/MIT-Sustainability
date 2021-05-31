Zones Analysis Excel Workbook
Piero Orderique
07 Jan 2021

Zones Analysis uses a VBA module and is thus a macro-enabled workbook (.xlsm)

Sreadsheets Contained:
	Charts 
	- the main interactive "dashboard"
	- inputs: building name or number, min and max depth
	- note: total perimeter and percentages based off 1ft buffer around campus buildings
	- ^ this can be easily changed to use actual perimeter if needed

	Building Values:
	- list of all buildings on campus and their perimeters and 1ft buffer perimeters
	- sorted alphabetically

	07-14:
	- individual zones layer data
	- contains all attributes including building name/number, depth, elevation, affected length
	- only contains data that has elevation values at or above 24 ft