trap '{ exit 1; }' INT # Stop the script if you press 'Ctrl+C'

while true; do
	python3 run.py
done
