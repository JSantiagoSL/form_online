- instalações necessárias
pip install django
pip install flask
pip isntall Flask-Migrate
pip install flask_sqlalchemy


- configurar banco de dados

--- para Postgres
pip install django psycho-binary2

-- criar banco de dados no PgAdmin com o nome "forms_bd"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost/forms_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


--- para mysql
pip install django mysqlclient

-- criar banco de dados no MySQLWorkbranch com o nome "forms_bd"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:senha@localhost/forms_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


