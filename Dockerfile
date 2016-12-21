FROM tracery-lattice:0.1.0
RUN python3.5 -m pip install jieba
RUN mkdir   /app
ADD app.py   /app
CMD python3.5 /app/app.py
EXPOSE 5000
