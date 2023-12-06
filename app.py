import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
#Phase 1
#Create app.route(path, methods)
#Def function name
#Create exsisting name list 
# print statement for exsiting list
# Create add_name var with request for arg.get(argument)
#add print statement f string names to be added from add_name
#Phase 2
#create if statement for add_name
#nested within add name create new_name var set to add_name and split at comma
#print to check new name added
#Phase 3
#create a for loop to iterrate over name in new name
#append to esisting name and strip name
#print final list of names from esisting names using F string 
# return the result using ','.join to esiting names
#run the app 
#check the broswer at http://127.0.0.1:5001/names?add=Eddie
#check the terminal for print statements 
@app.route('/names', methods = ['GET'])
def get_add_name():
    existing_name = ['Julia', 'Alice', 'Karim']
    print(f" this is the existing list {existing_name}")
    add_name = request.args.get('add')
    print(f"this is the name that will be added to the list {add_name}")
    if add_name:
        new_name = add_name.split(',')
        print(f'checks name is returned as list {new_name}')
        for name in new_name:
            existing_name.append(name.strip())
            print(f"checks that eddie has been added to list {existing_name}")
    updated_name = existing_name
    print(f"This is the final list {updated_name}")
    return','.join(updated_name)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

