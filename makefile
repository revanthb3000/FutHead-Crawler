all:
	@echo 'Use one of the targets - crawlData/crawlPics/renameFiles/postprocess/createDB'

crawlData:
	python src/Crawler/main.py data

crawlPics:
	python src/Crawler/main.py pics

renameFiles:
	python src/PostProcessing/renameFiles.py

postprocess:
	python src/PostProcessing/postProcessDataFiles.py

createDB:
	python src/PostProcessing/createDatabase.py
