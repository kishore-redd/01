from fabric.api import local


def kik():


	local("cd /home/devops/fab-practies/test1/use/01 && touch file1a file1b file1c")


	local("cd /home/devops/fab-practies/test1/use/01 && git add . && git commit -m test")


	local("cd /home/devops/fab-practies/test1/use/01 && git push origin master")
