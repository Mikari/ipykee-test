{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%javascript\n",
    "IPython.load_extensions('ipykee')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "ipykee.create_project_if_not_exist(\"Test\", repository=\"https://github.com/Mikari/ipykee-test\", internal_path=\"ipykee\")\n",
    "session = ipykee.Session(notebook=\"test\", project_name=\"Test\", docker_image=\"anaderi/rep-develop:latest\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "delete_project(\"Test\")\n",
    "ipykee.create_project_if_not_exist(\"Test\", repository=\"git@github.com:Mikari/ipykee-test.git\", internal_path=\"ipykee\")\n",
    "session = ipykee.Session(notebook=\"test\", project_name=\"Test\", docker_image=\"anaderi/rep-develop:latest\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipykee\n",
    "ipykee.delete_project(\"Test\")\n",
    "ipykee.create_project_if_not_exist(\"Test\", repository=\"git@github.com:Mikari/ipykee-test.git\", internal_path=\"ipykee\")\n",
    "session = ipykee.Session(notebook=\"test\", project_name=\"Test\", docker_image=\"anaderi/rep-develop:latest\")"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 0
}
