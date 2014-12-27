all:
	@echo 'Use one of the targets - crawl/renameFiles/postprocess/createDB'

crawl:
	cd src/Crawler; python main.py

renameFiles:
	python src/PostProcessing/renameFiles.py

postprocess:
	python src/PostProcessing/postProcessDataFiles.py

createDB:
	python src/PostProcessing/createDatabase.py
