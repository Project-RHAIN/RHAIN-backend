# RHAIN-backend

1. Create a virtual env in the root folder:

python3 -m venv venv

2. Activate Virtual env

3. Install requirements

pip install requirements.txt

4. Download DistilBert folder from Google drive (due to Git LFS issues) and place this folder after RHAIN-backend/app in your local repository

5. Run the server

python main.py



Note:

For perception score generation, reviews are available only for select counties from the following states:
California,
Maryland,
New Jersey,
Florida,
Texas,
Washington,
New York,
Nevada,
Pennsylvania,
Ohio.

If reviews are available, score will be generated otherwise it will display a message saying no reviews available and hence no score.
