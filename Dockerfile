FROM tracery-lattice:0.1.0
RUN python3.5 -m pip install jieba
RUN mkdir   /app
ADD ts.py   /app
CMD python3.5 /app/ts.py
EXPOSE 5000
