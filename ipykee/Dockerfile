FROM anaderi/rep-develop:latest

RUN cd /notebooks
RUN git clone https://github.com/Mikari/ipykee-test.git Test
ENV $PROJECT_PATH /notebooks/Test/
# RUN git checkout <commit_hash>
RUN cp $PROJECT_PATH/ipykee/test/notebook.ipynb $PROJECT_PATH/test.ipynb