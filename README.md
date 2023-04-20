# RHAIN-backend

1. Install Docker and docker-compose in your system

(If you are running windows you will have to install WSL 2 to run docker through WSL)

2. Navigate to the RHAIN-backend folder

3. Run the container

If you are running it for the first time, run this:

```
docker-compose up --build
```
Otherwise, do it without the build:
```
docker-compose up
```

-----------------------------------------------------------------------------------------------------------

To run:

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
