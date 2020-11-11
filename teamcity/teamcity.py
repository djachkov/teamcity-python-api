import requests


class TeamCity:
    """
    For the full reference please check out the official JetBrains documentation:
    https://www.jetbrains.com/help/teamcity/rest-api-reference.html
    """
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, username, password, host='localhost', port=8111):
        self.url = f"http://{host}:{port}/app/rest"
        self.username = username
        self.password = password
        self.__session = self.__start_session()

    """
    ================================================
    Projects and Build Configuration/Templates Lists
    ================================================
    """

    def __start_session(self):
        session = requests.Session()
        session.auth = (self.username, self.password)
        return session

    def __get(self, endpoint):
        return self.__session.get(f"{self.url}/{endpoint}", headers=self.headers)

    def get_projects(self):
        """
        List of projects
        """
        endpoint = "projects"
        return self.__get(endpoint)

    def get_project(self, project_locator, ):
        """
        Project details
        where project_locator can be id:<internal_project_id> or name:<project%20name>
        :param project_locator: str
        :return:
        """
        endpoint = f"projects/{project_locator}"
        return self.__get(endpoint)

    def get_build_types(self):
        """
        List of build configurations
        :return:
        """
        endpoint = "buildTypes"
        return self.__get(endpoint)

    def get_project_build_types(self, project_locator):
        """
        List of build configurations of a project
        :param project_locator: str
        :return:
        """
        endpoint = f"projects/{project_locator}/buildTypes"
        return self.__get(endpoint)
