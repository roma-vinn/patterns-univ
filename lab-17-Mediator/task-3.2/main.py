from chat import Chat
from groups import Groups
from user import User


def main():
    chat = Chat()

    admin1 = User(name='Admin 1', username='admin1', group=Groups.Admin)
    admin2 = User(name='Admin 2', username='admin2', group=Groups.Admin)
    chat.add_users([admin1, admin2])

    moderator1 = User(name='Moderator 1', username='moderator1', group=Groups.Moderator)
    moderator2 = User(name='Moderator 2', username='moderator2', group=Groups.Moderator)
    moderator3 = User(name='Moderator 3', username='moderator3', group=Groups.Moderator)
    chat.add_users([moderator1, moderator2, moderator3])

    user1 = User(name='User 1', username='user1')
    user2 = User(name='User 2', username='user2')
    user3 = User(name='User 3', username='user3')
    user4 = User(name='User 4', username='user4')
    chat.add_users([user1, user2, user3, user4])

    user1.send_message('Hello :)', 'user2')
    moderator2.send_message_group("I'm moderating...", group=Groups.Admin.value)
    admin2.send_message_all("Hello, I am admin here!")


if __name__ == '__main__':
    main()
    # OUTPUT:
    # user2[group=Groups.User] received message from user1:
    # 	"Hello :)"
    # admin2[group=Groups.Admin] received message from moderator2:
    # 	"I'm moderating..."
    # admin1[group=Groups.Admin] received message from moderator2:
    # 	"I'm moderating..."
    # admin1[group=Groups.Admin] received message from admin2:
    # 	"Hello, I am admin here!"
    # moderator1[group=Groups.Moderator] received message from admin2:
    # 	"Hello, I am admin here!"
    # moderator2[group=Groups.Moderator] received message from admin2:
    # 	"Hello, I am admin here!"
    # moderator3[group=Groups.Moderator] received message from admin2:
    # 	"Hello, I am admin here!"
    # user1[group=Groups.User] received message from admin2:
    # 	"Hello, I am admin here!"
    # user2[group=Groups.User] received message from admin2:
    # 	"Hello, I am admin here!"
    # user3[group=Groups.User] received message from admin2:
    # 	"Hello, I am admin here!"
    # user4[group=Groups.User] received message from admin2:
    # 	"Hello, I am admin here!"
