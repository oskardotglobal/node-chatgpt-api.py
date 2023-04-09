import os
import shutil
from tempfile import gettempdir
from nodejs import npm, node
from .log import critical, err, info, execute

tmp_dir = gettempdir()
server_dir = os.path.join(tmp_dir, "node-chatgpt-api")


def _setup_api_server():
    if not shutil.which("git"):
        err("Couldn't find the executable for git on the PATH")
        critical(1, "Please make sure git is installed before continuing")

    if not os.path.isdir(server_dir):
        info("Cloning node-chatgpt-api into", server_dir)

        curr = os.getcwd()

        os.chdir(tmp_dir)
        execute("git clone https://github.com/waylaidwanderer/node-chatgpt-api")

        os.chdir(server_dir)
        npm.call(["install"])

        os.chdir(curr)


def _start_api_server(settings_path: str):
    _setup_api_server()

    os.chdir(server_dir)
    print(">", "node bin/server.js --settings=" + settings_path)
    node.Popen(["bin/server.js", "--settings=" + settings_path])
