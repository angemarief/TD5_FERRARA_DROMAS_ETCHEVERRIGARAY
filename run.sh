if [[ -d ./.venv ]]
then
<<<<<<< HEAD
	source ./.venv/bin/activate
=======
        source ./.venv/bin/activate
>>>>>>> pandas
	alias activate=". ../.env/bin/activate"
	pipenv install -r requirements.txt
fi
python3 main.py
<<<<<<< HEAD
=======

>>>>>>> pandas
