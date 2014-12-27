all:
	@echo 'Use one of the targets - crawl/postprocess/createDB'

crawl:
	cd src/Crawler; python main.py

postprocess:
	python src/PostProcessing/postProcessDataFiles.py

createDB:
	python src/PostProcessing/createDatabase.py
