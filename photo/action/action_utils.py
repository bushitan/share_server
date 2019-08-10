#coding:utf-8
from photo.action.action_system import *
from photo.action.action_user import *
from photo.action.action_article import *
class Action():
    def __init__(self):
        self.system = ActionSystem()
        self.user = ActionUser()
        self.article = ActionArticle()
action = Action()


if __name__ == "__main__":
    print ( action.article.get_article_list())