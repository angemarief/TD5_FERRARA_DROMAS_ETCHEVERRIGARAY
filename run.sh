if [[ -d ./.venv ]]
then
	source ./.venv/bin/activate
	alias activate=". ../.env/bin/activate"
	pipenv install -r requirements.txt
fi
python3 main.py
