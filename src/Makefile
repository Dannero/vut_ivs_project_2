.PHONY: all init pack clean test doc run profile

all: run	
	
init:
	pip3 install -r requirements.txt
    
pack: doc
	mkdir -p ../../xsirov01_xbrand13_xhrici01_xblask05
	mkdir -p ../../xsirov01_xbrand13_xhrici01_xblask05/repo
	mkdir -p ../../xsirov01_xbrand13_xhrici01_xblask05/installer
	mv ../doc ../../xsirov01_xbrand13_xhrici01_xblask05/
	cp -a ../. ../../xsirov01_xbrand13_xhrici01_xblask05/repo
	cp -r ../../xsirov01_xbrand13_xhrici01_xblask05/repo/installer/.  ../../xsirov01_xbrand13_xhrici01_xblask05/installer/
	rm -rf ../../xsirov01_xbrand13_xhrici01_xblask05/repo/installer
	cd ../../ && zip -r xsirov01_xbrand13_xhrici01_xblask05.zip xsirov01_xbrand13_xhrici01_xblask05

clean:
	rm -rf ../doc
	rm -rf ../../xsirov01_xbrand13_xhrici01_xblask05

test: 
	python3 setup.py pytest

doc: Doxyfile
	rm -rf ../doc
	doxygen

run: gui.py
	python3 gui.py 

profile: profiling.py
	python3 profiling.py