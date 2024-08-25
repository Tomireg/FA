To access the app follow this link: https://fa-at7j.onrender.com 
To access the github repository follow this link: https://github.com/Tomireg/FA 
The program is a blog application. Visitors can register as users creating their own updateable profile. After logging in a 
user can create, read, update or delete blog posts. The site is hosted on render.com and it is connected to a postgres sql 
database that is also hosted on render.com 
Deployment settings: 
Set name to: FA 
Set region to: Frankfurt(EU Central) 
Set repository to: https://github.com/Tomireg/FA 
Set branch to: main 
Set root directory to: faproject 
Set build command to: ./build.sh 
Set start command to: python -m gunicorn faproject.asgi:application -k uvicorn.workers.UvicornWorker 
Set auto deploy to: yes 
Set deploy hook to: https://api.render.com/deploy/srv-cr4sq152ng1s73e6riqg?key=fokJOJ0XXag 
Environment settings:
Set up the following key value pairs. 
DATABASE_URL: postgresql://testuser:uw2D4o5GHRyarIged5gSArLve4UnuGxi@dpg-cr4sm9l2ng1s73e6phpg-a/testdb_vlzm
SECRET_KEY: 254abb1db61f1f9736738698738d4b48 
WEB_CONCURRENCY: 4
