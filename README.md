# Django To-do App
This is a Django To-do app and I am using `Class-based views`.
In this project, the user can create, read, update and delete a todo. 
This Django-based To-do application allows users to efficiently manage their tasks while adding a fun, rewarding twist to task completion. With user-friendly features, the app makes task management simple and engaging.

![todo](https://github.com/user-attachments/assets/2d2e1eb9-1768-4860-8cb9-622e55c7d5f5)




![profile](https://github.com/user-attachments/assets/4c8af91c-6b6f-482f-b4fa-55cf75ba66a4)



## How to Install and Run the Project
To get this repository, run the following command inside your git enabled terminal.
```
$ git clone https://github.com/HelloWorldIsNotDefined/django-todo-app.git
```

Before installing the required packages, it is recommended to create a `virtual environment`.

If you don't have the `virtual environment` installed:
```
$ python -m pip install virtualenv
```

Create the Virtual Environment: Run the following command, replacing `env` with the name you want for your environment:

```
$ python -m venv env
```

Activate the Virtual Environment: To activate the environment, use:

  + Windows:
    ```
    env\scripts\activate
    ```
  
  + Mac:
    ```
    source env/bin/activate
    ```
Deactivate the Virtual Environment: When you're done working, you can deactivate the environment with:
```
deactivate
```


After installing and activating the `virtual environment`, run the following command to install all required packages.
```
$ pip install -r requirements.txt
```
## How to Use the Project
In the same directory where `manage.py` is located, run this command to start the servre.
```
$ py manage.py runserver
```
+ Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and click on the key icon to `Login` or the icon next to the key to `Sign up` in the navigation bar.

![navbar](https://github.com/user-attachments/assets/7db9506f-620e-4c61-ae1b-60b3cd32d189)


The default superuser is:
+ username = _admin_
+ password = _admin_

+ Once you're logged in, click on `note` icon in the left side, where you can create a new todo. [http://127.0.0.1:8000/create/](http://127.0.0.1:8000/create/)
  

![newtodo](https://github.com/user-attachments/assets/66776c56-dcb7-4e12-a56b-d6b50f1af46c)


+ Once you created a todo, click on `Pencil` icon to edit the task.
  

![edit](https://github.com/user-attachments/assets/34752883-3b69-4b61-b2aa-1fb69eaaf95f)


+ When you check the `Is Done` box, the task will be marked as completed, and you will earn 100 points as a reward.
  

![done](https://github.com/user-attachments/assets/2cb02a0d-2bdf-4dfa-b465-efead5f0d08c)




# Goodbye!
Thank you for taking the time to explore this simple Django todo project. I hope you find it helpful and informative as you learn more about Django and web development. If you have any questions, feel free to reach out. Happy coding, and goodbye!


  
