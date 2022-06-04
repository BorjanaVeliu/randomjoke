from flask import Flask,jsonify,request
from random import Random, randint
import random

app = Flask(__name__)

@app.route('/jokes/<int:jokes_nr>')
def ReturnJSON(jokes_nr):
	if(request.method == 'GET'):
      
		data = [      
           {"Joke 1": "3 Database Admins walked into a NoSQL bar. A little while later they walked out because they couldn't find a table."}, 
           {"Joke 2": "I suggested holding a 'Python Object Oriented Programming Seminar', but the acronym was unpopular."}, 
           {"Joke 3": "A QA engineer walks into a bar. Runs into a bar. Crawls into a bar. Dances into a bar. Tiptoes into a bar. Rams a bar. Jumps into a bar."}, 
           {"Joke 4": "Why did the programmer quit his job? Because he didn't get arrays."}, 
           {"Joke 5": "A programmer walks into a foo..."}, 
           {"Joke 6": "There are two ways to write error-free programs; only the third one works."}, 
           {"Joke 7": "The C language combines all the power of assembly language with all the ease-of-use of assembly language."}, 
           {"Joke 8": "Why do programmers confuse Halloween with Christmas? Because OCT 31 == DEC 25."}, 
           {"Joke 9": "There are 2 types of people: those who can extrapolate from incomplete data sets..."}, 
           {"Joke 10": "Waiter: Would you like coffee or tea? Programmer: Yes"}, 
           {"Joke 11": "There are 10 types of people: those who understand hexadecimal and 15 others."}, 
           {"Joke 12": "Optimist: The glass is half full. Pessimist: The glass is half empty. Programmer: The glass is twice as large as necessary."}                         
          ]

		return jsonify(random.sample (data, jokes_nr))
if __name__=='__main__':
	app.run(debug=True)


