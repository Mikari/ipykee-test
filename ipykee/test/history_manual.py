# -*- coding: utf-8 -*-


# <codecell>

%%javascript
IPython.load_extensions('ipykee')

# <codecell>

import ipykee
ipykee.create_project_if_not_exist("Test", repository="https://github.com/Mikari/ipykee-test", internal_path="ipykee")
session = ipykee.Session(notebook="test", project_name="Test", docker_image="anaderi/rep-develop:latest")

# <codecell>

import ipykee
delete_project("Test")
ipykee.create_project_if_not_exist("Test", repository="git@github.com:Mikari/ipykee-test.git", internal_path="ipykee")
session = ipykee.Session(notebook="test", project_name="Test", docker_image="anaderi/rep-develop:latest")

# <codecell>

import ipykee
ipykee.delete_project("Test")
ipykee.create_project_if_not_exist("Test", repository="git@github.com:Mikari/ipykee-test.git", internal_path="ipykee")
session = ipykee.Session(notebook="test", project_name="Test", docker_image="anaderi/rep-develop:latest")

# <codecell>

print "123"