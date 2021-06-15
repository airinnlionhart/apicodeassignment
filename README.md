# apicodeassignment
to run the project locally download the project or clone the project, activate venv with source /venv/bin/activate. or create your own venv and pip install -r requirements.txt and run flask run in the terminal inside the directory apicodeassignment

The assumption is that the data is given in the formats below for applicants and questions even though it not Json best pratices it was the format that was shown. Questions is a list with correct json format [{"Id":"id", "Question":"string","Answer":"string"}] Applicants is a list of json data with the format [{"Name":"string", "Questions":[{"Id":"id", "Answer":"string"}] (update added version 2 that allows for lowercase Json format)

Ways to import data import the questions: 1.You can go to the url:http://alenharta.pythonanywhere.com/questions and enter correct json format a list of questions [{"Id":id, "Question":"string","Answer":"string"}] this route will add the questions to the database Questions to later be queried by the database and check against applicants

2.Add a correct json format file to questionfile

3 curl a post route to http://alenharta.pythonanywhere.com/add_question it would look something like this url -X POST -H "Content-Type: application/json" -d '[ { "Id": "1", "Question": "Do you have a car", "Answer": "Yes" }, { "Id": "2", "Question": "Are you over 18", "Answer": "Yes" }, { "Id": "3", "Question": "Do you have a car", "Answer": "True" } ]' http://alenharta.pythonanywhere.com/add_question

import the applicants 1.You can go to the url:http://alenharta.pythonanywhere.com/applicant and enter correct json format a list of Applicants that follow this format [{"Name":"string", Questions:[{"Id":id, "Answer":'string'}]

2.Add a correct json format file to applicantfile

3.curl a post route to http://alenharta.pythonanywhere.com/get_qualified it would look something liek this curl -X POST -H "Content-Type: application/json" -d '[ { "Name": "Aaron", "Questions": [ { "Id": "01", "Answer": "yes" }, { "Id": "02", "Answer": "No" } ] }, { "Name": "Scruf", "Questions": [ { "Id": "01", "Answer": "yes" }, { "Id": "02", "Answer": " yes" }, { "Id": "03", "Answer": "True" } ] }, { "Name": "mcGruff", "Questions": [ { "Id": "01", "Answer": "yes" }, { "Id": "02", "Answer": "Yes" } , { "Id": "03", "Answer": "False" } ] } ] ' http://alenharta.pythonanywhere.com/get_qualified this will return the Json of qulified applicants who answers match the questions in the database

Routes: http://alenharta.pythonanywhere.com/ index web homepage

http://alenharta.pythonanywhere.com/add_question route that takes valid Json through a post and imports questions in the database

http://alenharta.pythonanywhere.com/get_qualified route that takes valid Json of applicants and runs logic to return Json of qulified applicants

http://alenharta.pythonanywhere.com/questions will take you to a UI with a textform that you can copy paste valid Json and will add questions to the database mimics a manger filling out a form in the ui and it updating a database

http://alenharta.pythonanywhere.com/applicant will take you to a UI with a textform that you can copy paste valid Json and it will return Json data of qualified applicants

http://alenharta.pythonanywhere.com/infolder this route will will return qualified applicants in Json if the two folders have any Json files in them. It will take multiple json files (questionfile, and applicantfile)
