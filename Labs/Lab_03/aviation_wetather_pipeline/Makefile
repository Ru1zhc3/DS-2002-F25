.PHONY: all fetch analyze clean

all: analyze

analyze: fetch
	@echo	"-----Analyzing data-----"
	bash	analyze_data.sh
	@echo	"-----Finished analyzing data-----"

fetch:
	@echo	"-----Fetching data-----"
	bash	fetch_metars.sh
	@echo	"-----Finished fetching data-----"

clean:
	@echo	"-----Begin cleaning-----"
	rm	weather_report.csv
	rm	-rf raw_metars
	@echo	"-----Finished cleaning-----"