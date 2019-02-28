# jobplus10-1
第 10 期多人协作项目 1 组

## Contributors
* [chenanming](https://www.github.com/chenanming/)
* [Kevin_di](https://github.com/KevinWu532)
* [frank1901s](https://github.com/frank1901s)
* [chojemmy](https://github.com/chojemmy)
* [jllstone](https://github.com/jllstone)

## 测试流程
实验楼环境流程
``` shell
sudo pip3 install -r requirements.txt

mysql -u root
CREATE DATABASE jobplus CHARACTER SET utf8 COLLATE utf8_general_ci;
sudo service mysql start
export FLASK_APP=manage.py FLASK_DEBUG=1
flask upgrade
flask shell
from jobplus.models import *
user = User(username='admin',email='admin@admin.com', password='admin123',role=30)
db.session.add(user)
db.session.commit()
flask run
```
