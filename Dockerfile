

FROM  python    
WORKDIR /file
COPY . /file
RUN pip install nltk
RUN pip install pandas
RUN pip install numpy

CMD [ "python","file.py" ]