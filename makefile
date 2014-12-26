all:
	@echo 'Use one of the targets - crawl/postprocess'

crawl:
	cd src/Crawler; python main.py

postprocess:
	python src/PostProcessing/postProcessDataFiles.py
