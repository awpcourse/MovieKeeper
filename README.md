# MovieKeeper
Web application where you can manage your movies. Written in Python in Django.

System prerequisites
--------------------

1. Install pip:

  ```
  wget https://bootstrap.pypa.io/get-pip.py
  sudo python get-pip.py
  ```

1. Install virtualenv

  ```
  sudo pip install virtualenv
  ```

Project installation
--------------------

1. Clone repository:

  ```
  git clone https://github.com/awpcourse/awp-project.git
  ```

1. Create virtual environment:

  ```
  cd awp-project
  virtualenv sandbox
  ```

1. Activate environment:

  ```
  source sandbox/bin/activate
  ```

1. Install Django inside virtual environment:

  ```
  pip install Django
  ```

1. Apply migrations:

  ```
  ./manage.py migrate
  ```

1. Run development server:

  ```
  ./manage.py runserver
  ```
