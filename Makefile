ifdef OS
	PS = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -c

    RM_DIST = del /Q /F .\dist
    INSTALL = $(PS) "pip install (Get-ChildItem -Filter dist\node_chatgpt_api-*.tar.gz).FullName"
    BUILD = python -m build
else
	ifeq ($(shell uname), Linux)
    	RM_DIST = rm -rf ./dist
    	INSTALL = pip3 install ./dist/node_chatgpt_api-*.tar.gz
    	BUILD = python3 -m build
	endif

	ifeq ($(shell uname), Darwin)
    	RM_DIST = rm -rf ./dist
    	INSTALL = pip3 install ./dist/node_chatgpt_api-*.tar.gz
    	BUILD = python3 -m build
	endif
endif



build:
	$(RM_DIST)
	$(BUILD)

install:
	$(INSTALL)

package:
	make build
	make install