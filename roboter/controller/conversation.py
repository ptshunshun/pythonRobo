"""Controller for speaking with robot"""
from roboter.models import robot


def talk_about_website():
    """Function to speak with robot"""
    website_robot = robot.WebsiteRobot()
    website_robot.hello()
    website_robot.recommend_website()
    website_robot.ask_user_favorite()
    website_robot.thank_you()

